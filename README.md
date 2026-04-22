# 📊 ERP Report & Alert Dashboard

A Django-powered web portal for automating ERP data reporting, KPI visualization, and business alert notifications. Built for data analysts and ERP consultants who need clean, actionable insights beyond what standard ERP systems provide.

---

## 🚀 Features

- **📁 Data Upload** — Import CSV/Excel exports from ERP systems (Hansa, Odoo, SAP, etc.)
- **📊 KPI Dashboard** — Visual cards and charts for revenue, expenses, and balance trends
- **📄 Automated Reports** — Generate and download PDF & Excel reports on demand
- **🔔 Smart Alerts** — Set threshold-based triggers (e.g. overdue invoices, high expenses) with email notifications
- **👤 User Authentication** — Secure login, registration, and role-based access
- **📅 Scheduled Tasks** — Auto-send reports and alerts via Celery background jobs

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11, Django 4.x |
| Database | PostgreSQL (production), SQLite (development) |
| Task Queue | Celery + Redis |
| PDF Generation | WeasyPrint |
| Excel Export | openpyxl |
| Data Processing | pandas |
| Charts | Chart.js |
| Frontend | HTML5, Bootstrap 5 |
| Environment | python-decouple |

---

## 📁 Project Structure

```
erp_dashboard/
│
├── erp_dashboard/           # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── dashboard/               # KPI cards & chart views
├── reports/                 # PDF & Excel report generation
├── alerts/                  # Notification rules & email triggers
├── uploads/                 # CSV/Excel file upload & parsing
├── users/                   # Authentication & user management
│
├── requirements.txt
├── .env.example
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
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
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
```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
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

## 📦 Installation Requirements

```
django
pandas
openpyxl
weasyprint
celery
redis
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
- [ ] **Phase 1** — Data upload & table display
- [ ] **Phase 2** — KPI dashboard with Chart.js visualizations
- [ ] **Phase 3** — PDF & Excel report generation
- [ ] **Phase 4** — Alert rules & email notification system
- [ ] **Phase 5** — Celery scheduled reports

---

## 🔐 Security Notes

- Never commit your `.env` file — it is listed in `.gitignore`
- Use environment variables for all secrets and credentials
- See `.env.example` for required variables

---

## 👩‍💻 Author

**Doreen Njagi**
Odoo Consultant & Data Analyst
- GitHub: [@doreennjagi](https://github.com/doreennjagi)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
