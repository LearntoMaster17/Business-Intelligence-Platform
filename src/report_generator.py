#!/usr/bin/env python3
"""
Report Generator for Business Intelligence Platform
Handles generating and saving business intelligence reports
"""

import sqlite3
import pandas as pd
import os
from datetime import datetime
from analytics_engine import AnalyticsEngine

class ReportGenerator:
    def __init__(self, db_path):
        self.db_path = db_path
        self.analytics_engine = AnalyticsEngine(db_path)
        
    def generate_simple_report(self):
        """Generate a simple text report"""
        print("\n📄 Generating Business Report...")
        
        conn = sqlite3.connect(self.db_path)
        
        report = f"""
========================================
BUSINESS INTELLIGENCE REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
========================================

EXECUTIVE SUMMARY:
"""
        
        # Get key metrics
        query = "SELECT COUNT(*) as total_sales, SUM(total_amount) as total_revenue FROM sales"
        results = pd.read_sql_query(query, conn)
        
        total_sales = results.iloc[0]['total_sales']
        total_revenue = results.iloc[0]['total_revenue']
        
        report += f"""
• Total Sales Transactions: {total_sales}
• Total Revenue: ${total_revenue:,.2f}
• Average Sale Amount: ${total_revenue/total_sales:,.2f}

TOP PERFORMING REGIONS:
"""
        
        query = """
        SELECT region, SUM(total_amount) as revenue 
        FROM sales 
        GROUP BY region 
        ORDER BY revenue DESC 
        LIMIT 3
        """
        results = pd.read_sql_query(query, conn)
        
        for _, row in results.iterrows():
            # print("row", row)    
            report += f"• {row['region']}: ${row['revenue']:,.2f}\n"
        
        additional_report = self.analytics_engine.run_analytics()
        report += additional_report
        
        report += f"""
========================================
Report Status: ✅ GENERATED SUCCESSFULLY
Database: SQLite (No credentials needed!)
========================================
"""
        
        # Save report
        os.makedirs('../reports', exist_ok=True)
        report_file = f"../reports/bi_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        # print(report)
        print(f"💾 Report saved to: {report_file}")
        
        conn.close()
