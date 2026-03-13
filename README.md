# 💻 Laptop Market Analysis & Price Prediction

An end-to-end **Data Analysis and Machine Learning project** that explores the laptop market, identifies key factors affecting laptop prices, and builds a machine learning model to predict laptop prices.

The project includes:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- Interactive Python Dashboard
- Tableau Business Dashboards

---

# 📊 Project Objectives

The goal of this project is to:

- Understand laptop market trends
- Analyze factors influencing laptop prices
- Build a predictive machine learning model
- Visualize insights using professional dashboards
- Deliver business insights for hardware and pricing strategy

---

# 📁 Project Structure


Laptop_Price_Analysis_ML/
│
├── app/
│   └── app.py
│
├── data/
│   ├── laptop_prices.csv
│   └── laptop_cleaned.csv
│
├── Notebook/
│   ├── 01_EDA.ipynb
│   └── 02_ML.ipynb
│
├── output/
│   ├── Actual_vs_Predicted.png
│   ├── Brand_vs_Price.png
│   ├── correlation_analysis.png
│   ├── CPU_vs_Price.png
│   ├── Feature_importance.png
│   ├── laptop_price_model.pkl
│   ├── Laptop_vs_Price.png
│   ├── Market_structure.png
│   ├── missing_value.png
│   ├── Model_comparison.png
│   ├── OS_vs_price.png
│   ├── price_distribution_analysis.png
│   ├── price_distribution_detection.png
│   ├── RAM_vs_Price.png
│   ├── Residual_error_pro.png
│   ├── storage_vs_Price.png
│   └── weight_vs_price.png
│
├── Tableau_Dashboard/
│   ├── Overview.png
│   ├── Hardware_Analysis.png
│   └── Price_Insights.png
│
├── requirements.txt
├── .gitignore
└── README.md


---

# 🔍 Exploratory Data Analysis (EDA)

## Dataset Exploration

The EDA phase explores the structure of the dataset and identifies patterns affecting laptop prices.

## Key Analyses Performed

### Price Distribution
Understanding the distribution of laptop prices across the dataset.

### Brand vs Price
Analyzing how laptop manufacturers influence pricing.

### RAM vs Price
Higher RAM configurations generally correspond to higher laptop prices.

### CPU Frequency vs Price
Examines the relationship between processor speed and pricing.

### Storage Type vs Price
Comparing SSD, HDD, Hybrid, and Flash storage impact on laptop prices.

### OS vs Price
Understanding how operating systems influence price ranges.

### Missing Value Analysis
Heatmap visualization used to confirm data completeness.

### Correlation Analysis
Identifying relationships between numerical features such as:

- RAM
- CPU Frequency
- Screen Resolution (PPI)
- Storage Capacity
- Weight

---

# ⚙ Feature Engineering

## New Features Created

New features were engineered to improve model performance.

### Pixels Per Inch (PPI)

Calculated from screen resolution and screen size.

```python
ppi = sqrt(ScreenW**2 + ScreenH**2) / Inches
```

### Binary Encoding

Converted categorical features into numerical form.

#### Features Encoded

- Touchscreen
- IPS Panel
- Retina Display

#### Encoding Method

- Yes → 1
- No → 0

---

# 🤖 Machine Learning Pipeline

## Model Training

The machine learning pipeline predicts laptop prices using engineered features.

### Models Trained

| Model | Description |
|------|-------------|
| Linear Regression | Baseline regression model |
| Random Forest | Ensemble tree-based model |
| XGBoost | Gradient boosting model |

---

# 📈 Model Evaluation

## Evaluation Metrics

Model performance was evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

## Best Performing Model

The **XGBoost model** achieved the best performance with the highest R² score and lowest prediction error.

---

# 📊 Model Diagnostics

Several evaluation visualizations were generated.

### Actual vs Predicted
Compares predicted laptop prices with actual prices.

### Residual Error Analysis
Helps identify prediction errors and model bias.

### Feature Importance
Highlights the most influential features affecting laptop prices.

### Top Influential Features

- RAM
- CPU Frequency
- PPI
- Storage Type
- GPU Brand

---

# 📊 Tableau Business Dashboards

Interactive dashboards were created to provide business insights.

## 1️⃣ Overview Dashboard

### KPI Metrics

- Total Laptops
- Average Price
- Average RAM
- Average Weight

### Visualizations

- Laptop Price Distribution
- RAM vs Price
- Laptop Type Distribution
- Brand vs Price

---

## 2️⃣ Hardware Analysis Dashboard

Analyzes hardware specifications affecting laptop prices.

### Visualizations

- Screen Resolution vs Price
- Storage Type vs Price
- CPU Frequency vs Price

### Insight

Higher hardware specifications generally correspond to higher laptop prices.

---

## 3️⃣ Price Insights Dashboard

Business-focused pricing analysis.

### Visualizations

- GPU Brand vs Price
- Weight vs Price
- OS vs Price

### Key Insights

- macOS laptops tend to be premium priced
- SSD storage significantly increases laptop price
- Gaming laptops with powerful GPUs are higher priced

---

# 🖥 Python Dashboard

## Streamlit Dashboard

A **Streamlit dashboard** was developed for interactive laptop price prediction.

### Features

- Market statistics
- Interactive charts
- Laptop price prediction tool

Users can input laptop specifications and obtain estimated price predictions.

---

# 🛠 Technologies Used

## Programming

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Streamlit
- Plotly

## Visualization

- Tableau
- Python Dashboards

---

# 📈 Business Insights

Key insights derived from the analysis:

- RAM strongly influences laptop pricing
- High resolution displays increase price
- SSD storage laptops are more expensive
- Gaming laptops fall into higher price segments
- GPU brand significantly impacts laptop pricing

---

# 🚀 Future Improvements

Potential enhancements include:

- Hyperparameter tuning
- Deep learning price prediction
- Time-series laptop market analysis
- Deployment as a full web application

---

# ⚙ Installation

## Clone the repository

git clone https://github.com/yourusername/Laptop_Price_Analysis_ML.git

## Navigate to the project directory

cd Laptop_Price_Analysis_ML

## Install dependencies

pip install -r requirements.txt

## Run the Streamlit dashboard

streamlit run app/app.py


---

# 👨‍💻 Author

**Aparna Patel**
