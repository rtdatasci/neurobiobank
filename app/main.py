import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Create a function to handle the database connection
def get_db_connection():
    conn = sqlite3.connect("C:/Users/rajee/OneDrive/Documents/rtdatasci_github/neurobiobank/toy_clinical_data.db")
    conn.row_factory = sqlite3.Row  # Optional, for accessing columns by name
    return conn

# Define a Pydantic model to validate incoming data
class Report(BaseModel):
    condition_name: str
    symptom_name: str

# Route to fetch all reports from the database
@app.get("/reports/")
def get_reports():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports")
    rows = cursor.fetchall()
    conn.close()
    return [{"condition_name": row["condition_name"], "symptom_name": row["symptom_name"]} for row in rows]

# Route to add a new report to the database
@app.post("/add_report/")
def add_report(report: Report):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reports (condition_name, symptom_name) VALUES (?, ?)", 
                   (report.condition_name, report.symptom_name))
    conn.commit()
    conn.close()
    return {"message": "Report added successfully!"}

# # test in bash terminal, cd into app folder first
# uvicorn main:app --reload
# this will redirect or click link to open http://127.0.0.1:8000 
# swagger docs: http://127.0.0.1:8000/docs

