# 🛒 E-commerce Furniture Sales Dashboard – Power BI Project

A comprehensive Power BI dashboard to analyze sales, pricing, discounts, and shipping insights for an e-commerce furniture dataset. This project demonstrates interactive reporting and data storytelling through KPIs, DAX measures, and visual exploration.



## 📊 Dashboard Overview

This dashboard enables business teams to:
- Track total revenue, sold quantity, discount impact, and average pricing
- Identify top-selling products and underperformers
- Analyze the effect of free shipping and discount percentages on sales
- Explore data using slicers and visual interactions



## 🎯 Project Goals

- Analyze e-commerce furniture sales performance using Power BI  
- Identify patterns based on price, discount, and shipping tags  
- Visualize top-selling products and revenue generators  
- Build dynamic visuals to guide sales decisions  
- Share insights through GitHub and professional reporting



## 📂 Dataset Overview

- Product-level sales data including:
  - `productTitle` – Item name  
  - `originalPrice` – MRP before discount  
  - `price` – Final selling price  
  - `sold` – Units sold  
  - `tagText` – Shipping tag info (e.g., Free shipping)
- Derived fields like `Discount %`, `Price Bins`, and `Sold Bins` created via Power BI



## ⚙️ Tools & Technologies Used

- Power BI Desktop  
- DAX (Data Analysis Expressions)  
- Python (used for initial data cleaning with pandas)  
- GitHub for sharing the project  
- CSV dataset (cleaned)



## 📐 DAX Measures Used

- `Total Revenue = SUMX('cleaned_ecom', price * sold)`  
- `Total Units Sold = SUM(sold)`  
- `Average Price = AVERAGE(price)`  
- `Total Discount = SUMX((originalPrice - price) * sold)`  

### 📏 Calculated Columns

- `Discount % = (originalPrice - price) / originalPrice`  
- `Price Bins` – Grouped by $10 intervals  
- `Sold Bins` – Grouped by 200-unit intervals  



## 📌 Key Insights

- Free shipping products achieved higher sales volume  
- Top 10 products drove majority of total units sold  
- Products priced under $200 showed strongest performance  
- 40–60% discount range had the highest impact on conversions  
- Heatmap revealed lower-priced and medium-discounted items sold best  
- Higher discounts did not always lead to higher revenue



## 🧭 Navigation

- KPI Cards (Revenue, Sold, Avg Price, Discount)  
- Bar Chart: Top 10 Sold Products  
- Donut: Sold by Shipping Tag  
- Heatmap: Price vs Sold  
- Column Chart: Sold by Discount %  
- Pie Chart: Count by Price & Sold Bins  
- Slicers: Product Title, Price, Sold



## 📁 Files Included

- `cleaned_ecom.csv` – Cleaned dataset (if included)  
- `Ecommerce_Dashboard.pbix` – Power BI report file  
- `README.md` – Project description and usage



## 👤 Author

**Shreesha – Data Analyst Intern**  
[LinkedIn Profile](https://www.linkedin.com/in/shreesha-poojary85)



## 💡 Usage

Open the `.pbix` file in Power BI Desktop.  
All visuals are fully interactive.  
Use slicers to filter product-level performance.

