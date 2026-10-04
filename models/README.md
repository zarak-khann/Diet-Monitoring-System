# Diet Monitoring System

A Python-based diet monitoring application that combines **food classification, calorie estimation, and goal-based diet recommendations** into a single system.

The project provides both a **command-line interface** and a **Flask web application**, with a machine-learning model used to classify food categories from nutritional information.

## Features

* 🍎 Food category identification using a trained Random Forest classifier
* 🔢 Calorie calculation based on food and serving mass
* 🥗 Goal-based diet recommendations
* 📊 Nutrition dataset processing
* 🤖 Machine-learning model training and evaluation
* 🌐 Flask-based web interface
* 💻 Command-line interface
* 💾 Saved model, scaler, and label-encoder artifacts
* 📁 Modular project structure for different system components

## How It Works

The system is divided into several main components:

```text
                    Diet Monitoring System
                            │
              ┌─────────────┴─────────────┐
              │                           │
        Command Line                  Flask Web App
              │                           │
              └─────────────┬─────────────┘
                            │
                    ┌───────┴────────┐
                    │                │
             Food Identifier   Calorie Calculator
                    │                │
                    └───────┬────────┘
                            │
                    Diet Recommender
                            │
                    Nutrition Dataset
                            │
                    ML Model / Artifacts
```

### Food Identification

The food classification component uses nutritional features such as:

* Calories
* Fat
* Protein
* Carbohydrates

These features are scaled before being passed to a **Random Forest classifier**. The target food category is encoded using a `LabelEncoder`.

The trained artifacts are:

```text
models/
├── food_model.pkl
├── scaler.pkl
└── label_encoder.pkl
```

### Calorie Calculator

The calorie calculator searches the nutrition dataset for a food item and estimates calories according to the entered serving mass.

It accepts:

```text
g
kg
```

and converts kilograms to grams before calculating the estimated calories.

The calculation is based on the food's caloric value per 100 grams.

### Diet Recommender

The system also includes a diet recommendation component that can be accessed through the main system menu.

### Interfaces

The project provides two ways to use the system:

**Command Line**

```text
python main_system.py
```

The CLI provides access to:

```text
1. Food Identifier
2. Calorie Calculator
3. Diet Recommender
```

**Web Application**

The Flask application can be started with:

```text
python web_app/app.py
```

The application runs locally at:

```text
http://127.0.0.1:5000
```

## Machine Learning Pipeline

The food-classification model follows this general workflow:

```text
Nutrition Dataset
       ↓
Data Preparation
       ↓
Feature Selection
       ↓
Label Encoding
       ↓
Train/Test Split
       ↓
Feature Scaling
       ↓
Random Forest Training
       ↓
Model Evaluation
       ↓
Save Model Artifacts
```

The current training script uses a Random Forest classifier with 100 estimators and a maximum depth of 10. The data is split using a stratified train/test split.

## Project Structure

```text
Diet-Monitoring-System/
│
├── data/
│   └── processed/
│       └── final_nutrition_dataset.csv
│
├── diet_recommender/
│   └── ...
│
├── models/
│   ├── food_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── src/
│   └── food_classifier/
│       └── predict.py
│
├── web_app/
│   └── app.py
│
├── build_dataset.py
├── calorie_calculator.py
├── main.py
├── main_system.py
├── train_food_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

* **Python**
* **Pandas** — dataset processing
* **Scikit-learn** — machine learning
* **Joblib** — saving and loading model artifacts
* **Flask** — web application
* **HTML/CSS** — web interface
* **CSV** — nutrition dataset

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/zarak-khann/Diet-Monitoring-System.git
cd Diet-Monitoring-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Command-Line Application

```bash
python main_system.py
```

Choose one of the available options:

```text
1. Food Identifier
2. Calorie Calculator
3. Diet Recommender
```

### Web Application

```bash
python web_app/app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Rebuilding the Dataset and Model

If the dataset is changed, the project includes scripts for rebuilding the processed dataset and retraining the food-classification model.

Build the dataset:

```bash
python build_dataset.py
```

Train the model:

```bash
python train_food_model.py
```

The training script saves the model artifacts inside the `models/` directory.

## Project Purpose

This project was developed as a practical implementation of concepts in:

* Python programming
* Data processing
* Machine learning
* Classification
* Feature scaling
* Model evaluation
* Dataset preparation
* Flask web development
* Modular application design

The goal is to combine these concepts into one practical diet-monitoring application rather than build a production-grade medical or nutritional system.

## Limitations

This project is intended for **educational and demonstration purposes**.

The calorie estimates and diet recommendations should not be treated as professional medical or nutritional advice.

Model predictions are dependent on the quality and coverage of the available dataset. Real-world food composition and individual nutritional requirements can vary.

## Future Improvements

Possible future improvements include:

* User accounts and personal profiles
* Persistent diet history
* Daily calorie tracking
* Improved food recognition
* Larger and more diverse datasets
* More advanced recommendation models
* Personalized meal planning
* Nutrition dashboards and visualizations
* Automated testing
* Containerized deployment
* Improved web UI/UX

## Author

**Zarak Khan**

GitHub: [zarak-khann](https://github.com/zarak-khann)

---

**Note:** This project is a learning-focused implementation of machine learning and software development concepts.
