import psycopg2
import pandas as pd
from configs import DB_CONFIG, CLEANED_DATA_PATH

def setup_database():
    # Connect to PostgreSQL
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_behavior (
            event_time TIMESTAMP,
            event_type VARCHAR(20),
            product_id INT,
            category_id INT,
            category_code VARCHAR(255),
            brand VARCHAR(255),
            price FLOAT,
            user_id INT,
            user_comment TEXT
        )
    """)
    
    # Insert cleaned data
    df = pd.read_csv(CLEANED_DATA_PATH)
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO user_behavior 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Data uploaded to PostgreSQL")

if __name__ == "__main__":
    setup_database()