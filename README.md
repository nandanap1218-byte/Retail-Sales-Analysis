# Retail Sales Analytics Dashboard

## Project Overview

The Retail Sales Analytics Dashboard is an interactive data analytics project developed using Python and Streamlit. The project focuses on cleaning, analyzing, and visualizing retail sales data to provide actionable business insights.

The dashboard enables users to monitor sales performance, profitability, customer behavior, product performance, and regional trends through interactive visualizations and filters.

---

## Project Objectives

* Clean and preprocess retail sales data.
* Analyze sales trends and business performance.
* Calculate key performance indicators (KPIs).
* Identify top-performing products, regions, and customers.
* Build an interactive dashboard for business decision-making.

---

## Dataset

The dataset contains retail sales transaction records, including:

* Order Information
* Customer Information
* Product Categories and SubCategories
* Sales and Profit Data
* Region and Segment Details
* Return Status

Total Records: **80,000**

---

## Data Cleaning Performed

The following preprocessing steps were completed:

* Removed duplicate records.
* Standardized date formats to YYYY-MM-DD.
* Converted monetary columns to numeric format.
* Standardized category and segment values.
* Standardized Returned values (Yes/No).
* Removed missing values.
* Removed invalid quantity values.

---

## Key Performance Indicators (KPIs)

The dashboard calculates and displays:

* Total Revenue
* Total Profit
* Profit Margin
* Average Order Value (AOV)
* Total Orders

---

## Dashboard Features

### Interactive Filters

* Date Range
* Region
* Category
* Segment

### Visualizations

* Monthly Sales Trend
* Sales by Category
* Sales by SubCategory
* Region Comparison
* Top 10 Customers
* Year-over-Year Growth

### Interactive Data Table

* Dynamic table that updates automatically based on selected filters.

---

## Key Insights

* December consistently records the highest sales every year.
* Technology is the highest-performing product category.
* North America East generates the highest sales among all regions.
* Laptops are the top-selling subcategory.
* Linda Hernandez is the highest-value customer.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Streamlit
* Plotly
* Matplotlib
* Jupyter Notebook
* VS Code

---

## Repository Structure

retail_sales_dashboard/

├── app.py

├── retail_sales_cleaned.csv

├── retail_sales.ipynb

├── retail_sales_report.pptx

└── README.md

---

## Installation

Install the required libraries:

pip install streamlit pandas numpy plotly matplotlib

---

## Running the Dashboard

Run the Streamlit application:

streamlit run app.py

After running the command, the dashboard will be available in your browser at:

http://localhost:8501

---

## Files Description

### app.py

Contains the Streamlit dashboard application and visualizations.

### retail_sales_cleaned.csv

Cleaned retail sales dataset used for analysis and dashboard development.

### retail_sales.ipynb

Jupyter Notebook containing data cleaning, exploratory data analysis, KPI calculations, and visualization code.

### retail_sales_report.pptx

Project presentation summarizing objectives, methodology, dashboard features, and business insights.

---

## Conclusion

This project demonstrates the complete data analytics workflow, including data cleaning, exploratory data analysis, KPI calculation, data visualization, and dashboard development. The interactive dashboard provides meaningful insights that support data-driven business decisions.

---

## Author

Nandana P
