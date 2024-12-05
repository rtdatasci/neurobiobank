import pandas as pd
import os

# Define the path to the raw data folder
RAW_DATA_PATH = os.path.join(os.getcwd(), 'data', 'raw')

def extract_csv(file_name):
    """
    Extracts data from a CSV file.
    
    Args:
    - file_name (str): The name of the CSV file to be read from the raw data folder.
    
    Returns:
    - pandas.DataFrame: The extracted data as a pandas DataFrame.
    """
    # Build the file path
    file_path = os.path.join(RAW_DATA_PATH, file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_name} not found in {RAW_DATA_PATH}")

    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(file_path)

    return df

if __name__ == "__main__":
    # Example of usage: extracting data from 'your_data.csv'
    try:
        data = extract_csv('your_data.csv')
        print(f"Data extracted successfully:\n{data.head()}")
    except Exception as e:
        print(f"Error: {e}")
