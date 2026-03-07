#!/usr/bin/env python3
"""
Business Intelligence Platform - Main Entry Point
SQLite-based analytics platform for sales and customer data
Enterprise-ready business intelligence solution
"""

import sys
from database_manager import DatabaseManager
from data_loader import DataLoader
from analytics_engine import AnalyticsEngine
from report_generator import ReportGenerator
from health_checker import HealthChecker
from analysis_orchestrator import AnalysisOrchestrator

class BusinessIntelligencePlatform:
    def __init__(self):
        self.db_path = "../business_intelligence.db"
        self.db_manager = DatabaseManager(self.db_path)
        self.data_loader = DataLoader(self.db_path)
        self.analytics_engine = AnalyticsEngine(self.db_path)
        self.report_generator = ReportGenerator(self.db_path)
        self.health_checker = HealthChecker(self.db_path)
        self.analysis_orchestrator = AnalysisOrchestrator(self.db_path)
        
    def health_check(self):
        """Check system health"""
        self.health_checker.health_check()
        
    def run_analytics(self):
        """Run business intelligence analytics"""
        self.analytics_engine.run_analytics()
    
    def load_csv_data(self):
        """Load data from CSV files"""
        self.data_loader.load_sample_data()
        
    def generate_sample_data(self):
        """Generate sample data if CSV files are missing"""
        self.data_loader.generate_sample_data()
        
    def generate_simple_report(self):
        """Generate a simple text report"""
        self.report_generator.generate_simple_report()
        
    def run_full_analysis(self):
        """Run complete analysis pipeline"""
        self.analysis_orchestrator.run_full_analysis()

def main():
    """Main function with command line options"""
    bi_platform = BusinessIntelligencePlatform()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--health-check':
            bi_platform.health_check()
        elif sys.argv[1] == '--analytics-only':
            bi_platform.run_analytics()
        elif sys.argv[1] == '--load-csv-data':
            bi_platform.load_csv_data()
        elif sys.argv[1] == '--generate-sample-data':
            bi_platform.generate_sample_data()
        elif sys.argv[1] == '--report-only':
            bi_platform.generate_simple_report()
        else:
            print("Available options:")
            print("  --health-check         : Check system status")
            print("  --analytics-only       : Run analytics only")
            print("  --load-csv-data        : Load data from CSV files")
            print("  --generate-sample-data : Generate sample data")
            print("  --report-only          : Generate report only")
            print("  (no args)              : Run full analysis")
    else:
        bi_platform.run_full_analysis()

if __name__ == "__main__":
    main()
