import os

# Paths
RAW_DATA_PATH = os.path.join("data", "raw", "raw_ecommerce_data.csv")
CLEANED_DATA_PATH = os.path.join("data", "cleaned", "cleaned_ecommerce_data.csv")

# PostgreSQL Configuration
DB_CONFIG = {
    "dbname": "ecommerce_behavior_db",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}