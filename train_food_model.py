import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "data", "processed", "final_nutrition_dataset.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")

print("="*60)
print("TRAINING FOOD IDENTIFIER MODEL")
print("="*60)
print(f"Dataset: {DATASET_PATH}")
print(f"Models will be saved to: {MODEL_DIR}")
print("="*60)

# ---------------- LOAD DATASET ----------------
try:
    df = pd.read_csv(DATASET_PATH)
    print(f"\n✅ Dataset loaded: {len(df)} rows")
    
    # Standardize column names
    df.columns = df.columns.str.strip()
    
    df.rename(columns={
        "Caloric Value": "calories",
        "Fat": "fat",
        "Saturated Fats": "saturated_fat",
        "Carbohydrates": "carbohydrates",
        "Sugars": "sugars",
        "Protein": "protein",
        "Dietary Fiber": "fiber",
        "Sodium": "sodium"
    }, inplace=True)
    
    print(f"Columns: {df.columns.tolist()}")
    print(f"Categories: {df['category'].unique()}")
    
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    exit()

# ---------------- PREPARE DATA ----------------
print("\n" + "="*60)
print("PREPARING DATA")
print("="*60)

# Select features
feature_columns = ['calories', 'fat', 'protein', 'carbohydrates']
X = df[feature_columns]
y = df['category']

print(f"Features: {feature_columns}")
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")

# Encode target
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
print(f"Categories encoded: {label_encoder.classes_}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, 
    test_size=0.2, 
    random_state=42,
    stratify=y_encoded
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("✅ Features scaled")

# ---------------- TRAIN MODEL ----------------
print("\n" + "="*60)
print("TRAINING MODEL")
print("="*60)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train_scaled, y_train)
print("✅ Model trained")

# Evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Test Accuracy: {accuracy:.2%}")

# ---------------- SAVE MODEL ----------------
print("\n" + "="*60)
print("SAVING MODEL FILES")
print("="*60)

model_path = os.path.join(MODEL_DIR, "food_model.pkl")
scaler_path = os.path.join(MODEL_DIR, "scaler.pkl")
encoder_path = os.path.join(MODEL_DIR, "label_encoder.pkl")

joblib.dump(model, model_path)
joblib.dump(scaler, scaler_path)
joblib.dump(label_encoder, encoder_path)

print(f"✅ Model saved: {model_path}")
print(f"✅ Scaler saved: {scaler_path}")
print(f"✅ Encoder saved: {encoder_path}")

print("\n" + "="*60)
print("TRAINING COMPLETE!")
print("="*60)
print("\nYou can now run your Flask app:")
print("cd web_app")
print("python app.py")