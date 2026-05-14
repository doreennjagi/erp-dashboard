# 📊 ERP Report & Alert Dashboard

> A Django-powered SaaS portal for automating ERP data reporting, KPI visualization, and smart business alert notifications. Built for ERP consultants who resell actionable insights to their clients — beyond what standard ERP systems provide.

---

## 🚀 Live Features

### ✅ Phase 1 — Data Upload & Preview
- Import CSV/Excel exports from any ERP system (Odoo, SAP, Hansa, QuickBooks, etc.)
- Instant data preview (first 50 rows) with searchable table
- Supports multiple file uploads per user

### ✅ Phase 2 — KPI Dashboard & Charts
- **KPI Cards** — Total Income, Total Expenses, Net Balance (color-coded)
- **Bar Chart** — Monthly Income vs Expenses trend
- **Doughnut Chart** — Expense breakdown by category
- Professional sidebar layout with Bootstrap 5

### ✅ Phase 3 — Automated Reports
- Generate and download **PDF reports** on demand (WeasyPrint)
- Generate and download **Excel reports** on demand (openpyxl)

### ✅ Phase 4 — Smart Alerts & Email Notifications
- Set threshold-based alert rules per user (e.g. "Alert me if expenses exceed KES 200,000")
- Alert types: High Expenses, Low Balance, High Income
- Email notifications triggered automatically on CSV upload
- Alert log with full history of triggered events

### ✅ Phase 5 — Scheduled Reports (APScheduler)
- Automatic weekly report emails every Monday at 8:00 AM
- Pulls the user's latest uploaded dataset and sends a summary
- No Celery/Redis required — lightweight APScheduler

### ✅ User Authentication
- Secure login and registration pages
- Session-based authentication
- Redirects unauthenticated users to login

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11, Django 5.1 |
| Database | SQLite (development), PostgreSQL (production) |
| Task Scheduler | APScheduler + django-apscheduler |
| PDF Generation | WeasyPrint |
| Excel Export | openpyxl |
| Data Processing | pandas |
| Charts | Chart.js |
| Frontend | HTML5, Bootstrap 5, Bootstrap Icons |
| Environment | python-decouple |

---

## 📁 Project Structure

```
erp_dashboard/
│
├── erp_dashboard/          # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── scheduler.py        # APScheduler weekly report job
│   └── wsgi.py
│
├── dashboard/              # KPI cards & chart views
├── reports/                # PDF & Excel report generation
├── alerts/                 # Alert rules, triggers & email notifications
│   ├── models.py           # AlertRule, AlertLog
│   ├── views.py            # CRUD + check_alerts()
│   └── templates/
├── uploads/                # CSV/Excel file upload & parsing
│   ├── models.py           # UploadedFile
│   ├── views.py            # upload_file() with alert integration
│   └── templates/
├── users/                  # Authentication & user management
│   ├── views.py            # login, register, logout
│   └── templates/
│
├── requirements.txt
├── .env.example
├── test_data.csv
└── manage.py
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/doreennjagi/erp-dashboard.git
cd erp-dashboard
```

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
cp .env.example .env
# Edit .env with your settings
```

Your `.env` file should include:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 🧪 Test Data

A sample `test_data.csv` is included in the root directory with columns:

```
Date, Description, Amount, Type, Category
```

Upload it at the dashboard to instantly see KPIs, charts, and test alert rules.

---

## 🔔 Setting Up Alerts

1. Go to `/alerts/create/`
2. Choose an alert type (High Expenses, Low Balance, High Income)
3. Set a threshold value in KES
4. Enter the notification email
5. Upload any CSV — alerts trigger automatically and log every event

---

## 📦 Requirements

```
django
pandas
openpyxl
weasyprint
django-apscheduler
apscheduler
python-decouple
psycopg2-binary
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🗺️ Development Roadmap

- [x] Project setup & folder structure
- [x] Phase 1 — Data upload & table display
- [x] Phase 2 — KPI dashboard with Chart.js visualizations
- [x] Phase 3 — PDF & Excel report generation
- [x] Phase 4 — Alert rules & email notification system
- [x] Phase 5 — Scheduled weekly reports (APScheduler)
- [ ] Phase 6 — Multi-company support (each client isolated)
- [ ] Phase 7 — Role-based access (Admin, Manager, Viewer)
- [ ] Phase 8 — Pagination & advanced filters (date, category, type)
- [ ] Phase 9 — Subscription plans (Free / Pro / Enterprise)
- [ ] Phase 10 — Professional landing & pricing page

---

## 🔐 Security Notes

- Never commit your `.env` file — it is listed in `.gitignore`
- Use environment variables for all secrets and credentials
- Change `SECRET_KEY` before deploying to production
- Set `DEBUG=False` in production
- See `.env.example` for required variables

---

## 👩‍💻 Author

**Doreen Njagi**  
Odoo Consultant & Data Analyst

- GitHub: [@doreennjagi](https://github.com/doreennjagi)

---

## 📄 License & Intellectual Property

**Copyright © 2025 Doreen Njagi. All Rights Reserved.**

This software and its source code are the **exclusive intellectual property** of Doreen Njagi.

**You may NOT:**
- Copy, reproduce, or redistribute this software or any part of it
- Use this software or its concepts for commercial purposes without written permission
- Modify, adapt, or build upon this work without explicit written consent
- Sublicense or sell access to this software

**You MAY:**
- View the source code for personal learning purposes only

This project is **not open source**. Viewing this repository does not grant any rights to use, copy, or distribute the code or its underlying concepts.

For licensing, partnership, or commercial use inquiries, contact the author directly via GitHub.

> ⚠️ Unauthorized use of this software is a violation of copyright law and will be pursued accordingly.
