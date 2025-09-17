
# StudyHub

## Project Structure
backend/
├── app.py               # Flask backend with /register, /login, /logout routes
├── requirements.txt     # Python dependencies
├── .env.example         # Example env vars to configure DB and Flask secret
frontend/
└── ...                  # Original HTML/CSS/assets (unchanged)

## Setup & Run (Development)

1. **Install Python 3.10+** and `pip`.  

2. **Create a virtual environment** and activate it:  

   **Linux/macOS:**  
   ```bash
   python -m venv venv
   source venv/bin/activate

**Windows:**

```cmd
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**:

   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Configure environment variables**:

   * Copy the example file:

     ```bash
     cp backend/.env.example backend/.env
     ```

   * Edit `.env` and set your MySQL credentials and Flask secret:

     ```
     DB_HOST=localhost
     DB_USER=root
     DB_PASSWORD=yourpassword
     DB_NAME=studyhub
     FLASK_SECRET=kJDUFSyhgcdlkijougytjhbmsdkjxhj
     ```

5. **Ensure MySQL server is running** and reachable. The app will automatically create the database and `users` table if they don’t exist.

6. **Run the app**:

   ```bash
   cd backend
   python app.py
   ```

7. **Access the authentication pages**:
   Open your browser and go to:

   ```
   http://127.0.0.1:5000/studyhub_og/register.html
   http://127.0.0.1:5000/studyhub_og/login.html
   ```

## Notes

* If your frontend already has `register.html` and `login.html`, the backend will serve those pages and handle form POSTs to `/register` and `/login`.
* Forms must use `method="post"` and inputs named:

  * `username`
  * `password`
  * (optionally) `email`
* After login, the backend redirects to `index.html` (if present) or `/protected` with a simple message.
* Use `.env` to securely store DB credentials and the Flask secret key.
