from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_lines(length):
    if length == 'Short':
        lines = "5-10 lines"
    elif length == "Medium":
        lines = "10-20 lines"
    else:
        lines = "20-30 lines"

    return lines

def get_prompt(title, length, language, tone, hash_tags):

    lines = get_lines(length)
    prompt = f'''
    Generate a linkedin post using the below information. No preamble
    
    1) Topic: {title}
    2) Length: {lines}
    3) Language: {language}
    4) Tone: {tone}
    5) Hash tags: {hash_tags}
    '''

    examples = few_shot.get_filtered_posts(length=length, language=language, tag=title)

    if len(examples) > 0:
        prompt += "6) Refer the following example to understand the writing style."

        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f"\n\nExample {i + 1} \n\n{post_text}"

            if i==1:
                break

    return prompt

def generate_post(title, length, language, tone, hash_tags):
    prompt = get_prompt(title, length, language, tone, hash_tags)
    response = llm.invoke(prompt)
    return response.content

if __name__ == '__main__':
    post = generate_post("Job Search", "Long", "English", "Professional")
    print(post)