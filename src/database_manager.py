
#!/usr/bin/env python3
"""
Database Manager for Business Intelligence Platform
Handles database setup and basic operations
"""

import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path="business_intelligence.db"):
        self.db_path = db_path
        self.setup_database()
        
    def setup_database(self):
        """Create SQLite database and tables"""
        print("🏗️  Setting up SQLite database...")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create customers table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            company TEXT,
            registration_date DATE,
            customer_type TEXT CHECK(customer_type IN ('Premium', 'Standard', 'Business')),
            credit_limit DECIMAL(10,2),
            total_spent DECIMAL(10,2) DEFAULT 0.00
        )
        ''')
        
        # Create sales table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product_name TEXT NOT NULL,
            category TEXT,
            quantity INTEGER NOT NULL,
            unit_price DECIMAL(10,2) NOT NULL,
            total_amount DECIMAL(10,2) NOT NULL,
            sale_date DATE NOT NULL,
            sales_rep TEXT,
            region TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
        )
        ''')
        
        conn.commit()
        conn.close()
        print("✅ Database created successfully!")
        
    def get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_path)
        
    def get_db_path(self):
        """Get absolute database path"""
        return os.path.abspath(self.db_path)