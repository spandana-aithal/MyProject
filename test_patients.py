import requests
BASE='http://localhost:5000'

def test_create_patient():
    r = requests.post(BASE + '/patients', json={"name":"Test Patient","contact":"9999999999"})
    assert r.status_code == 201
    data = r.json()
    assert "patient_id" in data

def test_get_patient_not_found():
    r = requests.get(BASE + '/patients/P9999')
    assert r.status_code == 404