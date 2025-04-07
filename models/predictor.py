import pandas as pd
import joblib
from textblob import TextBlob

model = joblib.load("models/engagement_model.pkl")

def predict_engagement(text: str, line_count: int) -> int:
    word_count = len(text.split())
    sentiment = TextBlob(text).sentiment.polarity

    # Use DataFrame with correct column names
    input_df = pd.DataFrame([{
        "word_count": word_count,
        "line_count": line_count,
        "sentiment": sentiment
    }])

    predicted = model.predict(input_df)[0]
    return int(predicted)
