#  Internship Tracker

A Flask-based web application to manage internship applications with **automatic Gmail synchronization**. The application allows users to track internship statuses manually or update them automatically by scanning recruitment emails from Gmail.

---

## Features

- ✅ Add internship applications
- ✅ Edit existing applications
- ✅ Delete applications
- ✅ Track application status
  - Applied
  - Interview
  - Selected
  - Rejected
- ✅ Dashboard showing application statistics
- ✅ Gmail API Integration
- ✅ Automatic email scanning
- ✅ Keyword-based status detection
- ✅ Status history tracking
- ✅ SQLite database
- ✅ Responsive Bootstrap UI

---

##  Tech Stack

### Frontend
- HTML
- CSS
- Bootstrap 5

### Backend
- Python
- Flask

### Database
- SQLite

### APIs
- Gmail API
- Google OAuth 2.0

### Libraries
- google-api-python-client
- google-auth
- google-auth-oauthlib
- BeautifulSoup4

---

##  Project Structure

```
Internship-Tracker/
│
├── app.py
├── scheduler.py
├── internships.db
├── requirements.txt
│
├── credentials/
│   └── credentials.json
│
├── services/
│   ├── gmail_service.py
│   ├── email_reader.py
│   ├── keyword_matcher.py
│   ├── company_extractor.py
│   └── db_updater.py
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sristiii17/internship-tracker-flask

cd Internship-Tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gmail API

1. Create a project in Google Cloud Console.
2. Enable Gmail API.
3. Create OAuth Client credentials.
4. Download `credentials.json`.
5. Place it inside:

```
credentials/
```

### 5. Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📧 Gmail Synchronization

Click the **Sync Gmail** button to:

- Read recent Gmail messages
- Extract company information
- Detect application status using keywords
- Update the database automatically

Supported status detection:

- Applied
- Interview
- Selected
- Rejected

---

## 💾 Database Schema

### applications

| Column | Description |
|---------|-------------|
| id | Primary Key |
| company | Company Name |
| role | Job Role |
| status | Current Status |
| email_subject | Last matched email |
| last_updated | Last update timestamp |
| updated_by | Manual / Gmail Automation |

---

### status_history

Stores every status change with timestamp for tracking application progress.

---

##  Screenshot


<img width="959" height="419" alt="image" src="https://github.com/user-attachments/assets/b11e94c1-bd26-40e1-9ef8-6e57e2e14898" />


##  Future Improvements

- AI-powered email classification
- Company logo integration
- Email notifications
- Search and filter applications
- Dark mode
- Charts and analytics
- Multi-user authentication

---

## 👩‍💻 Author

**Sristi Sharma**

Computer Engineering Student

GitHub: https://github.com/sristiii17

LinkedIn: https://linkedin.com/in/sristi-sharma-506862325/

---

## ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.
