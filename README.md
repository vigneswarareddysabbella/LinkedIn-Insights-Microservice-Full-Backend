# LinkedIn Insights Microservice

A backend microservice that fetches, stores, and serves insights of LinkedIn Company Pages using a given **Page ID**.  
Built as part of a **GenAI Developer Intern Assignment**, following clean architecture, REST principles, and scalable backend practices.

---

## 🚀 Features

### Mandatory Features
- Fetch LinkedIn Page details using **Page ID**
- Scrape LinkedIn company pages (Playwright-based)
- Store data persistently in a database (SQLite for demo)
- REST APIs built using **FastAPI**
- Auto-fetch data if not present in DB
- Clean separation of concerns (API, Service, Model layers)
- Ready-to-test APIs with Swagger UI

### Data Collected
- Page ID
- Page Name
- Page URL
- Followers count
- Description (optional)
- Posts (structure ready for extension)

---

## 🛠 Tech Stack

- **Python 3.10+**
- **FastAPI** – REST API framework
- **SQLAlchemy** – ORM
- **Playwright** – Web scraping
- **SQLite** – Database (easy local demo)
- **Uvicorn** – ASGI server

---

## 📁 Project Structure

app/
├── main.py
├── core/
│ └── database.py
├── models/
│ ├── base.py
│ ├── page.py
│ └── post.py
├── services/
│ ├── scraper.py
│ └── linkedin_service.py
└── api/
└── v1/
├── router.py
└── endpoints/
└── page.py


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/linkedin-insights.git
cd linkedin-insights
