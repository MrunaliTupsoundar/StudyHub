#venv\Scripts\activate
#deactivate

from flask import Flask, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3, os
from dotenv import load_dotenv

# Load env
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
SECRET_KEY = os.getenv("SECRET_KEY", "devsecret")
DB_FILE = os.getenv("DB_FILE", "users.db")

frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
app = Flask(__name__, static_folder=frontend_path, static_url_path="")
app.secret_key = SECRET_KEY

DB_PATH = os.path.join(os.path.dirname(__file__), DB_FILE)

def get_db_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_PATH):
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
        """)
        conn.commit()
        conn.close()

@app.route("/api/register", methods=["POST"])
def api_register():
    username = request.form.get("username","").strip()
    email = request.form.get("email","").strip()
    password = request.form.get("password","")
    if not username or not email or not password:
        return jsonify({"success":False,"error":"Username, email and password required"}), 400
    pw_hash = generate_password_hash(password)
    import datetime
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username,email,password_hash,created_at) VALUES (?, ?, ?, ?)",
                    (username, email, pw_hash, datetime.datetime.utcnow().isoformat()))
        conn.commit()
        conn.close()
        return jsonify({"success":True,"message":"Registered"}), 200
    except Exception as e:
        err = str(e)
        if "UNIQUE constraint failed: users.username" in err:
            return jsonify({"success":False,"error":"Username already exists"}), 400
        if "UNIQUE constraint failed: users.email" in err:
            return jsonify({"success":False,"error":"Email already exists"}), 400
        return jsonify({"success":False,"error":err}), 500

@app.route("/api/login", methods=["POST"])
def api_login():
    username = request.form.get("username","").strip()
    password = request.form.get("password","")
    if not username or not password:
        return jsonify({"success":False,"error":"Username and password required"}), 400
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, username))
    row = cur.fetchone()
    conn.close()
    if row is None:
        return jsonify({"success":False,"error":"User not found"}), 400
    if not check_password_hash(row["password_hash"], password):
        return jsonify({"success":False,"error":"Incorrect password"}), 400
    session["user_id"] = row["id"]
    session["username"] = row["username"]
    return jsonify({"success":True,"redirect": "/studyhub_og/index.html"}), 200

@app.route("/api/logout", methods=["GET"])
def api_logout():
    session.pop("user_id", None)
    session.pop("username", None)
    return jsonify({"success":True}), 200

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
