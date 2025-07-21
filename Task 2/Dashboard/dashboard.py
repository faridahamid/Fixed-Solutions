import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os

# Set wide layout
st.set_page_config(layout="wide")

# === Background Styling ===
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("file://C:/Users/lenovo/Desktop/Fixed Solutions/Task 2/Dashboard/Screenshot 2025-07-21 173950.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: #E3E3E3;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# === Load Raw Data (for cancelled invoices) ===
raw_df = pd.read_csv(r"C:\Users\lenovo\Desktop\Fixed Solutions\Task 2\Model\Online_Retail.csv", encoding='latin1')
raw_df.dropna(subset=['InvoiceNo', 'StockCode', 'Description', 'CustomerID'], inplace=True)
raw_df['InvoiceDate'] = pd.to_datetime(raw_df['InvoiceDate'])
raw_df['TotalPrice'] = raw_df['Quantity'] * raw_df['UnitPrice']



# === Load Cleaned Data ===
df = pd.read_csv(r"C:\Users\lenovo\Desktop\Fixed Solutions\Task 2\Model\data_cleaned.csv", encoding='latin1')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']


month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

df['MonthNum'] = df['InvoiceDate'].dt.month
monthly_sales = df.groupby('MonthNum')['TotalPrice'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['MonthNum'].apply(lambda x: month_names[x - 1])


# Top Products, Customers, Revenue by Country
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
rev_country = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

# === Load Precomputed RFM Segmentation ===
rfm = pd.read_csv(r"C:\Users\lenovo\Desktop\Fixed Solutions\Task 2\Model\rfm_with_labels.csv")
if 'CustomerID' in rfm.columns:
    rfm.set_index('CustomerID', inplace=True)

# Map cluster numbers to names
cluster_map = {0: 'Loyal Customers', 1: 'Mid-Tier Customers', 2: 'At-risk Customers'}
rfm['Segment'] = rfm['Cluster'].map(cluster_map)
segmentation_counts = rfm['Segment'].value_counts()

# === Dashboard Layout ===
st.title("Online Retail Customer Dashboard")

# Row 1
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Monthly Sales Trend")
    fig1, ax1 = plt.subplots(figsize=(4, 2))
    sns.lineplot(data=monthly_sales, x='Month', y='TotalPrice', color='navy', marker="o", ax=ax1)
    ax1.set_facecolor("#000000")
    fig1.patch.set_facecolor('#000000')
    ax1.tick_params(colors='white')
    ax1.set_title("Revenue by Month", color='white')
    st.pyplot(fig1)

with col2:
    st.subheader("Revenue by Country")
    fig2, ax2 = plt.subplots(figsize=(4, 2))
    sns.barplot(x=rev_country.values, y=rev_country.index, palette='Blues_d', ax=ax2)
    ax2.set_facecolor("#000000")
    fig2.patch.set_facecolor('#000000')
    ax2.tick_params(colors='white')
    ax2.set_title("Top Countries", color='white')
    st.pyplot(fig2)

with col3:
    st.subheader("Top Customers by Order Share")

    c_id_count = df['CustomerID'].value_counts()
    c_id_total = c_id_count.sum()

    c_order_share = ((c_id_count / c_id_total) * 100).reset_index()
    c_order_share.columns = ['CustomerID', 'OrderShare']
    c_order_share['CustomerID'] = c_order_share['CustomerID'].astype(str)

    top_order_share = c_order_share.sort_values('OrderShare', ascending=False).head(10)

    fig7, ax7 = plt.subplots(figsize=(4, 2))
    sns.barplot(x='OrderShare', y='CustomerID', data=top_order_share, palette='cool', ax=ax7)

    ax7.set_facecolor("#000000")
    fig7.patch.set_facecolor('#000000')
    ax7.tick_params(colors='white')
    ax7.set_title("Top 10 Customers by Order Share (%)", color='white')
    ax7.set_xlabel("Order Share (%)", color='white')
    ax7.set_ylabel("Customer ID", color='white')

    st.pyplot(fig7)



# Row 2
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Top Customers")
    fig4, ax4 = plt.subplots(figsize=(4, 2))
    sns.barplot(x=top_customers.values, y=top_customers.index.astype(str), palette='cool', ax=ax4)
    ax4.set_facecolor("#000000")
    fig4.patch.set_facecolor('#000000')
    ax4.tick_params(colors='white')
    ax4.set_title("Top Spending Customers", color='white')
    st.pyplot(fig4)

with col5:
    st.subheader("Top Products")
    fig5, ax5 = plt.subplots(figsize=(4, 2))
    sns.barplot(x=top_products.values, y=top_products.index, palette='mako', ax=ax5)
    ax5.set_facecolor("#000000")
    fig5.patch.set_facecolor('#000000')
    ax5.tick_params(colors='white')
    ax5.set_title("Most Purchased Products", color='white')
    st.pyplot(fig5)

with col6:
    st.subheader("Customer Segments")
    fig6, ax6 = plt.subplots(figsize=(4, 2))
    segmentation_counts.plot(kind='barh', color='#1E90FF', ax=ax6)
    ax6.set_facecolor("#000000")
    fig6.patch.set_facecolor('#000000')
    ax6.tick_params(colors='white')
    ax6.set_title("Customer Segments by Cluster", color='white')
    ax6.set_xlabel("Number of Customers", color='white')
    ax6.set_ylabel("Segment", color='white')
    st.pyplot(fig6)