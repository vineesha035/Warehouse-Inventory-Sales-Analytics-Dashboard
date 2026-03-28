# Warehouse-Inventory-Analytics-Dashboard

View the Dashboard on Tableau:  
*https://public.tableau.com/views/WarehouseInventoryAnalyticsDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link*

# Project Overview & Objectives

This project involves building an interactive Warehouse Inventory & Sales Analytics Dashboard using Tableau. The dataset utilized contains information on grocery items, including product details, stock levels, supplier performance, sales volume, and more.

1)Monitor stock levels and product availability. 2) Evaluate supplier performance based on pricing and delivery efficiency. 3) Analyze sales trends and identify fast/slow-moving items.

# Dataset Information

Source: Kaggle API - Grocery Inventory and Sales Dataset
Columns Used:

Product Details: Product_ID, Product_Name, Category

Inventory: Stock_Quantity, Reorder_Level, Reorder_Quantity, Expiration_Date

Supplier Details: Supplier_ID, Supplier_Name

Sales: Sales_Volume, Inventory_Turnover_Rate

<div class='tableauPlaceholder' id='viz1741660862712' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wa&#47;WarehouseInventoryAnalyticsDashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WarehouseInventoryAnalyticsDashboard&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wa&#47;WarehouseInventoryAnalyticsDashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>   

# Data Preprocessing

Performed using Python (Pandas):

Date Formatting: Converted Date_Received, Last_Order_Date, and Expiration_Date to datetime format.

Unit Price Cleanup: Removed currency symbols and converted to numeric.

Missing Value Handling: Checked and imputed missing values where necessary.

Category Grouping: Grouped items into broader product categories.

Tableau Dashboards Created

# 1️⃣ Stock Level Monitoring 📊

Purpose: Track current stock levels and highlight products needing restocking.

Metrics Used: Stock_Quantity, Reorder_Level, Expiration_Date

Conditional Formatting:

Green → Sufficient Stock

Orange → Low Stock

Red → Reorder Needed

# 2️⃣ Supplier Performance Analysis 📦

Purpose: Evaluate suppliers based on efficiency and product availability.

Metrics Used: Supplier_Name, Sales_Volume, Reorder_Quantity

Insights: Identify best-performing suppliers and optimize vendor relationships.

# 3️⃣ Sales Trend Analysis 📈

Purpose: Identify fast-moving and slow-moving products.

Metrics Used: Sales_Volume, Category, Quarter of Last_Order_Date

Insights: Seasonal demand trends, category-wise performance.

# Deployment

The dashboard is published on Tableau Public for interactive insights.

Users can filter by Category, Supplier, and Sales Period for detailed analysis.

# Future Enhancements

Integrating live data from APIs for real-time inventory tracking.

Adding forecasting models to predict future sales trends.

Enhancing warehouse space optimization insights.

For any questions or feedback, feel free to reach out!
