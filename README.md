## Diet Monitoring System

This project provides a Flask web application and a command-line application for food category identification, calorie calculation, and goal-based diet recommendations.

### Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The trained model files are stored in `models/`. To rebuild them after changing the dataset, run `python build_dataset.py` and then `python train_food_model.py`.

### Run the web application

```powershell
python web_app/app.py
```

Open http://127.0.0.1:5000.

### Run the command-line application

```powershell
python main_system.py
```