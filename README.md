# Hospital Management System (HMS)
This package contains a complete, ready-to-upload solution for the **Hospital Management System (HMS)**
assignment for CS162–CS168.

## What's included (ready-to-upload)
- Confluence page text (copy/paste): `confluence/Confluence_Pages.md`
- Jira CSV for bulk import (epics, stories, tasks, bugs): `jira/jira_issues.csv`
- GitHub-ready project skeleton and code: `src/` (Flask demo server), `db/schema.sql`
- Automated test example: `tests/test_patients.py`
- ER diagram (PNG): `docs/ERD.png`
- Effort estimation spreadsheet: `effort/effort_estimation.xlsx`
- Final report draft: `final_report/Final_Report.md`

## How to use
1. Import `jira/jira_issues.csv` into your Jira project (Jira -> Issues -> Import issues from CSV). Use project key `HMS` or change CSV before import.
2. Create a Confluence space and paste contents of `confluence/Confluence_Pages.md` into pages.
3. Create a GitHub repository and push everything in this folder to it. The `src/` folder contains a simple Flask demo server you can run locally.
4. Run the demo server:
   ```bash
   cd src
   pip install -r requirements.txt
   python server.py
   ```
5. Run tests (optional):
   ```bash
   pip install -r requirements.txt pytest requests
   pytest -q
   ```

## License
This package is provided to help you complete the assignment. Edit names and team members before submission.