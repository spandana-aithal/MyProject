# Hospital Management System — Project Plan (CS162–CS168)

## Project Overview
**Project:** Hospital Management System (HMS)  
**Team:** CS162–CS168 — Replace with actual member names and roles.  
**Short description:** HMS automates patient registration, appointment scheduling, doctor management, billing, and record keeping for a hospital. The goal is to reduce paperwork, improve accuracy, and speed up patient throughput.

## Objectives
- Reduce manual paperwork and data duplication.
- Provide fast patient registration and search.
- Automate appointment scheduling and reminders.
- Manage doctor availability and clinics.
- Produce bills and discharge summaries.

## Scope
**In-scope**
- Patient registration and search
- Appointment booking and cancellation
- Doctor CRUD and availability
- Billing & payment recording
- Basic reports (daily appointments, discharges)

**Out-of-scope**
- Pharmacy management
- Ambulance tracking
- Mobile application (phase 2)

## Functional Requirements
- FR1: Register a new patient (name, DOB, contact, address).
- FR2: Search patient by ID/name.
- FR3: Book / cancel / reschedule appointments.
- FR4: Add/edit doctor information and availability.
- FR5: Record diagnosis and treatment in patient history.
- FR6: Generate bills and receipts.

## Non-functional Requirements
- NFR1: Demo system should respond in <2s for basic endpoints.
- NFR2: Data stored in a relational DB (Postgres/MySQL) for production.
- NFR3: Use secure transport (HTTPS) in production.

## Milestones & Timeline
- Week 1: Requirements & Design
- Week 2: Core Implementation (Patients, Doctors, Appointments)
- Week 3: Billing, Reports & Testing
- Week 4: Finalize Documentation & Submission

## Design Artifacts
- ER Diagram: upload `docs/ERD.png`
- DB Schema: upload `db/schema.sql`
- API Endpoints: documented in README and Confluence pages

## Effort Estimation (summary)
Total estimated hours: **238 hours**
Costs at different rates:
- $5/hr → $1190
- $10/hr → $2380
- $20/hr → $4760

## Test Plan
- Manual test cases for patient creation, appointment booking, billing generation.
- Automated smoke tests example in `tests/`

## Deliverables
- Confluence pages (this content)
- Jira board (import `jira/jira_issues.csv`)
- GitHub repo (push `src/`, `db/`, `docs/`)
- Final report (see `final_report/Final_Report.md`)