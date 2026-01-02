# 🧑‍💼 Recruitment System (Full Stack Flask App)

This is a full stack recruitment system built using **Flask** and **MongoDB Atlas**. It allows candidates to register and apply for jobs, while recruiters can post job listings and manage applications.

---

## 🚀 Features

- 👤 User Registration & Login
- 📝 Job Posting (Recruiter)
- 📄 Job Application (Candidate)
- 🔐 Secure Authentication (Sessions)
- 🌐 MongoDB Atlas Integration
- 🎨 HTML, CSS (via Jinja templates)

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Database**: MongoDB Atlas
- **Deployment**:
  - Backend: Render
  - (Optional) Frontend: Netlify (if separate)

---

## 📁 Project Structure


---

## ⚙️ Installation & Running Locally

1. **Clone the repo**  
   `git clone https://github.com/dkesavapriya/recruitment-system.git`

2. **Install dependencies**  
   `pip install -r requirements.txt`

3. **Create `.env` file**

MONGO_URI=your_mongodb_uri
SECRET_KEY=your_secret_key
'ADMIN_USERNAME'
'ADMIN_PASSWORD'


4. **Run the app**  
   `python app.py`

---

## 🌍 Live Demo (After Deployment)

- 🔗 [[Live App (Render)]](https://flask-recruitment-system.onrender.com)
- 💻 GitHub: [Project Link](https://github.com/dkesavapriya/recruitment-system)

---

## 📦 Deployment

### 🧩 On Render (Backend)
1. Create new **Web Service** on [https://render.com](https://render.com)
2. Connect your GitHub repo
3. Set:
   - Build Command: *(leave empty)*
   - Start Command: `gunicorn app:app`
4. Add **Environment Variables**:
   - `MONGO_URI`
   - `SECRET_KEY`
   - 'ADMIN_USERNAME'
   - 'ADMIN_PASSWORD'
5. Deploy and grab the live link!

---


---
