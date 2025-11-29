from flask import Flask, request, jsonify
from models import InMemoryDB

app = Flask(__name__)
db = InMemoryDB()

@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.json or {}
    name = data.get('name')
    contact = data.get('contact')
    dob = data.get('dob')
    if not name or not contact:
        return jsonify({"error":"name and contact required"}), 400
    patient = db.create_patient(name=name, contact=contact, dob=dob)
    return jsonify(patient), 201

@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    p = db.get_patient(patient_id)
    if not p:
        return jsonify({"error":"not found"}), 404
    return jsonify(p), 200

@app.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.json or {}
    name = data.get('name')
    spec = data.get('specialization')
    if not name:
        return jsonify({"error":"name required"}), 400
    doc = db.create_doctor(name=name, specialization=spec)
    return jsonify(doc), 201

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json or {}
    patient_id = data.get('patient_id')
    doctor_id = data.get('doctor_id')
    appointment_datetime = data.get('appointment_datetime')
    if not patient_id or not doctor_id or not appointment_datetime:
        return jsonify({"error":"patient_id, doctor_id and appointment_datetime required"}), 400
    appt = db.create_appointment(patient_id, doctor_id, appointment_datetime)
    if appt is None:
        return jsonify({"error":"invalid patient_id or doctor_id"}), 400
    return jsonify(appt), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)