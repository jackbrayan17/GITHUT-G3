import os

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Chargement des donnees
print("Chargement du dataset...")
df = pd.read_csv("data/raw/housing.csv")
print(f"Dataset charge : {len(df)} lignes")

# Preparation des features
df["quartier_code"] = df["quartier"].astype("category").cat.codes
features = [
    "surface",
    "chambres",
    "age",
    "distance_centre",
    "etage",
    "parking",
    "piscine",
    "garage",
    "quartier_code",
]
X = df[features]
y = df["prix"]

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {len(X_train)} | Test: {len(X_test)}")

# Entrainement
print("Entrainement du modele...")
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MAE  : {mae:,.0f}")
print(f"R2   : {r2:.4f}")

# Sauvegarde du modele
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/housing_model.joblib")
print("Modele sauvegarde dans models/housing_model.joblib")
