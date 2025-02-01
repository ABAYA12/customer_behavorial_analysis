# E-Commerce Behavior Analysis Project

## Project Overview
This project analyzes e-commerce user behavior data to help predict where to place advertisements. The dataset includes user interactions (views, cart additions, purchases) with products, along with product categories, brands, and prices. The project involves:

- Downloading the dataset from Kaggle using KaggleHub.
- Adding fake user comments to simulate real-world feedback.
- Cleaning the data (formatting dates, removing special symbols, handling missing values).
- Storing the cleaned data in a PostgreSQL database for further analysis.

## Folder Structure
```
customer_behaviorial_analysis/
├── main.py                     # Main script to run the workflow
├── process_data.py             # Downloads, processes, and cleans data
├── setup_database.py           # Sets up PostgreSQL database
├── config.py                   # Configuration file
├── requirements.txt            # List of dependencies
└── data/                       # Folder for raw and cleaned data
    ├── raw/                    # Raw data (downloaded from Kaggle)
    └── cleaned/                # Cleaned data (ready for analysis)
```

## Files and Their Purpose

### 1. main.py
**Purpose:** Runs the entire workflow.

#### Steps:
- Downloads and processes the data (`process_data.py`).
- Sets up the PostgreSQL database (`setup_database.py`).

### 2. process_data.py
**Purpose:** Downloads the dataset, adds fake user comments, and cleans the data.

#### Key Features:
- Downloads the dataset using KaggleHub.
- Adds fake comments for purchase events.
- Cleans the data (formats dates, removes special symbols).
- Saves raw and cleaned data to `data/raw/` and `data/cleaned/`.

### 3. setup_database.py
**Purpose:** Sets up a PostgreSQL database and uploads the cleaned data.

#### Key Features:
- Creates a table `user_behavior` in PostgreSQL.
- Uploads the cleaned data from `data/cleaned/cleaned_ecommerce_data.csv`.

### 4. config.py
**Purpose:** Stores configuration variables (file paths, database credentials).

#### Variables:
- `RAW_DATA_PATH`: Path to save raw data.
- `CLEANED_DATA_PATH`: Path to save cleaned data.
- `DB_CONFIG`: PostgreSQL database credentials.

### 5. requirements.txt
**Purpose:** Lists all Python dependencies required for the project.

#### Dependencies:
- `pandas`: For data manipulation.
- `numpy`: For numerical operations.
- `faker`: For generating fake user comments.
- `psycopg2-binary`: For PostgreSQL database interaction.
- `kagglehub`: For downloading the dataset from Kaggle.

## How to Run the Project

### Step 1: Set Up Kaggle Credentials
1. Create a Kaggle account at [Kaggle](https://www.kaggle.com/).
2. Go to **Account → Create New API Token**.
3. Place the downloaded `kaggle.json` file in:
   - **Windows:** `C:\Users\<username>\.kaggle\`
   - **Linux/Mac:** `~/.kaggle/`

### Step 2: Install Dependencies
Run the following command to install all dependencies:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up PostgreSQL
1. Install PostgreSQL on your machine.
2. Create a database named `ecommerce_behavior_db`.
3. Update the `DB_CONFIG` in `config.py` with your PostgreSQL credentials:

```python
DB_CONFIG = {
    "dbname": "ecommerce_behavior_db",
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}
```

### Step 4: Run the Project
Execute the main script:
```bash
python main.py
```

## Workflow Overview

### Step 1: Download and Process Data
- The dataset is downloaded from Kaggle using KaggleHub.
- Fake user comments are added for purchase events.
- The data is cleaned (dates formatted, special symbols removed).
- Raw and cleaned data are saved to `data/raw/` and `data/cleaned/`.

### Step 2: Set Up Database
- A PostgreSQL table `user_behavior` is created.
- The cleaned data is uploaded to the database.

## Output Files

### 1. Raw Data
- **Location:** `data/raw/raw_ecommerce_data.csv`
- **Description:** The original dataset with fake comments added.

### 2. Cleaned Data
- **Location:** `data/cleaned/cleaned_ecommerce_data.csv`
- **Description:** The cleaned dataset, ready for analysis.

### 3. PostgreSQL Database
- **Table:** `user_behavior`

#### Schema:
```sql
Column         | Type
-----------------|-------------------
event_time     | TIMESTAMP
event_type     | VARCHAR(20)
product_id     | INT
category_id    | INT
category_code  | VARCHAR(255)
brand          | VARCHAR(255)
price          | FLOAT
user_id        | INT
user_comment   | TEXT
```

## Example Queries

### Most Purchased Products:
```sql
SELECT product_id, COUNT(*) AS purchase_count
FROM user_behavior
WHERE event_type = 'purchase'
GROUP BY product_id
ORDER BY purchase_count DESC
LIMIT 10;
```

### User Comments:
```sql
SELECT user_comment
FROM user_behavior
WHERE user_comment IS NOT NULL
LIMIT 10;
```

## Troubleshooting

### 1. KaggleHub Download Issues
- Ensure the `kaggle.json` file is in the correct location.
- Check your internet connection.

### 2. PostgreSQL Connection Issues
- Verify the `DB_CONFIG` credentials in `config.py`.
- Ensure PostgreSQL is running.

### 3. Missing Dependencies
Run `pip install -r requirements.txt` to install all dependencies.

## Future Enhancements
- **Add Visualization:** Use tools like Matplotlib or Tableau to visualize insights.
- **Train Ad Prediction Model:** Use the cleaned data to train a machine learning model for ad placement.
- **Automate Workflow:** Use a scheduler (e.g., cron or Airflow) to run the pipeline periodically.

## Contact
For questions or feedback, please reach out to [Your Name] at [Your Email].

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

**Enjoy analyzing e-commerce behavior data! 🚀**

