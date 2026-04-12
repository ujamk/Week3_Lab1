cat > smart_ambulance_login.py <<'PY'
# Smart Ambulance Login System
# commit test line

# Smart Ambulance Login System

import sqlite3
import hashlib

DB_NAME = "smart_ambulance_users.db"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def main():
    create_database()
    print("Smart Ambulance Login System")

if __name__ == "__main__":
    main()
PY