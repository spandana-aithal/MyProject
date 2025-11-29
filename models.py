import threading

class InMemoryDB:
    def __init__(self):
        self._lock = threading.Lock()
        self._patients = {}
        self._doctors = {}
        self._appointments = {}
        self._next_patient = 1
        self._next_doctor = 1
        self._next_appointment = 1

    def create_patient(self, name, contact, dob=None):
        with self._lock:
            pid = f"P{self._next_patient:04d}"
            self._next_patient += 1
            patient = {"patient_id": pid, "name": name, "contact": contact, "dob": dob}
            self._patients[pid] = patient
            return patient

    def get_patient(self, patient_id):
        return self._patients.get(patient_id)

    def create_doctor(self, name, specialization=None):
        with self._lock:
            did = f"D{self._next_doctor:03d}"
            self._next_doctor += 1
            doctor = {"doctor_id": did, "name": name, "specialization": specialization}
            self._doctors[did] = doctor
            return doctor

    def create_appointment(self, patient_id, doctor_id, appointment_datetime):
        # validate ids
        if patient_id not in self._patients or doctor_id not in self._doctors:
            return None
        with self._lock:
            aid = f"A{self._next_appointment:05d}"
            self._next_appointment += 1
            appt = {"appointment_id": aid, "patient_id": patient_id, "doctor_id": doctor_id, "appointment_datetime": appointment_datetime, "status": "scheduled"}
            self._appointments[aid] = appt
            return appt