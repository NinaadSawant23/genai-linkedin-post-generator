import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def extract_metadata(post):
    template = """
    You are given a LinkedIn post. Your task is to extract:
    1. The number of lines
    2. The language of the post (should be English)
    3. Up to 2 tags summarizing the post

    ⚠️ Output a valid JSON only. Do not include any explanation or markdown. Just return the JSON object.

    Example format:
    {{
      "line_count": 12,
      "language": "English",
      "tags": ["Career Advice", "Job Search"]
    }}

    Here is the post:
    {post}
    """
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"post": post})

    raw_output = response.content.strip()

    try:
        start = raw_output.find('{')
        end = raw_output.rfind('}') + 1
        cleaned_json = raw_output[start:end]
        res = json.loads(cleaned_json)
    except Exception as e:
        print("🔴 RAW LLM OUTPUT:\n", raw_output)
        raise OutputParserException(f"Failed to extract valid JSON from LLM output: {e}")

    return res


def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post["tags"])

    unique_tags_list = ", ".join(unique_tags)

    template = """
    I will give you a list of tags. You need to unify tags with the following requirements:
    1. Tags are unified and merged to create a shorter list. 
       Example: "Resume Writing", "LinkedIn Strategy", "Cover Letter Tips" → "Personal Branding"  
       Example: "Motivation", "Inspiration", "Career Advice" → "Career Development"
       Example: "Job Change", "Career Pivot" → "Career Transition"

    2. Use Title Case for tags. For example: "Career Growth", "Job Search"

    3. Return a valid JSON. No preamble.

    4. Output format: 
    {{
      "OldTag1": "UnifiedTag",
      "OldTag2": "UnifiedTag",
      ...
    }}

    Here is the list of tags: 
    {tags}
    """
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"tags": unique_tags_list})

    try:
        start = response.content.find('{')
        end = response.content.rfind('}') + 1
        raw_json = response.content[start:end]
        res = json.loads(raw_json)
    except Exception as e:
        print("🔴 RAW TAG OUTPUT:\n", response.content)
        raise OutputParserException(f"Failed to extract valid tag mapping: {e}")

    return res


def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []

    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)
        for i, post in enumerate(posts):
            try:
                metadata = extract_metadata(post["text"])
                post_with_metadata = post | metadata
                enriched_posts.append(post_with_metadata)

                print(f"Post {i}: Enriced")
            except Exception as e:
                print(f"⚠️ Error processing post {i}: {e}")
                continue  # skip this post

    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post["tags"]
        new_tags = {unified_tags.get(tag, tag) for tag in current_tags}
        post["tags"] = list(new_tags)

    with open(processed_file_path, "w", encoding="utf-8") as outfile:
        json.dump(enriched_posts, outfile, indent=4)

    print(f"✅ Processed {len(enriched_posts)} posts. Output saved to {processed_file_path}")


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
