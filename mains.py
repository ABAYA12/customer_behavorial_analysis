from process_data import process_data
from setup_database import setup_database

def main():
    print("Step 1: Downloading and processing data...")
    process_data()
    
    print("\nStep 2: Setting up database...")
    setup_database()
    
    print("\nWorkflow completed!")

if __name__ == "__main__":
    main()