# LinkedIn Post Generator with GenAI 🧠✍️

![GenAI](https://img.shields.io/badge/GenAI-LLaMA3-orange)
![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-red)
![LangChain](https://img.shields.io/badge/LLM-Powered_by_LangChain-blueviolet)
![Python](https://img.shields.io/badge/Python-3.9%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)

An AI-powered LinkedIn post generator built with GenAI (LLaMA 3), LangChain, and Streamlit. This tool uses real-world LinkedIn content and few-shot learning to generate personalized, high-quality posts — with customizable tone, length, language, and hashtags. It also includes a machine learning-based engagement predictor using RandomForest to estimate post performance.

> 💬 Want to grow your personal brand on LinkedIn? Let AI do the heavy lifting.

## 🚀 Features

- 🎯 **Topic-Based Generation** – Select from real LinkedIn categories like *Career Advice*, *Job Search*, and more.
- 🎭 **Tone Control** – Choose between *Professional*, *Casual*, *Inspirational*, *Storytelling*, etc.
- 📏 **Length Options** – Create posts of various lengths (Short, Medium, Long).
- 🏷️ **Hashtag Control** – Specify the number of hashtags to include.
- 🧠 **Few-Shot Learning** – Posts are generated using real examples as context.
- 🔮 **Engagement Prediction** – A machine learning model estimates likes/comments using post characteristics.
- 💡 **Beautiful UI** – Powered by Streamlit with custom styling and helpful UX.


## 🧠 Technologies Used

| Category         | Tools / Libraries                         |
|------------------|--------------------------------------------|
| **LLM & GenAI**   | LLaMA 3 (via LangChain + Groq API)         |
| **Web UI**        | Streamlit                                  |
| **ML Model**      | scikit-learn, RandomForestRegressor        |
| **Data Handling** | Pandas, TextBlob, JSON                     |
| **Other**         | dotenv, joblib, langchain, python-environ |

## 🧪 Engagement Prediction Model

- 📍 Located in models/engagement_model.pkl
- 🤖 Model: RandomForestRegressor (via scikit-learn)
- 🧾 Features used:
  - Word Count
  - Line Count
  - Sentiment Score

To retrain this model
```
cd models
python engagement_prediction.py
```

## ⚙️ Installation & Setup
1. Clone the Repository
```
git clone https://github.com/NinaadSawant23/linkedin-post-generator.git
cd linkedin-post-generator
```
2. Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Add Your API Key
Create a .env file in the root folder and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```
5. If you want to re-process the raw data 
```
python preprocess.py
```
6. Run the application
```
streamlit run main.py
```

## 📌 Usage
1. Select post preferences: topic, tone, language, length and hashtag count.
2. Click ✨ Generate Post.
3. View your AI-generated LinkedIn post in the output panel.
4. See predicted likes/comments using the built-in ML model.
5. Copy and use the content directly on LinkedIn 🚀

## 🖼️ Screenshots
![Project Screenshot](/screenshots/form.png)
![Project Screenshot](/screenshots/post.png)


## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🙌 Acknowledgements
- LangChain
- Groq
- Streamlit
- Everyone posting great content on LinkedIn 🙏
![image](https://github.com/user-attachments/assets/c2443a93-f63e-4d58-8b7f-1703a34f2741)
