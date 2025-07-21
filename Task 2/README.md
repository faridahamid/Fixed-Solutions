#  Customer Segmentation Using K-Means – Online Retail Dataset

This project focuses on customer behavior analysis and segmentation using the **Online Retail dataset** from the UCI Machine Learning Repository. It was developed as part of the **Fixed Solutions internship program** to demonstrate practical applications of data science in marketing and business strategy.

---

## Objective

To analyze customer transactions and **segment customers into meaningful groups** using **RFM analysis** and **K-Means clustering**, helping businesses tailor marketing strategies and improve customer retention.

---

## Dataset Description

- **Source:** [Online Retail Dataset](./Task%202/Model/Online_Retail.xlsx)
- **Records:** ~500,000 transactions  
- **Period:** Dec 2010 to Dec 2011  
- **Fields:** InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

---



## Steps and Methodology

1. **Data Cleaning**  
   - Removed nulls, duplicates, and non-product entries (e.g., postage, samples)  
   - Filtered for valid transactions and UK-based customers

2. **Feature Engineering**  
   - Calculated **RFM (Recency, Frequency, Monetary)** values for each customer  
   - Normalized features for clustering

3. **Clustering with K-Means**  
   - Applied Elbow Method to select optimal number of clusters  
   - Segmented customers into 3 main groups:
     - High-Value Loyal Customers  
     - Mid-Tier or Potential Customers  
     - Low-Value or At-Risk Customers

4. **Insights & Business Recommendations**  
   - Found that most revenue comes from a small group of customers  
   - Seasonality affects sales (peaks in Nov–Dec)  
   - Weekdays outperform weekends in order volume

---

## Results

- **Total Revenue:** £8.7M from 18,400 orders  
- **Average Order Value:** £474  
- **Non-product revenue :** £149,981  
- **Customer Segments Identified:** 3 distinct behavioral groups  
- **Actionable Insights:** Focus retention efforts on Cluster 0, run win-back campaigns for Cluster 2

---

##  Project Presentation

The project was visually presented in a **10-slide PowerPoint** with:

- Problem definition and objectives  
- Data cleaning and transformation visuals  
- Monthly trend analysis and top products  
- RFM segmentation strategy and cluster insights  




