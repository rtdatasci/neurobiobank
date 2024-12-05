import pandas as pd

def transform_data(df):
    """
    Transforms the extracted data to prepare it for loading into PostgreSQL.
    
    Args:
    - df (pandas.DataFrame): The extracted data as a pandas DataFrame.
    
    Returns:
    - pandas.DataFrame: The transformed data.
    """
    
    # Example 1: Remove duplicates
    df = df.drop_duplicates()

    # Example 2: Handle missing values
    # Option 1: Fill missing numerical values with the mean of the column
    df.fillna(df.mean(), inplace=True)
    # Option 2: Fill missing categorical values with the mode of the column
    df.fillna(df.mode().iloc[0], inplace=True)

    # Example 3: Rename columns for consistency (optional)
    df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)

    # Example 4: Convert data types (optional)
    # Ensure a column is of type integer
    df['some_column'] = df['some_column'].astype(int)

    # Example 5: Create new columns (optional)
    # For example, creating a 'year' column from a 'date' column
    if 'date_column' in df.columns:
        df['year'] = pd.to_datetime(df['date_column']).dt.year

    # Example 6: Filter data (optional)
    # For example, only keeping rows where a value is greater than a threshold
    df = df[df['some_column'] > 0]

    # Example 7: Reset index (optional)
    df.reset_index(drop=True, inplace=True)

    return df

if __name__ == "__main__":
    # Example usage: Load data, transform it, and show the result
    try:
        # Assuming `data` is the DataFrame extracted in `extract.py`
        # You would call `extract.py` first, and then pass the result here
        data = pd.read_csv('data/raw/your_data.csv')  # Example, ideally import from extract.py
        transformed_data = transform_data(data)
        
        print(f"Transformed Data:\n{transformed_data.head()}")
    except Exception as e:
        print(f"Error: {e}")
