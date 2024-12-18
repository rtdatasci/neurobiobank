from fastapi.testclient import TestClient
from main import app  # Replace with the correct path if needed

client = TestClient(app)

def test_get_reports():
    # Test the GET /reports/ endpoint
    response = client.get("/reports/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_report():
    # Test the POST /add_report/ endpoint
    new_report = {
        "condition_name": "Alzheimer's Disease",
        "symptom_name": "Memory loss"
    }
    response = client.post("/add_report/", json=new_report)
    assert response.status_code == 200
    assert response.json() == {"message": "Report added successfully!"}
