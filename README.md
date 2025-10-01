# Customer Support Ticketing System

A **Django backend project** for managing customer support tickets. Users can register, create tickets, and track their status, while agents can manage and assign tickets. The project exposes **RESTful APIs** and uses **JWT authentication** for secure access.  

---

## Tech Stack

- **Backend:** Python, Django, Django REST Framework (DRF)  
- **Authentication:** JWT (`djangorestframework-simplejwt`)  
- **Database:** SQLite (local/demo) or PostgreSQL (production)  
- **Task Queue:** Celery  
- **Server:** Gunicorn  
- **Deployment:** Render  
- **Version Control:** Git / GitHub  
- **Containerization:** Docker  

---

## Features

- User registration and login with JWT authentication  
- Ticket creation, assignment, and status tracking  
- Role-based access for agents and customers  
- REST API endpoints for all functionalities  
- Browser-friendly landing page with links to API endpoints  

---

## API Endpoints (Sample)

- `POST /api/auth/token/` – Obtain JWT access and refresh tokens  
- `POST /api/auth/token/refresh/` – Refresh access token  
- `GET /api/auth/me/` – Get logged-in user profile  
- `GET /api/tickets/` – List all tickets (authenticated)  
- `POST /api/tickets/` – Create a new ticket  
- `GET /api/tickets/{id}/` – Get ticket details  
- `PUT /api/tickets/{id}/` – Update ticket  
- `DELETE /api/tickets/{id}/` – Delete ticket
