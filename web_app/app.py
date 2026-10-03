
import os
import pandas as pd
import joblib
from flask import Flask, render_template, request

# ---------------- FLASK APP ----------------
app = Flask(__name__)

# ---------------- BASE DIRECTORY ----------------
WEB_APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(WEB_APP_DIR)

# ---------------- PATHS ----------------
DATASET_PATH = os.path.join(BASE_DIR, "data", "processed", "final_nutrition_dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "food_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

# ---------------- DEBUG: Print paths ----------------
print("="*50)
print("PATH VERIFICATION")
print("="*50)
print(f"BASE_DIR: {BASE_DIR}")
print(f"\nDataset path: {DATASET_PATH}")
print(f"Dataset exists: {os.path.exists(DATASET_PATH)}")
print(f"\nScaler path: {SCALER_PATH}")
print(f"Scaler exists: {os.path.exists(SCALER_PATH)}")
print(f"\nModel path: {MODEL_PATH}")
print(f"Model exists: {os.path.exists(MODEL_PATH)}")
print(f"\nEncoder path: {ENCODER_PATH}")
print(f"Encoder exists: {os.path.exists(ENCODER_PATH)}")
print("="*50)
# ---------------- LOAD DATASET ----------------
# ---------------- LOAD DATASET ----------------
try:
    df = pd.read_csv(DATASET_PATH)

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

    # ✅ ADD THESE LINES - Define column names
    food_col = "food"  # The food name column
    calorie_col = "calories"  # The renamed calorie column
    
    print("Dataset loaded successfully")
    print(f"Columns: {df.columns.tolist()}")  # Debug: check columns

except Exception as e:
    df = None
    food_col = None
    calorie_col = None
    print("Dataset not loaded:", e)


# ---------------- LOAD MODEL ----------------
# ---------------- LOAD MODEL ----------------
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
    print("Food identifier model loaded successfully")
except Exception as e:
    model = None
    scaler = None
    label_encoder = None
    print(f"Model not loaded: {e}")

# Define column names
food_col = "food"
calorie_col = "calories"

# ---------------- HOME ROUTE ----------------
@app.route("/")
def home():
    return render_template("index.html")



# ================================
# FOOD IDENTIFIER
# ================================

@app.route("/food", methods=["GET", "POST"])
def food():
    matches = None
    prediction = None
    food_details = None
    error = None

    if request.method == "POST":
        if "food" in request.form:
            food_input = request.form["food"].strip()
            if not food_input:
                error = "Enter a food name to search."
            else:
                matches = df[df[food_col].str.contains(food_input, case=False, na=False, regex=False)]

        elif "selected_food" in request.form:
            try:
                idx = int(request.form["selected_food"])
                if idx not in df.index:
                    raise ValueError("The selected food is not available.")
                selected_row = df.loc[idx]

                # Get features (must match training features: calories, fat, protein, carbs)
                features = [[
                    selected_row['calories'],
                    selected_row['fat'],
                    selected_row['protein'],
                    selected_row['carbohydrates']
                ]]

                if scaler is not None and model is not None and label_encoder is not None:
                    # Scale features
                    feature_frame = pd.DataFrame(
                        features, columns=["calories", "fat", "protein", "carbohydrates"]
                    )
                    features_scaled = scaler.transform(feature_frame)
                    
                    # Predict category
                    prediction_encoded = model.predict(features_scaled)[0]
                    predicted_category = label_encoder.inverse_transform([prediction_encoded])[0]
                    
                    # Create prediction message
                    actual_category = selected_row['category']
                    prediction = f"Predicted: {predicted_category} | Actual: {actual_category}"
                    
                    # Food details for display
                    food_details = {
                        'name': selected_row[food_col],
                        'category': actual_category,
                        'predicted': predicted_category,
                        'calories': selected_row['calories'],
                        'protein': selected_row['protein'],
                        'fat': selected_row['fat'],
                        'carbs': selected_row['carbohydrates']
                    }
                else:
                    prediction = "❌ Model not loaded"
                    
            except Exception as e:
                error = str(e)

    return render_template(
        "food.html",
        matches=matches,
        prediction=prediction,
        food_details=food_details,
        error=error
    )

# ================================
# CALORIE CALCULATOR
# ================================

def calculate_calories(row, mass, unit):
    if mass < 0:
        raise ValueError("Mass must not be negative.")

    calories_per_100g = row[calorie_col]

    if unit == "g":
        calories = (calories_per_100g / 100) * mass

    elif unit == "kg":
        calories = (calories_per_100g / 100) * (mass * 1000)

    else:
        raise ValueError("Unit must be g or kg.")

    return round(calories, 2)


@app.route("/calories", methods=["GET", "POST"])
def calories():

    matches = None
    result = None
    error = None

    if request.method == "POST":

        if "food" in request.form:

            food_input = request.form["food"].strip()
            if not food_input:
                error = "Enter a food name to search."
            else:
                matches = df[df[food_col].str.contains(food_input, case=False, na=False, regex=False)]

        elif "selected_food" in request.form:
            try:
                idx = int(request.form["selected_food"])
                if idx not in df.index:
                    raise ValueError("The selected food is not available.")
                mass = float(request.form["mass"])
                unit = request.form["unit"].lower()
                selected_row = df.loc[idx]
                result = calculate_calories(selected_row, mass, unit)
            except (KeyError, TypeError, ValueError) as exc:
                error = str(exc)

    return render_template(
        "calories.html",
        matches=matches,
        result=result,
        error=error
    )

# ================================
# BMR
# ================================

def calculate_bmr(weight, height, age, gender):

    if gender == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161


# ================================
# TDEE
# ================================

def calculate_tdee(bmr, activity):

    activity_levels = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }

    return bmr * activity_levels.get(activity, 1.2)


# ================================
# DIET RECOMMENDER
# ================================

@app.route("/diet", methods=["GET", "POST"])
def diet():

    result = None
    diet_plan = None
    error = None

    if request.method == "POST":
        try:
            age = int(request.form["age"])
            height = float(request.form["height"])
            weight = float(request.form["weight"])
            gender = request.form["gender"]
            activity = request.form["activity"]
            goal = request.form["goal"]

            if age <= 0:
                raise ValueError("Age must be greater than zero.")
            if goal not in {"loss", "maintain", "gain"}:
                raise ValueError("Goal must be loss, maintain, or gain.")

            bmi = weight / ((height / 100) ** 2)
            bmr = calculate_bmr(weight, height, age, gender)
            calories = calculate_tdee(bmr, activity)

            if goal == "loss":
                calories -= 500
            elif goal == "gain":
                calories += 500

            result = f"BMI: {bmi:.2f} | Recommended Calories: {int(calories)} kcal"

            eligible_foods = df[df["category"].ne("Junk")].copy()
            if goal == "gain":
                eligible_foods = eligible_foods.sort_values(
                    ["calories", "protein"], ascending=False
                )
            elif goal == "loss":
                eligible_foods = eligible_foods.sort_values(
                    ["protein", "fiber", "calories"], ascending=[False, False, True]
                )
            else:
                eligible_foods = eligible_foods.sort_values(
                    ["protein", "carbohydrates"], ascending=False
                )

            foods = eligible_foods[food_col].head(12).tolist()
            if len(foods) < 12:
                raise ValueError("Not enough suitable foods are available.")

            diet_plan = f"""
Breakfast: {foods[0]}, {foods[1]}, {foods[2]}

Lunch: {foods[3]}, {foods[4]}, {foods[5]}

Dinner: {foods[6]}, {foods[7]}, {foods[8]}

Snacks: {foods[9]}, {foods[10]}, {foods[11]}
"""
        except (KeyError, TypeError, ValueError, ZeroDivisionError) as exc:
            error = str(exc)

    return render_template(
        "diet.html",
        result=result,
        diet_plan=diet_plan,
        error=error
    )


# ================================
# RUN SERVER
# ================================

if __name__ == "__main__":
    app.run(debug=True)