import sqlite3


def create_bank_table():
    with sqlite3.connect("db.sqlite3") as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS bank (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                address TEXT,
                uuid TEXT UNIQUE
            )
            """
        )


def create_users_table():
    with sqlite3.connect("users.sqlite3") as conn:
        db = conn.cursor()
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                passport_id TEXT UNIQUE NOT NULL,
                pincode TEXT UNIQUE NOT NULL,
                role TEXT NOT NULL,
                bank_name TEXT NO NULL
            )
        """)
        conn.commit()