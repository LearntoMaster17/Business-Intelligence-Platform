#!/usr/bin/env python3
"""
Analysis Orchestrator for Business Intelligence Platform
Handles the complete analysis pipeline orchestration
"""

import os
from data_loader import DataLoader
from analytics_engine import AnalyticsEngine
from report_generator import ReportGenerator

class AnalysisOrchestrator:
    def __init__(self, db_path):
        self.db_path = db_path
        self.data_loader = DataLoader(db_path)
        self.analytics_engine = AnalyticsEngine(db_path)
        self.report_generator = ReportGenerator(db_path)
        
    def run_full_analysis(self):
        """Run complete analysis pipeline"""
        print("🚀 Starting Business Intelligence Platform")
        print("=" * 50)
        
        try:
            # Step 1: Load or generate data
            self.data_loader.load_sample_data()
            
            # Step 2: Run analytics
            self.analytics_engine.run_analytics()
            
            # Step 3: Generate report
            self.report_generator.generate_simple_report()
            
            print("\n🎉 Analysis completed successfully!")
            print(f"📊 Database location: {os.path.abspath(self.db_path)}")
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
