# Business Intelligence Platform

A modular SQLite-based analytics platform for sales and customer- **Database**: SQLite (no credentials required)
- **Location**: `business_intelligence.db` (auto-created)
- **Tables**: `customers`, `sales`
- **Encoding**: UTF-8 compatible

---

## 📄 Resume Section

**Business Intelligence Analytics Platform** | *Python, SQLite, Pandas*  
Developed a modular enterprise-grade business intelligence platform for sales and customer data analysis. Implemented automated data processing pipeline with CSV import capabilities, real-time analytics engine, and comprehensive reporting system. Built scalable architecture with 7 specialized modules including data loading, analytics processing, health monitoring, and report generation. Platform features command-line interface with multiple execution modes, automatic sample data generation, and UTF-8 encoded report exports. Achieved complete separation of concerns through modular design enabling independent testing and maintenance of analytics components.

**Technologies Used:** Python 3.12, SQLite Database, Pandas Data Analysis, Object-Oriented Programming (OOP), Modular Architecture, CSV Data Processing, Command Line Interface (CLI), Automated Reporting, Data Visualization, Business Intelligence (BI), Git Version Control analysis.

## Features

- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Data Management**: Load data from CSV files or generate sample data automatically
- **Analytics Engine**: Comprehensive business intelligence analytics
- **Report Generation**: Automated timestamped reports with detailed insights
- **Health Monitoring**: System health checks and data validation
- **Command Line Interface**: Multiple execution options for different use cases

## Project Structure

```
sales-analytics-platform/
├── src/                           # Source code modules
│   ├── main.py                   # Entry point and CLI
│   ├── database_manager.py       # Database setup and management
│   ├── data_loader.py           # CSV loading and sample data generation
│   ├── analytics_engine.py      # Business intelligence analytics
│   ├── report_generator.py      # Report generation and file output
│   ├── health_checker.py        # System health validation
│   └── analysis_orchestrator.py # Pipeline orchestration
├── data/                         # Data files
│   ├── sample_customers.csv     # Customer data
│   ├── sample_sales.csv         # Sales transaction data
│   └── config.json              # Configuration settings
├── reports/                      # Generated reports (auto-created)
├── requirements.txt              # Python dependencies
└── README.md                    # This file
```

## Quick Start

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run Complete Analysis
```bash
python src/main.py
```

## Command Line Options

| Option | Description |
|--------|-------------|
| *(no arguments)* | Run complete analysis pipeline |
| `--health-check` | Check system status and data integrity |
| `--analytics-only` | Run analytics without data loading |
| `--generate-data` | Generate sample data for testing |
| `--report-only` | Generate business intelligence report only |

## Data Sources

The platform automatically loads data from:
- `data/sample_customers.csv` - Customer information and profiles
- `data/sample_sales.csv` - Sales transaction records

If CSV files are not found, the system automatically generates sample data for testing.

## Analytics Capabilities

1. **Sales Summary** - Total sales, revenue, and performance metrics
2. **Product Analysis** - Top-selling products by revenue and quantity
3. **Regional Performance** - Geographic sales distribution and trends
4. **Customer Segmentation** - Analysis by customer type (Premium, Standard, Business)
5. **Time Series Analysis** - Monthly sales trends and patterns

## Output

- **Console Analytics** - Real-time analysis results displayed in terminal
- **Business Reports** - Detailed reports saved as `reports/bi_report_YYYYMMDD_HHMMSS.txt`
- **SQLite Database** - Persistent data storage in `business_intelligence.db`

## Example Usage

```bash
# Complete analysis with data loading, analytics, and reporting
python src/main.py

# Quick system health check
python src/main.py --health-check

# Run analytics on existing data
python src/main.py --analytics-only

# Generate sample data for testing
python src/main.py --generate-data

# Generate report only
python src/main.py --report-only
```

## Database

- **Type**: SQLite (no credentials required)
- **Location**: `business_intelligence.db` (auto-created)
- **Tables**: `customers`, `sales`
- **Encoding**: UTF-8 compatible
