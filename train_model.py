import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import pickle
import os
import random

random.seed(42)

positive_templates = [
    "I love this {}, it is absolutely amazing!",
    "Best {} I have ever used, highly recommend!",
    "Excellent quality {}, very satisfied!",
    "Outstanding {}, works perfectly!",
    "Great {}, exceeded my expectations!",
    "Fantastic {}, will definitely buy again!",
    "Incredible {} experience, very happy!",
    "Perfect {}, exactly what I needed!",
    "Amazing {}, top quality product!",
    "Superb {}, completely worth the money!"
]

negative_templates = [
    "Terrible {}, complete waste of money!",
    "Worst {} I have ever bought, very disappointed!",
    "Horrible quality {}, broke immediately!",
    "Awful {}, does not work at all!",
    "Very bad {}, would not recommend!",
    "Disgusting {}, never buying again!",
    "Poor {} quality, very unhappy!",
    "Dreadful {}, total disappointment!",
    "Useless {}, complete garbage!",
    "Worst experience with {}, very angry!"
]

items = ['product', 'service', 'item', 'purchase', 'experience',
         'device', 'software', 'app', 'tool', 'solution']

texts = []
labels = []

for _ in range(250):
    template = random.choice(positive_templates)
    item = random.choice(items)
    texts.append(template.format(item))
    labels.append(1)

for _ in range(250):
    template = random.choice(negative_templates)
    item = random.choice(items)
    texts.append(template.format(item))
    labels.append(0)

combined = list(zip(texts, labels))
random.shuffle(combined)
texts, labels = zip(*combined)

df = pd.DataFrame({'text': texts, 'sentiment': labels})

print("Dataset generated successfully!")
print(f"Total samples: {len(df)}")
print(f"Positive: {sum(df['sentiment'])}, Negative: {len(df) - sum(df['sentiment'])}")

X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['sentiment'], test_size=0.2, random_state=42
)

mlflow.set_experiment("sentiment-analysis")

with mlflow.start_run():
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000, C=1.0)
    model.fit(X_train_vec, y_train)

    predictions = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, predictions)

    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_param("max_features", 5000)
    mlflow.log_param("ngram_range", "1,2")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "sentiment-model")

    print("Model logged to MLflow!")

os.makedirs('model', exist_ok=True)
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model saved successfully!")
print("Training complete!")
