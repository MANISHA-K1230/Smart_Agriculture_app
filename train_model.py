import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

os.makedirs("model", exist_ok=True)

data = pd.read_csv("dataset/crop_data.csv")

X = data.drop("crop", axis=1)
y = data["crop"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model/crop_model.pkl")

print("Model saved successfully")