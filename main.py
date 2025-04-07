import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from models.predictor import predict_engagement
import re

def highlight_hashtags(text: str) -> str:
    """
    Wraps hashtags (words starting with #) in a span with custom styling.
    """
    # This regex finds words that start with #
    highlighted_text = re.sub(
        r"(#\w+)",
        r'<span style="color:#FF4B4B; font-weight:bold;">\1</span>',
        text
    )
    return highlighted_text

def main():
    st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")
    st.title("🚀 LinkedIn Post Generator with AI")

    st.markdown("Craft engaging LinkedIn posts using AI + real-world examples. Choose your preferences below and click **Generate**!")

    # === Load Tag Options ===
    fs = FewShotPosts()
    tags = fs.get_tags()
    lengths = ["Short", "Medium", "Long"]
    languages = ["English", "Spanish"]
    tones = ["Professional", "Inspirational", "Casual", "Informative", "Storytelling", "Humorous", "Persuasive"]

    # === User Input Section ===
    st.markdown("---")
    st.subheader("🛠️ Post Preferences")

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            selected_tag = st.selectbox("🎯 Topic", options=tags)
        with col2:
            selected_len = st.selectbox("📏 Length", options=lengths)
        with col3:
            selected_lang = st.selectbox("🌍 Language", options=languages)

        col4, col5 = st.columns([2, 1])
        with col4:
            selected_tone = st.selectbox("🎭 Tone", options=tones)
        with col5:
            selected_hash = st.slider("🏷️ Number of Hashtags", min_value=0, max_value=5, value=2, help="How many hashtags to include at the end")

    st.markdown("---")

    # === Generate Button & Output Section ===
    if st.button("✨ Generate Post"):
        post = generate_post(length=selected_len, language=selected_lang, title=selected_tag, tone=selected_tone, hash_tags=selected_hash)

        highlighted_post = highlight_hashtags(post)

        st.subheader("📝 Generated LinkedIn Post")
        st.write(highlighted_post, unsafe_allow_html=True)

        line_count = post.count("\n") + 1
        predicted = predict_engagement(post, line_count)

        st.success(f"🔮 Predicted Engagement: `{predicted}` likes/comments")

    st.markdown("---")
    st.caption("Built with 💡 GenAI & LangChain | by Ninaad")

if __name__ == '__main__':
    main()
