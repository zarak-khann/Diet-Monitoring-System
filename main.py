import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# ======================================
# 1. Load Dataset
# ======================================
df = pd.read_csv("data/processed/final_nutrition_dataset.csv")
print("\nDataset Loaded Successfully")
print("Shape:", df.shape)


# ======================================
# 2. Separate Features & Target
# ======================================
X = df.drop(columns=["food", "category"])
y = df["category"]


# ======================================
# 3. Encode Target Labels
# ======================================
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

print("\nEncoded Classes:", encoder.classes_)


# ======================================
# 4. Train-Test Split (Stratified)
# ======================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)


# ======================================
# 5. Feature Scaling
# ======================================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ======================================
# 6. Train Random Forest Model
# ======================================
model = RandomForestClassifier(
    n_estimators=200,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train_scaled, y_train)

print("\nModel Training Completed")


# ======================================
# 7. Model Evaluation
# ======================================
y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, target_names=encoder.classes_))

print("Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))


# ======================================
# 8. Feature Importance
# ======================================
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nTop Important Features:\n")
print(feature_importance.head(10))


# ======================================
# 9. Save Model Artifacts
# ======================================
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(encoder, "encoder.pkl")

print("\nModel, Scaler, and Encoder Saved Successfully!")