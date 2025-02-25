
# Road-Accident-Predictions-and-Traffic-Severity-Analysis

![Screenshot (205)](https://github.com/user-attachments/assets/b6b5e928-737d-4024-b0ee-47db2f32861a)



### 🚗 Overview
Road accidents are a significant concern worldwide, leading to loss of life, property damage, and traffic disruptions. This project aims to leverage data science techniques to predict road accidents and analyze traffic severity. By understanding patterns and key influencing factors, we can contribute to smarter traffic management and safer roads.

### 📌 Objectives
1. Predict Accident Likelihood: Utilize machine learning models to forecast road accidents based on historical and real-time data.
2. Analyze Traffic Severity: Understand the factors contributing to traffic severity during accidents.
3. Data Visualization: Present insights using interactive visualizations for better decision-making.

### 🔧 Features
1. Data Preprocessing: Clean and preprocess accident and traffic datasets.
2. Feature Engineering: Extract critical features such as weather conditions, road type, time of day, etc.
3. Prediction Models: Train and evaluate machine learning models to predict accident likelihood.
4. Severity Analysis: Identify high-severity zones and influencing factors.
5. Visualization Dashboards: Create dashboards to explore trends and patterns.

### 📂 Project Structure
```bash
Road-Accident-Predictions-and-Traffic-Severity-Analysis/
│
├──artifacts
├── data/                     # Contains datasets (raw and processed)
│   ├── raw/
│   ├── processed/
│
├── notebooks/                # Jupyter notebooks for data exploration and model development
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│ 
│
├── source/
|    ├──components
│    │    ├──  __init__.py                  # Source code for the project
│    │    ├── preprocessing.py      # Scripts for data cleaning
│    │    ├── modeling.py           # Scripts for machine learning models
│    │    ├── analysis.py           # Scripts for severity analysis
│    ├── Pipeline
|    │    ├── __init__.py
│    │    ├── predict_pipeline.py
│    │    ├── train_pipeline.py
│    ├── __init__.py
│    ├──  exception.py
│    ├── logger.py
│    ├──  utils.py
├── templates
│       ├── home.html
├── venv                # Conda environment file (optional)
├── .gitignore
├── app.py
├── LICENSE                   # License information
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies 
├── setup.py                 
```

### 🚀 Getting Started
Prerequisites
Python 3.8+
Jupyter Notebook
Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, Plotly, Streamlit

```bash
Install dependencies:
pip install -r requirements.txt
```

### Running the Project
Clone the repository:
```bash
git clone https://github.com/yourusername/Road-Accident-Predictions-and-Traffic-Severity-Analysis.git
cd Road-Accident-Predictions-and-Traffic-Severity-Analysis
```
Process the data:
```bash
python src/preprocessing.py
```
Train the model:
```bash
python src/modeling.py
```
Launch the dashboard:
```bash
streamlit run dashboards/app.py
```

### 🛠️ Tools and Technologies
1. Data Preprocessing: Pandas, NumPy
2. Visualization: Matplotlib, Seaborn, Plotly
3. Machine Learning: Scikit-learn, XGBoost, LightGBM
4. Dashboarding: Streamlit

### 📊 Insights
1. Weather conditions and road types significantly impact accident severity.
2. Accidents are more likely during peak hours and bad weather.
3. High-severity zones can be visualized for targeted intervention.

### 📈 Results
1. Accuracy: 85% (or replace with your result)
2. Top Features: Weather, Road Type, Time of Day,

### 🧩 Future Scope
1. Incorporate real-time data for dynamic predictions.
2. Expand analysis to multiple cities or regions.
3. Develop a mobile application for real-time alerts.

### 👩‍💻 Author
Name - Aditya
LinkedIn: https://www.linkedin.com/in/aditya-akuskar-27b43533a/  

GitHub: https://github.com/Adity-star/























