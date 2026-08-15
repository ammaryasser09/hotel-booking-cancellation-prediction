# 🏨 Hotel Booking AI

### Intelligent Hotel Booking Analysis & Cancellation Prediction Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-FF6600)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly)

> **Hotel Booking AI** is an end-to-end Machine Learning and Data Analytics platform built to analyze hotel booking behavior, identify cancellation patterns, explore customer and market segments, analyze pricing and lead-time behavior, and provide business-oriented insights through an interactive Streamlit application.

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
* [Class Imbalance](#-class-imbalance)
* [Machine Learning](#-machine-learning)
* [Model Evaluation](#-model-evaluation)
* [Streamlit Application](#-streamlit-application)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [How to Run](#-how-to-run)
* [Technologies](#-technologies)
* [Business Insights](#-business-insights)
* [Future Improvements](#-future-improvements)
* [Author](#-author)
* [Supervisor](#-supervisor)

---

# 🔎 Overview

The hotel industry processes a large number of reservations every day. One of the major challenges is **booking cancellation**, which can negatively affect occupancy, revenue forecasting, demand planning, and hotel operations.

**Hotel Booking AI** transforms historical hotel reservation data into meaningful analytical insights and Machine Learning predictions.

The platform focuses on:

* Understanding hotel booking behavior.
* Identifying cancellation patterns.
* Analyzing booking lead time.
* Studying ADR and pricing behavior.
* Exploring market segments.
* Analyzing distribution channels.
* Understanding customer loyalty.
* Detecting outliers.
* Studying numerical feature correlations.
* Training Machine Learning classification models.
* Predicting booking cancellation risk.
* Presenting results through an interactive Streamlit dashboard.

The project combines:

**Data Analysis + Data Visualization + Machine Learning + Business Intelligence**

into one unified platform.

---

# 💼 Business Problem

Hotel cancellations can create several business challenges:

* Empty rooms.
* Revenue loss.
* Uncertain occupancy.
* Poor demand forecasting.
* Inefficient resource planning.
* Difficulty identifying high-risk reservations.
* Challenges in pricing and inventory management.

The goal of this project is to analyze historical booking data and build a predictive system that helps identify cancellation risk and provides useful business insights.

---

# 🎯 Project Objectives

The main objectives of the project are:

1. Understand the structure and quality of hotel booking data.
2. Clean and preprocess the dataset.
3. Analyze numerical and categorical variables.
4. Explore booking distributions.
5. Identify cancellation patterns.
6. Analyze customer and market segments.
7. Study ADR and pricing behavior.
8. Analyze booking lead time.
9. Detect and investigate outliers.
10. Engineer useful Machine Learning features.
11. Handle class imbalance.
12. Train multiple Machine Learning algorithms.
13. Evaluate model performance using multiple metrics.
14. Select an effective predictive approach.
15. Build an interactive Streamlit dashboard.
16. Generate automated business-oriented insights.

---

# 📊 Dataset

The project uses the **Hotel Booking Demand Dataset**.

The dataset contains approximately:

**119,390 booking records**

and includes information about hotel reservations, customers, pricing, distribution channels, market segments, and cancellation behavior.

### Main Features

Important columns include:

* `hotel`
* `is_canceled`
* `lead_time`
* `arrival_date_year`
* `arrival_date_month`
* `stays_in_weekend_nights`
* `stays_in_week_nights`
* `adults`
* `children`
* `babies`
* `meal`
* `country`
* `market_segment`
* `distribution_channel`
* `is_repeated_guest`
* `previous_cancellations`
* `reserved_room_type`
* `booking_changes`
* `deposit_type`
* `agent`
* `company`
* `days_in_waiting_list`
* `customer_type`
* `adr`

---

## 🎯 Target Variable

The main Machine Learning target is:

```text
is_canceled
```

Where:

```text
0 → Booking was not canceled
1 → Booking was canceled
```

The cancellation rate in the original hotel booking dataset is approximately **37%**.

---

# ✨ Key Features

## 📈 Exploratory Data Analysis

The application provides analysis of:

* Booking distributions.
* Cancellation behavior.
* Lead-time patterns.
* ADR distribution.
* Market segments.
* Customer types.
* Hotel types.
* Distribution channels.
* Guest behavior.
* Outliers.
* Feature correlations.
* Customer loyalty.

---

## 🤖 Machine Learning

Multiple Machine Learning algorithms were evaluated during model development:

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Classifier
* K-Nearest Neighbors
* Gaussian Naive Bayes
* XGBoost

The final application uses an **XGBoost pipeline** for the prediction component.

---

## 📊 Interactive Dashboard

The Streamlit application provides:

* KPI cards.
* Interactive navigation.
* Booking analysis.
* Cancellation analysis.
* Lead-time analysis.
* ADR and pricing analysis.
* Distribution analysis.
* Outlier analysis.
* Correlation analysis.
* Guest loyalty analysis.
* Automated business insights.
* Machine Learning prediction.

---

# 🔬 Exploratory Data Analysis

The EDA stage was performed to understand the dataset before Machine Learning.

## Numerical Analysis

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

Visualization techniques include:

* Histograms.
* Box plots.
* Bar charts.
* Distribution analysis.
* Correlation heatmaps.

---

## Categorical Analysis

Important categorical variables include:

* `hotel`
* `meal`
* `country`
* `market_segment`
* `distribution_channel`
* `reserved_room_type`
* `deposit_type`
* `customer_type`

These features were analyzed to understand differences between booking groups and cancellation behavior.

---

# 🧹 Data Preprocessing

The Machine Learning preprocessing pipeline includes several stages.

## Missing Values

Missing values were analyzed according to feature type.

### Numerical Features

Median imputation was used:

```python
SimpleImputer(strategy="median")
```

### Categorical Features

Most-frequent imputation was used:

```python
SimpleImputer(strategy="most_frequent")
```

---

## 🔤 Categorical Encoding

Categorical variables were transformed using:

```python
OneHotEncoder(handle_unknown="ignore")
```

This allows categorical features to be converted into numerical representations suitable for Machine Learning models.

---

## 🔧 ColumnTransformer

A `ColumnTransformer` was used to apply different preprocessing operations to numerical and categorical features within the Machine Learning pipeline.

This makes the preprocessing process consistent between training and prediction.

---

# ⚙️ Feature Engineering

Feature engineering was used to create more meaningful representations of the booking data.

## ⏱️ Lead Time Groups

Bookings were grouped according to their lead time:

```text
0–30 days
31–60 days
61–120 days
121–180 days
180+ days
```

This allows cancellation behavior to be analyzed according to how far in advance a reservation was made.

---

## 📅 Date Features

Arrival information can also be analyzed using temporal features such as:

* Arrival year.
* Arrival month.
* Arrival period.

These features help identify seasonal and yearly booking patterns.

---

# ⚖️ Class Imbalance

The target variable is imbalanced because the number of non-canceled bookings is larger than the number of canceled bookings.

The dataset contains approximately:

```text
Not Canceled → 63%
Canceled     → 37%
```

Class imbalance was considered during Machine Learning development.

Techniques such as:

```python
class_weight="balanced"
```

and **SMOTE** were used/considered during model experimentation.

This helps reduce the tendency of classification models to favor the majority class.

---

# 🤖 Machine Learning

Several classification algorithms were evaluated.

| Model                | Description                      |
| -------------------- | -------------------------------- |
| Logistic Regression  | Linear classification baseline   |
| Decision Tree        | Rule-based classification        |
| Random Forest        | Ensemble learning                |
| SVC                  | Margin-based classification      |
| KNN                  | Distance-based classification    |
| Gaussian Naive Bayes | Probabilistic classification     |
| XGBoost              | Gradient boosting classification |

---

# 🚀 XGBoost

**XGBoost** was selected as the main advanced Machine Learning approach because it performs well on structured and tabular datasets.

The project contains a saved XGBoost Machine Learning pipeline:

```text
hotel_booking_xgboost_pipeline.pkl
```

The saved pipeline contains the preprocessing and trained prediction workflow required for inference.

The model can be loaded using:

```python
import joblib

model = joblib.load(
    "hotel_booking_xgboost_pipeline.pkl"
)
```

This allows new booking information to pass through the same preprocessing and prediction pipeline used during model development.

---

# 📏 Model Evaluation

The Machine Learning models were evaluated using several metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

### Development Results

| Model               |       Train Accuracy |        Test Accuracy |
| ------------------- | -------------------: | -------------------: |
| Logistic Regression |               77.35% |               77.09% |
| Decision Tree       |               78.81% |               77.44% |
| XGBoost             | Final Selected Model | Final Selected Model |

> Model selection should not rely on accuracy alone. Precision, recall, F1-score, and ROC-AUC are also important when evaluating cancellation prediction because the target variable is imbalanced.

---

# 📊 Streamlit Application

The project includes an interactive web application built using **Streamlit**.

The application is organized into multiple pages.

## 🏠 Home

The Home page provides:

* Project introduction.
* Project overview.
* Dataset statistics.
* System capabilities.
* Machine Learning workflow.
* XGBoost information.
* Project architecture.

---

## 📊 Analysis

The Analysis page focuses on Exploratory Data Analysis and provides:

* Analysis filters.
* Booking KPIs.
* Booking behavior analysis.
* Cancellation drivers.
* Lead-time analysis.
* ADR and pricing analysis.
* Distribution analysis.
* Outlier analysis.
* Feature correlation.
* Guest loyalty.
* Automated business insights.

---

## 📈 Dashboard

The Dashboard page provides an interactive overview of the main hotel booking KPIs and analytical visualizations.

It is designed to make the results easier to understand from a business perspective.

---

## 🤖 Prediction

The Prediction page uses the trained XGBoost pipeline to estimate whether a hotel reservation is likely to be canceled.

The prediction workflow is based on the same preprocessing pipeline used during model development.

---

## ℹ️ About

The About page provides information about:

* The project.
* Technologies used.
* Machine Learning approach.
* Project purpose.
* Author.
* Supervisor.

---

# 🗂️ Project Structure

The actual repository structure is:

```text
hotel-booking-cancellation-prediction/
│
├── .streamlit/
│   └── config.toml
│
├── pages/
│   ├── About.py
│   ├── Analysis.py
│   ├── Dashboard.py
│   └── Prediction.py
│
├── Home.py
│
├── navigation.py
│
├── hotel_bookings.csv
│
├── hotel_booking_xgboost_pipeline.pkl
│
├── project machine learning.ipynb
│
├── README.md
│
└── requirements.txt
```

### Main Files

**`Home.py`**

Main entry point of the Streamlit application.

**`navigation.py`**

Handles the application's navigation system.

**`pages/Analysis.py`**

Contains the Exploratory Data Analysis interface.

**`pages/Dashboard.py`**

Contains the main analytical dashboard.

**`pages/Prediction.py`**

Contains the Machine Learning prediction interface.

**`pages/About.py`**

Contains project and author information.

**`hotel_bookings.csv`**

The main hotel booking dataset.

**`hotel_booking_xgboost_pipeline.pkl`**

Saved XGBoost prediction pipeline.

**`project machine learning.ipynb`**

Notebook containing the data analysis and Machine Learning development workflow.

**`requirements.txt`**

Contains the Python dependencies required to run the project.

---

# 🛠️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ammaryasser09/hotel-booking-cancellation-prediction.git
```

## 2. Navigate to the Project

```bash
cd hotel-booking-cancellation-prediction
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Start the Streamlit application using:

```bash
streamlit run Home.py
```

After running the command, Streamlit will provide a local URL where the application can be accessed.

Usually:

```text
http://localhost:8501
```

---

# 📦 Main Dependencies

The project uses technologies including:

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

The complete dependency list is available in:

```text
requirements.txt
```

---

# 🧰 Technologies

## Programming

* Python

## Data Analysis

* Pandas
* NumPy

## Data Visualization

* Matplotlib
* Seaborn
* Plotly

## Machine Learning

* Scikit-learn
* XGBoost
* Imbalanced-learn

## Application

* Streamlit

## Model Persistence

* Joblib

## Version Control

* Git
* GitHub

---

# 💡 Business Insights

The analysis produced several meaningful observations.

## ⚠️ Cancellation Behavior

Hotel booking cancellation represents a significant business challenge and requires careful monitoring because cancellations can affect occupancy and revenue planning.

---

## ⏱️ Lead Time and Cancellation

Cancellation rates tend to increase as booking lead time increases.

Example analysis:

```text
0–30 days       → 16.42%
31–60 days      → 31.62%
61–120 days     → 33.54%
121–180 days    → 35.09%
180+ days       → 39.74%
```

This suggests that reservations made significantly in advance may require additional monitoring and retention strategies.

---

## 🎯 Market Segment

Online Travel Agencies represent one of the dominant market segments in the dataset.

This highlights the importance of understanding third-party booking channels when analyzing cancellation behavior.

---

## 🏨 Hotel Type

City Hotel represents a large share of the booking activity within the dataset.

Comparing City Hotel and Resort Hotel behavior can provide additional insight into booking patterns and cancellation risk.

---

# 🔮 Future Improvements

Potential future improvements include:

* Real-time cancellation risk scoring.
* Advanced revenue forecasting.
* Customer segmentation using clustering.
* Customer lifetime value analysis.
* Recommendation systems.
* Explainable AI using SHAP.
* Real-time database integration.
* Authentication and user management.
* Cloud deployment.
* REST API using FastAPI.
* AI-generated business recommendations.
* Multilingual dashboard support.
* Real-time hotel data integration.

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
                Streamlit Platform
                         │
                         ▼
               Business Insights
```

---

# 📸 Application Preview

The application contains several main interfaces:

```text
Home
   │
   ├── Analysis
   │
   ├── Dashboard
   │
   ├── Prediction
   │
   └── About
```

Screenshots can be added later under a dedicated `screenshots/` folder.

---

# 👨‍💻 Author

## Ammar Yasser Zaki

Artificial Intelligence Student
Egyptian Russian University

GitHub:

[@ammaryasser09](https://github.com/ammaryasser09?utm_source=chatgpt.com)

---

# 👨‍🏫 Supervisor

## Eng. Mohab Allam

---

# ⭐ Project Highlights

* End-to-end Machine Learning project.
* Real-world hotel booking dataset.
* Comprehensive Exploratory Data Analysis.
* Numerical and categorical feature analysis.
* Feature engineering.
* Missing-value handling.
* Class imbalance handling.
* Multiple Machine Learning algorithms.
* XGBoost classification.
* Saved Machine Learning pipeline.
* Interactive Streamlit application.
* Interactive dashboard.
* Cancellation analysis.
* Lead-time analysis.
* ADR and pricing analysis.
* Guest loyalty analysis.
* Correlation analysis.
* Automated business insights.
* GitHub-ready project structure.

---

# 📄 License

This project was developed for educational, academic, and portfolio purposes.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Repository:

[Hotel Booking Cancellation Prediction](https://github.com/ammaryasser09/hotel-booking-cancellation-prediction?utm_source=chatgpt.com)
