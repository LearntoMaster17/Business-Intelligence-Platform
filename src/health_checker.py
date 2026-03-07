#!/usr/bin/env python3
"""
Health Checker for Business Intelligence Platform
Handles system health checks and data validation
"""

import sqlite3

class HealthChecker:
    def __init__(self, db_path):
        self.db_path = db_path
        
    def health_check(self):
        """Check system health"""
        print("🏥 System Health Check")
        print("=" * 30)
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Check tables exist
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"✅ Database tables: {[table[0] for table in tables]}")
            
            # Check data counts
            cursor.execute("SELECT COUNT(*) FROM customers")
            customer_count = cursor.fetchone()[0]
            print(f"✅ Customers in database: {customer_count}")
            
            cursor.execute("SELECT COUNT(*) FROM sales")
            sales_count = cursor.fetchone()[0]
            print(f"✅ Sales records: {sales_count}")
            
            print("✅ System is healthy and ready!")
            
            conn.close()
            
        except Exception as e:
            print(f"❌ Health check failed: {e}")
