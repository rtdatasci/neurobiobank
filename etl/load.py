import psycopg2
from psycopg2 import sql
import pandas as pd
import os

# Define connection parameters
DB_HOST = os.getenv('DB_HOST', 'localhost')  # Your host
DB_PORT = os.getenv('DB_PORT', '5432')  # Default port for PostgreSQL
DB_NAME = os.getenv('DB_NAME', 'your_database')
DB_USER = os.getenv('DB_USER', 'your_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'your_password')

def create_table_if_not_exists(cursor):
    """
    Creates the table if it does not exist.
    
    Args:
    - cursor: The PostgreSQL database cursor.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS your_table (
        id SERIAL PRIMARY KEY,
        column1 VARCHAR(255),
        column2 INT,
        column3 DATE,
        year INT,
        -- Add other columns based on your DataFrame
    );
    """
    cursor.execute(create_table_query)

def load_data_to_postgresql(df):
    """
    Loads the transformed data into PostgreSQL.
    
    Args:
    - df (pandas.DataFrame): The transformed data.
    """
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()

        # Create table if it doesn't exist
        create_table_if_not_exists(cursor)

        # Insert data into the table
        insert_query = """
        INSERT INTO your_table (column1, column2, column3, year)
        VALUES (%s, %s, %s, %s);
        """
        
        # Loop through DataFrame and insert each row
        for index, row in df.iterrows():
            cursor.execute(insert_query, (row['column1'], row['column2'], row['column3'], row['year']))

        # Commit the transaction
        connection.commit()

        print(f"Successfully loaded {len(df)} rows into the PostgreSQL database.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    try:
        # Read transformed data (you can load the data from `transform.py`)
        data = pd.read_csv('data/transformed/your_transformed_data.csv')  # Example: After transformation
        load_data_to_postgresql(data)

    except Exception as e:
        print(f"Error: {e}")
