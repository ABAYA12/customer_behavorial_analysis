import os
import kagglehub
import pandas as pd
import numpy as np
from faker import Faker
import re
import zipfile
from configs import RAW_DATA_PATH, CLEANED_DATA_PATH

# Initialize fake comment generator
fake = Faker()
Faker.seed(42)

def download_dataset():
    """Download dataset using KaggleHub."""
    print("Downloading dataset...")
    dataset_path = kagglehub.dataset_download("mkechinov/ecommerce-behavior-data-from-multi-category-store")
    
    # Extract zip file if needed
    if dataset_path.endswith('.zip'):
        with zipfile.ZipFile(dataset_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(dataset_path))
        dataset_path = dataset_path.replace('.zip', '')
    
    print(f"Dataset downloaded to: {dataset_path}")
    return dataset_path

def add_comments(df):
    """Generate fake user comments for 'purchase' events only."""
    comments = []
    for event_type in df['event_type']:
        if event_type == 'purchase':
            comment = fake.sentence(nb_words=10) if np.random.rand() > 0.3 else np.nan  # 30% missing comments
        else:
            comment = np.nan
        comments.append(comment)
    df['user_comment'] = comments
    return df

def clean_data(df):
    """Clean the dataset."""
    # Format event_time
    df['event_time'] = pd.to_datetime(df['event_time']).dt.strftime('%Y-%m-%d %H:%M:%S')
    
    # Clean text fields
    text_columns = ['category_code', 'brand', 'user_comment']
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: re.sub(r'[_,;/\|{}[\]!@#%^&*()=+]', '', str(x)) if pd.notnull(x) else x)
    
    return df

def process_data():
    # Download and get dataset path
    dataset_dir = download_dataset()
    csv_path = os.path.join(dataset_dir, '2019-Nov.csv')
    
    # Load dataset
    df = pd.read_csv(
        csv_path,
        dtype={
            'product_id': 'int32',
            'category_id': 'int32',
            'user_id': 'int32',
            'price': 'float32'
        },
        usecols=lambda col: col != 'user_session'  # Drop user_session to save memory
    )
    
    # Add comments
    df = add_comments(df)
    
    # Clean data
    df = clean_data(df)
    
    # Save raw + cleaned data
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)
    df.to_csv(RAW_DATA_PATH, index=False)
    
    # Save cleaned data (without NA comments)
    os.makedirs(os.path.dirname(CLEANED_DATA_PATH), exist_ok=True)
    df.dropna(subset=['user_comment'], inplace=True)
    df.to_csv(CLEANED_DATA_PATH, index=False)
    
    print(f"\nProcessed data saved to:\n- Raw: {RAW_DATA_PATH}\n- Cleaned: {CLEANED_DATA_PATH}")

if __name__ == "__main__":
    process_data()