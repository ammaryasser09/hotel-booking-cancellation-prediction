# 🏨 Hotel Booking AI

### Intelligent Hotel Booking Analysis & Cancellation Prediction Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-FF6600)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly)

> **Hotel Booking AI** is an end-to-end Machine Learning and Data Analytics platform designed to analyze hotel booking behavior, identify cancellation patterns, explore pricing and customer segments, and provide business-oriented insights through an interactive Streamlit dashboard.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Business Problem](#-business-problem)
* [Project Objectives](#-project-objectives)
* [Dataset](#-dataset)
* [Key Features](#-key-features)
* [Exploratory Data Analysis](#-exploratory-data-analysis)
* [Data Preprocessing](#-data-preprocessing)
* [Feature Engineering](#-feature-engineering)
* [Machine Learning](#-machine-learning)
* [Model Evaluation](#-model-evaluation)
* [Dashboard](#-dashboard)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [How to Run](#-how-to-run)
* [Technologies](#-technologies)
* [Business Insights](#-business-insights)
* [Future Improvements](#-future-improvements)
* [Author](#-author)

---

## 🔎 Overview

The hotel industry deals with a large number of reservations every day. One of the major challenges is **booking cancellation**, which can negatively affect occupancy, revenue forecasting, and operational planning.

This project uses historical hotel booking data to:

* Analyze customer booking behavior.
* Identify the main factors associated with cancellations.
* Understand pricing and ADR patterns.
* Analyze booking lead time.
* Explore market and distribution segments.
* Detect potential outliers.
* Study relationships between numerical features.
* Train Machine Learning models to predict booking cancellations.
* Present analytical results through an interactive dashboard.

The final application combines **Data Analysis, Data Visualization, Machine Learning, and Business Intelligence** in one platform.

---

## 💼 Business Problem

Hotel cancellations can lead to:

* Empty rooms.
* Revenue loss.
* Poor occupancy forecasting.
* Inefficient resource planning.
* Difficulty predicting future demand.

The goal of this project is to transform historical booking data into actionable insights and build a predictive model that can help hotels better understand and manage cancellation risk.

---

## 🎯 Project Objectives

The project focuses on the following objectives:

1. Understand the structure and quality of hotel booking data.
2. Clean and preprocess the dataset.
3. Analyze numerical and categorical variables.
4. Identify important cancellation patterns.
5. Analyze customer and market segments.
6. Study ADR and pricing behavior.
7. Engineer useful features for Machine Learning.
8. Handle class imbalance.
9. Train and compare multiple Machine Learning algorithms.
10. Select a strong predictive model.
11. Build an interactive analytics dashboard.
12. Generate automated business insights.

---

## 📊 Dataset

The project uses the **Hotel Booking Demand Dataset**, containing approximately:

**119,390 booking records**

The dataset includes information related to:

* Hotel type
* Reservation status
* Lead time
* Arrival date
* Number of guests
* Market segment
* Distribution channel
* Customer type
* Deposit type
* Room type
* Previous cancellations
* Booking changes
* ADR
* Country
* Agent
* Company

### Target Variable

The main prediction target is:

```text
is_canceled
```

Where:

```text
0 → Booking was not canceled
1 → Booking was canceled
```

---

## ✨ Key Features

### 📈 Exploratory Data Analysis

The platform provides analysis of:

* Booking distributions
* Cancellation behavior
* Lead-time patterns
* ADR distribution
* Market segments
* Customer types
* Hotel types
* Distribution channels
* Guest behavior
* Outliers
* Feature correlations

### 🧠 Machine Learning

Several Machine Learning algorithms were evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Classifier
* K-Nearest Neighbors
* Gaussian Naive Bayes
* XGBoost

### 📊 Interactive Dashboard

The Streamlit dashboard provides:

* KPI cards
* Interactive filters
* Data visualizations
* Booking analysis
* Cancellation analysis
* Pricing analysis
* Guest loyalty analysis
* Correlation analysis
* Automated business insights

---

# 🔬 Exploratory Data Analysis

The EDA stage was used to understand the dataset before applying Machine Learning.

### Numerical Analysis

Important numerical variables include:

* `lead_time`
* `adults`
* `children`
* `babies`
* `stays_in_weekend_nights`
* `stays_in_week_nights`
* `booking_changes`
* `days_in_waiting_list`
* `adr`

Visualizations include:

* Histograms
* Box plots
* Distribution plots
* Bar charts
* Correlation heatmaps

### Categorical Analysis

Important categorical variables include:

* `hotel`
* `meal`
* `country`
* `market_segment`
* `distribution_channel`
* `reserved_room_type`
* `deposit_type`
* `customer_type`

---

# 🧹 Data Preprocessing

The preprocessing pipeline includes:

### Missing Values

Missing values were analyzed and handled according to the nature of each feature.

For numerical features:

```python
SimpleImputer(strategy="median")
```

For categorical features:

```python
SimpleImputer(strategy="most_frequent")
```

### Encoding

Categorical features were transformed using:

```python
OneHotEncoder(handle_unknown="ignore")
```

### Feature Transformation

A `ColumnTransformer` was used to apply different preprocessing operations to numerical and categorical features.

---

# ⚙️ Feature Engineering

Several features were created to improve the analysis and Machine Learning process.

Examples include:

### Lead Time Groups

Bookings were grouped into:

```text
0–30 days
31–60 days
61–120 days
121–180 days
180+ days
```

This helped analyze how cancellation behavior changes depending on how early the booking was made.

### Date-Based Features

Additional temporal features can be extracted from arrival dates, such as:

* Arrival year
* Arrival month
* Arrival period

---

# ⚖️ Class Imbalance

The target variable is not perfectly balanced.

Approximate distribution:

```text
Not Cancelled → 72.51%
Cancelled     → 27.49%
```

To address this issue, techniques such as:

```python
class_weight="balanced"
```

and **SMOTE** were considered/used during model development.

This helps prevent the model from becoming overly biased toward the majority class.

---

# 🤖 Machine Learning

The following models were evaluated:

| Model                | Purpose                       |
| -------------------- | ----------------------------- |
| Logistic Regression  | Linear baseline               |
| Decision Tree        | Rule-based classification     |
| Random Forest        | Ensemble learning             |
| SVC                  | Margin-based classification   |
| KNN                  | Distance-based classification |
| Gaussian Naive Bayes | Probabilistic baseline        |
| XGBoost              | Advanced gradient boosting    |

---

# 🚀 XGBoost

XGBoost was selected as the main advanced Machine Learning approach because it is highly effective for structured/tabular datasets.

The final pipeline includes preprocessing and the trained XGBoost model.

Example:

```python
joblib.dump(
    final_model,
    "hotel_booking_xgboost_pipeline.pkl"
)
```

The saved pipeline can later be loaded for prediction without manually repeating the preprocessing steps.

---

# 📏 Model Evaluation

The models were evaluated using several metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

### Example Results

| Model               |       Train Accuracy |        Test Accuracy |
| ------------------- | -------------------: | -------------------: |
| Logistic Regression |               77.35% |               77.09% |
| Decision Tree       |               78.81% |               77.44% |
| XGBoost             | Final selected model | Final selected model |

> The final model selection should consider more than accuracy alone, especially because cancellation prediction is a classification problem with class imbalance.

---

# 📊 Streamlit Dashboard

The project includes an interactive web dashboard built with **Streamlit**.

The dashboard is designed to transform technical Machine Learning results into understandable business insights.

### Dashboard Sections

#### 🏠 Overview

Provides a high-level summary of:

* Total bookings
* Cancellation rate
* Average ADR
* Average lead time

#### 📊 Booking Behavior

Analyzes:

* Booking patterns
* Hotel distribution
* Market segments
* Customer types

#### ❌ Cancellation Drivers

Explores factors associated with cancellation behavior.

#### ⏱️ Lead Time Analysis

Analyzes how cancellation rates change as the booking lead time increases.

#### 💰 ADR & Pricing

Analyzes:

* Average Daily Rate
* Pricing distributions
* Pricing outliers
* Segment-level ADR

#### 📦 Distribution & Outlier Analysis

Examines booking channels and unusual observations.

#### 🔗 Feature Correlation

Provides correlation analysis between numerical variables.

#### 👤 Guest Loyalty

Analyzes repeated guests and customer behavior.

#### 🧠 Automated Business Insights

Generates business-oriented conclusions from the analyzed data.

---

# 💡 Business Insights

Some important findings from the analysis include:

### ⚠️ Cancellation Risk

The dataset contains a significant percentage of canceled reservations, making cancellation prediction an important business problem.

### ⏱️ Lead Time

Longer booking lead times are associated with higher cancellation rates.

Example analysis:

```text
0–30 days       → 16.42%
31–60 days      → 31.62%
61–120 days     → 33.54%
121–180 days    → 35.09%
180+ days       → 39.74%
```

This suggests that reservations made far in advance may require additional retention strategies.

### 🎯 Market Segment

Online Travel Agencies represent a major portion of the booking volume.

### 🏨 Hotel Distribution

City Hotel represents a large share of the booking activity in the dataset.

---

# 🗂️ Project Structure

```text
Hotel-Booking-AI/
│
├── app.py
│
├── pages/
│   ├── analysis.py
│   ├── prediction.py
│   └── ...
│
├── data/
│   └── hotel_bookings.csv
│
├── models/
│   └── hotel_booking_xgboost_pipeline.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   └── ML_Modeling.ipynb
│
├── assets/
│   ├── images/
│   └── styles/
│
├── requirements.txt
│
└── README.md
```

> Adjust the structure above to match the actual folders and files in your repository.

---

# 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/ammaryasser09/Hotel-Booking-AI.git
```

Navigate to the project:

```bash
cd Hotel-Booking-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📦 Main Dependencies

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
Plotly
Scikit-learn
XGBoost
Imbalanced-learn
Joblib
Streamlit
```

---

# 🧰 Technologies

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-learn
* XGBoost
* Imbalanced-learn

### Application

* Streamlit

### Model Persistence

* Joblib

### Version Control

* Git
* GitHub

---

# 🔮 Future Improvements

Future versions of the project may include:

* Real-time hotel booking prediction.
* Advanced cancellation risk scoring.
* Dynamic revenue forecasting.
* Customer segmentation using clustering.
* Recommendation systems.
* Explainable AI using SHAP.
* Real-time database integration.
* Authentication and user management.
* Cloud deployment.
* REST API using FastAPI.
* Advanced AI-generated business recommendations.
* Multilingual dashboard support.

---

# 🎯 Project Workflow

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Feature Engineering
     │
     ▼
Data Preprocessing
     │
     ▼
Class Imbalance Handling
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
XGBoost Pipeline
     │
     ▼
Streamlit Dashboard
     │
     ▼
Business Insights
```

---

# 📸 Screenshots

Add screenshots of the application here:

```text
screenshots/
├── dashboard.png
├── analysis.png
├── cancellation.png
├── pricing.png
└── prediction.png
```

Example:

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

# 👨‍💻 Author

### Ammar Yasser Zaki

Artificial Intelligence Student
Egyptian Russian University

**GitHub:** `ammaryasser09`

---

# 👨‍🏫 Supervisor

### Eng. Mohab Allam

---

# ⭐ Project Highlights

* End-to-end Machine Learning project
* Real-world hotel booking dataset
* Comprehensive EDA
* Feature engineering
* Class imbalance handling
* Multiple Machine Learning algorithms
* XGBoost classification
* Interactive Streamlit dashboard
* Automated business insights
* Production-oriented ML pipeline

---

# 📄 License

This project is developed for educational and portfolio purposes.

---

## ⭐ If you find this project useful

Feel free to ⭐ the repository and explore the project.
