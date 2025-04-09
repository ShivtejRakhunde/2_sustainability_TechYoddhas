# ⚡ Smart Grid Optimization: Integrating Renewable Energy for Sustainable Power Systems

This project focuses on building a predictive and analytical pipeline for a smart grid system powered by renewable energy sources. By forecasting energy generation and modeling consumption across nodes, we aim to improve power distribution and grid stability in a sustainable manner.

---

## 🎯 Goals

1. Accurately **forecast power generation** using historical data.
2. **Distribute predicted power** intelligently across consumption nodes.
3. **Assess and predict grid stability** based on real-time and generated metrics.

---

## 📌 Problem Statement

The project involves the following core tasks:

### 1. Power Prediction
- Use past **5 years of historical data** (20 files) to forecast **hourly power generation** for the **first 3 months of 2024**.
- Features: `DateTime`, `Air Temperature`, `Pressure`, `Wind Speed`.

### 2. Data Preparation
- Merge all 20 CSV data files into a **single input dataset** for model training.
- Final dataset columns: `DateTime`, `Air`, `Pressure`, `Wind Speed`, `Power Generated`.

### 3. Power Distribution
- Distribute the **predicted power (p)** for each hour among 3 nodes:
  - 🔵 Node 1 → 20%  
  - 🟢 Node 2 → 45%  
  - 🔴 Node 3 → 35%

### 4. Grid Stability Prediction
- Use the **Grid folder dataset** containing:
  - `Price per Unit`
  - `Unit Consumption`
  - `Grid Stability` (target variable)
- Combine with new features: `Predicted Power`, `Node-wise Power Distribution`.

---

## 🧠 Machine Learning Tasks

- **Regression Model** for predicting Power Generation (`p`)
- **Classification/Regression Model** for Grid Stability using:
  - Historical + Predicted data
  - Real-time grid consumption metrics

---
