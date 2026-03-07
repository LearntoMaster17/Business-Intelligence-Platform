#!/usr/bin/env python3
"""
Analytics Engine for Business Intelligence Platform
Handles all business intelligence analytics and calculations
"""

import sqlite3
import pandas as pd

class AnalyticsEngine:
    def __init__(self, db_path):
        self.db_path = db_path
        self.report = ""
        
    def run_analytics(self):
        """Run business intelligence analytics"""
        print("\n📈 Running Business Intelligence Analytics...")
        self.report += "\n📈 Running Business Intelligence Analytics...\n"
        
        conn = sqlite3.connect(self.db_path)
        
        # 1. Sales Summary
        print("\n1️⃣ SALES SUMMARY")
        self.report += "\n1️⃣ SALES SUMMARY\n"
        
        query = """
        SELECT 
            COUNT(*) as total_sales,
            SUM(total_amount) as total_revenue,
            AVG(total_amount) as avg_sale_amount,
            MAX(total_amount) as highest_sale
        FROM sales
        """
        results = pd.read_sql_query(query, conn)
        print(results.to_string(index=False))
        self.report += results.to_string(index=False) + "\n"
        
        # 2. Top Products
        print("\n2️⃣ TOP SELLING PRODUCTS")
        self.report += "\n2️⃣ TOP SELLING PRODUCTS\n"
        
        query = """
        SELECT 
            product_name,
            SUM(quantity) as total_quantity,
            SUM(total_amount) as total_revenue,
            COUNT(*) as sales_count
        FROM sales 
        GROUP BY product_name 
        ORDER BY total_revenue DESC 
        LIMIT 5
        """
        results = pd.read_sql_query(query, conn)
        print(results.to_string(index=False))
        self.report += results.to_string(index=False) + "\n"
        
        # 3. Sales by Region
        print("\n3️⃣ SALES BY REGION")
        self.report += "\n3️⃣ SALES BY REGION\n"
        
        query = """
        SELECT 
            region,
            COUNT(*) as sales_count,
            SUM(total_amount) as total_revenue,
            AVG(total_amount) as avg_revenue
        FROM sales 
        GROUP BY region 
        ORDER BY total_revenue DESC
        """
        results = pd.read_sql_query(query, conn)
        print(results.to_string(index=False))
        self.report += results.to_string(index=False) + "\n"
        
        # 4. Customer Analysis
        print("\n4️⃣ CUSTOMER ANALYSIS")
        self.report += "\n4️⃣ CUSTOMER ANALYSIS\n"
        
        query = """
        SELECT 
            c.customer_type,
            COUNT(DISTINCT c.customer_id) as customer_count,
            COALESCE(SUM(s.total_amount), 0) as total_revenue,    
            COALESCE(AVG(s.total_amount), 0) as avg_purchase
        FROM customers c
        LEFT JOIN sales s ON c.customer_id = s.customer_id
        GROUP BY c.customer_type
        ORDER BY total_revenue DESC
        """
        # COALESCE(..., 0) replaces NULL with 0 (so report doesn’t show blank).
        results = pd.read_sql_query(query, conn)
        print(results.to_string(index=False))
        self.report += results.to_string(index=False) + "\n"
        
        # 5. Monthly Trends
        print("\n5️⃣ MONTHLY SALES TRENDS")
        self.report += "\n5️⃣ MONTHLY SALES TRENDS\n"
        
        query = """
        SELECT 
            strftime('%Y-%m', sale_date) as month,
            COUNT(*) as sales_count,
            SUM(total_amount) as total_revenue
        FROM sales 
        GROUP BY strftime('%Y-%m', sale_date)
        ORDER BY month DESC
        LIMIT 6
        """
        results = pd.read_sql_query(query, conn)
        print(results.to_string(index=False))
        self.report += results.to_string(index=False) + "\n"
        
        conn.close()
        return self.report
