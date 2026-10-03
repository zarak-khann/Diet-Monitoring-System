def calculate_bmi(weight, height_cm):
    if weight <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be greater than zero.")
    height_m = height_cm / 100
    return weight / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_bmr(weight, height_cm, age, gender):
    if weight <= 0 or height_cm <= 0 or age <= 0:
        raise ValueError("Age, weight, and height must be greater than zero.")
    if gender.lower() == "male":
        return (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
    if gender.lower() == "female":
        return (10 * weight) + (6.25 * height_cm) - (5 * age) - 161
    raise ValueError("Gender must be male or female.")


def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725
    }
    try:
        return bmr * activity_multipliers[activity_level.lower()]
    except (AttributeError, KeyError):
        raise ValueError(
            "Activity level must be sedentary, light, moderate, or active."
        ) from None


def adjust_calories(tdee, goal):
    if goal == "loss":
        return tdee - 300
    elif goal == "gain":
        return tdee + 400
    else:
        return tdee