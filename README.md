# 📝 Flask To-Do App

A simple yet functional **To-Do List Web Application** built using **Flask** for the backend and vanilla HTML/CSS/JavaScript for the frontend. This app allows users to **Sign Up**, **Log In**, and **manage their tasks** efficiently with full CRUD (Create, Read, Update, Delete) capabilities.

## 🚀 Features

- 🔐 **User Authentication**: Sign up and log in functionality using Flask sessions.
- ✅ **Add Task**: Users can add new to-do tasks.
- ✏️ **Update Task**: Edit task content directly from the UI.
- 🗑️ **Delete Task**: Remove tasks permanently.
- 📋 **Persistent Task Storage**: Tasks are saved per user.
- 💻 **Frontend in One File**: HTML, CSS, and JavaScript are embedded in `index.html` for simplicity.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript (inline in `index.html`)
- **Database**: SQLite (default for Flask apps)

## 📂 Project Structure

flask-to-do-app/
│
├── app.py # Main Flask app
├── templates/
│ └── index.html # Single-page app with embedded CSS/JS
├── static/
│ └── style.css # (Optional) If you decide to externalize CSS
├── models.py # (Optional) Task/User models
├── database.db # SQLite database (auto-created)
├── requirements.txt # Python dependencies
└── README.md # Project documentation



## ▶️ Getting Started

### 1. Clone the Repository


git clone https://github.com/yourusername/flask-to-do-app.git
cd flask-to-do-app

2. Create a Virtual Environment (Optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application
python app.py

The app will run on http://127.0.0.1:5000/.

✅ Usage
Visit the homepage and sign up for a new account.

Once logged in, you can:

Add new tasks

Edit existing tasks

Delete tasks

All changes will be reflected in real-time, thanks to embedded JavaScript.

🧾 Dependencies
Listed in requirements.txt:

Flask

Flask-Login

SQLite3 (built-in with Python)

To generate it manually:

bash
Copy
Edit
pip freeze > requirements.txt
📌 Notes
Make sure SECRET_KEY is set in your app.py for session management.

If using this in production, consider using a more robust database like PostgreSQL.

📸 Screenshot
(Add a screenshot of your app here if available)

🧑‍💻 Author
Your Name
GitHub

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

yaml
Copy
Edit

---

Let me know if you’d like help generating the actual `app.py`, `index.html`, or database schema too.




   

