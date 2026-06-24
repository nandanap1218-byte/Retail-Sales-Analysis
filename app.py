import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Sales Dashboard")

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv("retail_sales_cleaned.csv")

df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# =====================================
# SIDEBAR FILTERS
# =====================================

st.sidebar.header("Filters")

# Date Range

start_date = st.sidebar.date_input(
    "Start Date",
    df['OrderDate'].min().date()
)

end_date = st.sidebar.date_input(
    "End Date",
    df['OrderDate'].max().date()
)

# Region

region = st.sidebar.multiselect(
    "Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

# Category

category = st.sidebar.multiselect(
    "Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

# Segment

segment = st.sidebar.multiselect(
    "Segment",
    options=df['Segment'].unique(),
    default=df['Segment'].unique()
)

# =====================================
# APPLY FILTERS
# =====================================

filtered_df = df[
    (df['OrderDate'].dt.date >= start_date) &
    (df['OrderDate'].dt.date <= end_date) &
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Segment'].isin(segment))
]

# =====================================
# KPI CALCULATIONS
# =====================================

total_revenue = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = filtered_df['OrderID'].nunique()

aov = total_revenue / total_orders if total_orders > 0 else 0

# =====================================
# KPI CARDS
# =====================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "Revenue",
    f"{total_revenue/1_000_000:.2f} M"
)

kpi2.metric(
    "Profit",
    f"{total_profit/1_000_000:.2f} M"
)

kpi3.metric(
    "AOV",
    f"{aov:.0f}"
)

kpi4.metric(
    "Orders",
    f"{total_orders:,}"
)

st.markdown("---")

# =====================================
# MONTHLY SALES TREND
# =====================================

filtered_df['YearMonth'] = (
    filtered_df['OrderDate']
    .dt.to_period('M')
    .astype(str)
)

monthly_sales = (
    filtered_df
    .groupby('YearMonth')['Sales']
    .sum()
    .reset_index()
)

fig_monthly = px.line(
    monthly_sales,
    x='YearMonth',
    y='Sales',
    markers=True,
    title='Monthly Sales Trend'
)

# =====================================
# SALES BY CATEGORY
# =====================================

category_sales = (
    filtered_df
    .groupby('Category')['Sales']
    .sum()
    .reset_index()
)

fig_category = px.bar(
    category_sales,
    x='Category',
    y='Sales',
    title='Sales by Category'
)

# =====================================
# 2 x 2 MATRIX - ROW 1
# =====================================

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_monthly, use_container_width=True)

with col2:
    st.plotly_chart(fig_category, use_container_width=True)

# =====================================
# SALES BY SUBCATEGORY
# =====================================

subcategory_sales = (
    filtered_df
    .groupby('SubCategory')['Sales']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_subcategory = px.bar(
    subcategory_sales,
    x='SubCategory',
    y='Sales',
    title='Sales by SubCategory'
)

# =====================================
# REGION COMPARISON
# =====================================

region_sales = (
    filtered_df
    .groupby('Region')['Sales']
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region_sales,
    x='Region',
    y='Sales',
    title='Region Comparison'
)

# =====================================
# 2 x 2 MATRIX - ROW 2
# =====================================

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(fig_subcategory, use_container_width=True)

with col4:
    st.plotly_chart(fig_region, use_container_width=True)

st.markdown("---")

# =====================================
# TOP 10 CUSTOMERS
# =====================================

top_customers = (
    filtered_df
    .groupby('CustomerName')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_customer = px.bar(
    top_customers,
    x='CustomerName',
    y='Sales',
    title='Top 10 Customers'
)

st.plotly_chart(
    fig_customer,
    use_container_width=True
)

# =====================================
# YEAR OVER YEAR GROWTH
# =====================================

filtered_df['Year'] = filtered_df['OrderDate'].dt.year

yearly_sales = (
    filtered_df
    .groupby('Year')['Sales']
    .sum()
    .reset_index()
)

yearly_sales['YoY Growth %'] = (
    yearly_sales['Sales']
    .pct_change() * 100
)

fig_yoy = px.bar(
    yearly_sales,
    x='Year',
    y='YoY Growth %',
    title='Year Over Year Growth (%)'
)

st.plotly_chart(
    fig_yoy,
    use_container_width=True
)

# =====================================
# DATA TABLE
# =====================================

st.subheader("Filtered Data")

st.dataframe(filtered_df)

# =====================================
# KPI SUMMARY TABLE
# =====================================

st.subheader("KPI Summary")

summary = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Profit",
        "Orders",
        "AOV"
    ],
    "Value": [
        f"{total_revenue/1_000_000:.2f} M",
        f"{total_profit/1_000_000:.2f} M",
        f"{total_orders:,}",
        f"{aov:.0f}"
    ]
})

st.dataframe(summary)