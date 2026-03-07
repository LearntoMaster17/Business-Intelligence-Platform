#!/usr/bin/env python3
"""
Data Loader for Business Intelligence Platform
Handles loading data from CSV files and generating sample data
"""

import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import random

class DataLoader:
    def __init__(self, db_path):
        self.db_path = db_path
        
    def load_sample_data(self):
        """Load sample data from CSV files"""
        print("📊 Loading sample data...")
        
        try:
            # Load customers data
            customers_df = pd.read_csv('../data/sample_customers.csv')
            customers_df.to_sql('customers', sqlite3.connect(self.db_path), if_exists='replace', index=False)
            """
            to_sql = to write the Data of csv into the SQLite database.
            - Table name: 'customers'
            - sqlite3.connect(self.db_path) → creates DB connection
            - if_exists='replace' → drop old table & recreate it
            - index=False → don’t store Pandas index column
            """
            
            # Load sales data
            sales_df = pd.read_csv('../data/sample_sales.csv')
            sales_df.to_sql('sales', sqlite3.connect(self.db_path), if_exists='replace', index=False)
            
            print(f"✅ Loaded {len(customers_df)} customers and {len(sales_df)} sales records")
            
        except FileNotFoundError as e:
            print(f"❌ CSV files not found: {e}")
            self.generate_sample_data()
            
    def generate_sample_data(self):
        """Generate sample data if CSV files are missing"""
        print("🎲 Generating sample data...")
        
        conn = sqlite3.connect(self.db_path)
        
        # Generate sample customers
        customers_data = []
        for i in range(1, 21):
            customers_data.append((
                i,
                f"Customer{i}",
                f"LastName{i}",
                f"customer{i}@email.com",
                f"555-{i:04d}",   # i:04d = zero-padded 4 digit number
                f"Company{i}",
                (datetime.now() - timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d'),
                random.choice(['Premium', 'Standard', 'Business']),
                random.randint(5000, 20000),
                random.randint(0, 5000)
            ))
        
        conn.executemany('''
        INSERT INTO customers VALUES (?,?,?,?,?,?,?,?,?,?)
        ''', customers_data)
        
        """In SQLite’s Python driver (sqlite3), the Connection object is a bit special:
            It has some “shortcut” methods (execute, executemany, executescript).
            When you call conn.executemany(...), under the hood it creates a temporary cursor, runs the SQL, and then closes that cursor."""
        
        # Generate sample sales
        sales_data = []
        products = ['Laptop', 'Monitor', 'Chair', 'Desk', 'Phone', 'Tablet']
        regions = ['North', 'South', 'East', 'West']
        reps = ['John Smith', 'Sarah Johnson', 'Mike Davis', 'Lisa Brown']
        
        for i in range(1, 51):
            product = random.choice(products)
            category = 'Electronics' if product in ['Laptop', 'Monitor', 'Phone', 'Tablet'] else 'Furniture'
            quantity = random.randint(1, 5)
            unit_price = random.randint(100, 1500)
            
            sales_data.append((
                i,
                random.randint(1, 20),
                product,
                category,
                quantity,
                unit_price,
                quantity * unit_price,
                (datetime.now() - timedelta(days=random.randint(1, 90))).strftime('%Y-%m-%d'),
                random.choice(reps),
                random.choice(regions)
            ))
        
        conn.executemany('''
        INSERT INTO sales VALUES (?,?,?,?,?,?,?,?,?,?)
        ''', sales_data)
        
        conn.commit()
        conn.close()
        print("✅ Sample data generated successfully!")
