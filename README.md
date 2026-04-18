# 🏡 PropertyHub

Full-stack web application for managing properties, reviews, and images.  
Built with a Flask backend and React frontend.

---

## 🚀 Features

- 🔐 User authentication (signup, login, logout)
- 🏠 Property management (create, view, delete)
- 🖼 Image uploads for properties
- ⭐ Reviews system with ratings and comments
- 🌙 Dark mode support (React Context)
- 🔄 Full CRUD operations
- 🔗 REST API integration
- 📡 Frontend routing with React Router

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-RESTful
- Faker (for seeding data)

### Frontend
- React
- React Router DOM
- Context API

### Database
- SQLite (development)

---

## 📁 Project Structure

PropertyHub/
│
├── client/                # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── server/                # Flask backend
│   ├── app.py
│   ├── models.py
│   ├── config.py
│   ├── seed.py
│   └── instance/
│
├── Pipfile
├── Pipfile.lock
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/yourusername/propertyhub.git
cd propertyhub

---

### 2. Backend Setup

cd server
pipenv install
pipenv shell

#### Run migrations & seed database

flask db upgrade
python seed.py

#### Start server

python app.py

Server runs on:
http://localhost:5555

---

### 3. Frontend Setup

cd client
npm install
npm start

Frontend runs on:
http://localhost:3000

---

## 🔗 API Endpoints

### Auth
- POST /signup
- POST /login
- DELETE /logout
- GET /check_session

### Properties
- GET /properties
- POST /properties
- DELETE /properties/:id

### Reviews
- GET /reviews
- POST /reviews
- PATCH /reviews/:id
- DELETE /reviews/:id

### Images
- GET /images
- POST /images
- DELETE /images/:id

---

## 🧪 Development Notes

- Uses session-based authentication
- Admin role required for some actions (e.g., deleting properties/images)
- Ensure backend is running before starting frontend
- Proxy should be set in client/package.json:

"proxy": "http://localhost:5555"

---

## 📌 Future Improvements

- Email notifications
- Role-based UI (Admin vs User)
- Image upload (instead of URLs)
- Pagination & search
- Deployment (Render / Vercel)
- Better error handling

---

## 👨‍💻 Author

Artem Roshchupkin  
GitHub: https://github.com/ArtRosh  
LinkedIn: https://www.linkedin.com/in/artem-roshchupkin-34a882354

---

## 📄 License

MIT License