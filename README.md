# 🛒 Shopper Spectrum: Customer Segmentation & Product Recommendation System

## 📌 Project Overview

Shopper Spectrum is an end-to-end E-Commerce Analytics project designed to analyze customer purchasing behavior, identify meaningful customer segments, and provide personalized product recommendations.

The project combines **RFM Analysis**, **K-Means Clustering**, and **Item-Based Collaborative Filtering** to help businesses better understand their customers and improve customer engagement through data-driven decision-making.

---

## 🎯 Problem Statement

E-commerce businesses generate massive amounts of transaction data every day. Analyzing this data can help organizations:

* Understand customer purchasing patterns
* Identify high-value customers
* Detect at-risk customers
* Deliver personalized product recommendations
* Improve marketing and retention strategies

This project aims to leverage transaction data to create actionable customer insights and recommendation systems.

---

## 🚀 Key Features

### 📊 Exploratory Data Analysis (EDA)

* Transaction analysis by country
* Top-selling products analysis
* Monthly sales trend analysis
* Revenue distribution analysis
* Customer purchasing behavior insights

### 👥 Customer Segmentation

* RFM (Recency, Frequency, Monetary) Analysis
* Data Standardization using StandardScaler
* K-Means Clustering
* Elbow Method for optimal cluster selection
* Silhouette Score evaluation
* Customer segment labeling

### 🎁 Product Recommendation System

* Item-Based Collaborative Filtering
* Customer-Product Interaction Matrix
* Cosine Similarity Calculation
* Top 5 Product Recommendations

### 📱 Interactive Streamlit Dashboard

* Home Dashboard
* EDA Dashboard
* RFM Analysis
* Product Recommendation Module
* Customer Segmentation Module
* Business Insights Page

---

## 🏗 Project Architecture

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
RFM Analysis
   ↓
K-Means Clustering
   ↓
Customer Segmentation
   ↓
Collaborative Filtering
   ↓
Product Recommendation
   ↓
Streamlit Dashboard
```

---

## 📂 Project Structure

```text
Shopper-Spectrum/
│
├── assets/
│   └── logo.png
│
├── data/
│   └── OnlineRetail.csv
│
├── models/
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── modules/
│   ├── home.py
│   ├── eda.py
│   ├── rfm_analysis.py
│   ├── recommendation.py
│   ├── segmentation.py
│   └── insights.py
│
├── utils/
│   ├── theme.py
│   └── data_loader.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Information

Dataset contains the following fields:

| Column      | Description                  |
| ----------- | ---------------------------- |
| InvoiceNo   | Transaction Number           |
| StockCode   | Product Code                 |
| Description | Product Description          |
| Quantity    | Quantity Purchased           |
| InvoiceDate | Date and Time of Transaction |
| UnitPrice   | Price Per Product            |
| CustomerID  | Unique Customer Identifier   |
| Country     | Customer Country             |

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

* Removed missing Customer IDs
* Removed cancelled invoices
* Removed negative quantities
* Removed zero or negative prices
* Removed duplicate records
* Created TotalAmount feature

```python
TotalAmount = Quantity × UnitPrice
```

---

## 📈 RFM Analysis

Customer behavior was analyzed using:

### Recency

Days since the customer's last purchase.

### Frequency

Number of unique transactions made by a customer.

### Monetary

Total amount spent by a customer.

---

## 🤖 Machine Learning Models

### Customer Segmentation

**Algorithm:** K-Means Clustering

Customer segments:

| Segment       | Description                               |
| ------------- | ----------------------------------------- |
| ⭐ High-Value  | Frequent, recent, high-spending customers |
| 🛍 Regular    | Consistent customers                      |
| 📦 Occasional | Infrequent customers                      |
| ⚠ At-Risk     | Customers inactive for a long period      |

---

### Product Recommendation System

**Approach:** Item-Based Collaborative Filtering

**Similarity Metric:** Cosine Similarity

Recommendation Process:

1. Create Customer-Product Matrix
2. Calculate Product Similarities
3. Recommend Top 5 Similar Products

---

## 🛠 Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-Learn
* K-Means Clustering
* StandardScaler
* Cosine Similarity

### Deployment

* Streamlit

### Model Storage

* Joblib

---

## 📷 Dashboard Screenshots

### 🏠 Home Dashboard

Add Screenshot Here

### 📊 EDA Dashboard

Add Screenshot Here

### 👥 Customer Segmentation

Add Screenshot Here

### 🎁 Product Recommendation

Add Screenshot Here

---

## 💼 Business Use Cases

* Customer Segmentation for Marketing Campaigns
* Personalized Product Recommendations
* Customer Retention Strategies
* Inventory Optimization
* Customer Lifetime Value Analysis
* Sales Trend Monitoring

---

## 📈 Results

* Successfully segmented customers into meaningful behavioral groups.
* Built a recommendation system capable of suggesting similar products.
* Developed an interactive analytics dashboard for business users.
* Generated actionable insights from customer transaction data.

---

## 🔮 Future Enhancements

* Hybrid Recommendation System
* Customer Churn Prediction
* Real-Time Recommendation Engine
* Advanced Customer Lifetime Value Analysis
* Streamlit Cloud Deployment

---

## 👩‍💻 Author

### Pooja Jangid

Data Analyst | Python | SQL | Power BI | Machine Learning | Streamlit

GitHub: https://github.com/poojajangid19

LinkedIn: Add Your LinkedIn Profile Link

---

## ⭐ If you found this project useful, please consider giving it a star.
