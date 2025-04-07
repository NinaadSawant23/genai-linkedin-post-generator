import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from textblob import TextBlob

# Load preprocessed posts
with open("../data/processed_posts.json", encoding="utf-8") as f:
    df = pd.read_json(f)

# Feature Engineering
df['word_count'] = df['text'].apply(lambda x: len(x.split()))
df['sentiment'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

X = df[['word_count', 'line_count', 'sentiment']]
y = df['engagement']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "engagement_model.pkl")
print("Model trained and saved successfully!")
