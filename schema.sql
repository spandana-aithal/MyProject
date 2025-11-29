-- Simple schema for Hospital Management System (HMS)
CREATE TABLE patients (
  patient_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  dob DATE,
  contact VARCHAR(15),
  address TEXT
);

CREATE TABLE doctors (
  doctor_id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  specialization VARCHAR(100),
  contact VARCHAR(15)
);

CREATE TABLE appointments (
  appointment_id SERIAL PRIMARY KEY,
  patient_id INT REFERENCES patients(patient_id),
  doctor_id INT REFERENCES doctors(doctor_id),
  appointment_datetime TIMESTAMP,
  status VARCHAR(20)
);

CREATE TABLE bills (
  bill_id SERIAL PRIMARY KEY,
  patient_id INT REFERENCES patients(patient_id),
  amount NUMERIC(10,2),
  bill_date DATE,
  status VARCHAR(20)
);