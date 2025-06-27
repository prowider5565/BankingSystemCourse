import sqlite3
from status import FAILURE, INVALID_LABEL, SUCCESSFUL
from user import User
import random
import uuid


banks = []


class Bank:
    def __init__(self, title: str = None, description: str = None, address : str = None):
        self.title = title
        self.description = description
        self.address = address
        self.uuid = uuid.uuid4()
        self.cards = []
        self.users = []
        self.workers = []

    @staticmethod
    def get_bank_by_title(title: str):
        for bank in banks:
            if bank.title == title:
                return bank

    @staticmethod
    def list_bank_names():
        with sqlite3.connect("db.sqlite3") as conn:
            db = conn.cursor()
            db.execute(
                """
                SELECT title FROM bank
                """
            )
            rows = db.fetchall()
            return "".join(f"{row[0]}\n" for row in rows)

    def create_card(self):
        num = [8, 6, 0, 0] + [random.randint(0, 9) for _ in range(11)]
        total = sum(
            (n if i % 2 else (n * 2 - 9 if n * 2 > 9 else n * 2))
            for i, n in enumerate(num[::-1])
        )
        num.append((10 - total % 10) % 10)
        self.cards.append("".join(map(str, num)))
        return "Seccsessfull created"

    def create(self):
        with sqlite3.connect("db.sqlite3") as conn:
            db = conn.cursor()
            db.execute(
                """
                INSERT INTO bank (title, description, address, uuid)
                VALUES (?, ?, ?, ?)
                """,
                (self.title, self.description, self.address, str(self.uuid)),
            )
            conn.commit()
        print("Bank added successfully!")


    def get_bank(self):
        with sqlite3.connect("db.sqlite3") as conn:
            db = conn.cursor()
            db.execute(
                """
                SELECT title, description, address, uuid FROM bank WHERE uuid = ?
                """,
                (str(self.bank_uuid),),
            )
            row = db.fetchone()
            if row:
                bank = Bank(title=row[0], description=row[1], address=row[2])
                bank.uuid = uuid.UUID(row[3])
                return bank
            return None

    @staticmethod
    def get_all_banks():
        with sqlite3.connect("db.sqlite3") as conn:
            db = conn.cursor()
            db.execute(
                """
                SELECT title, description, address, uuid FROM bank
                """
            )
            rows = db.fetchall()
            banks_list = []
            for row in rows:
                bank = Bank(title=row[0], description=row[1], address=row[2])
                bank.uuid = uuid.UUID(row[3])
                banks_list.append(bank)
            return banks_list

    @staticmethod
    def get_banks_count():
        with sqlite3.connect("db.sqlite3") as conn:
            db = conn.cursor()
            db.execute(
                """
                SELECT COUNT(*) FROM bank
                """
            )
            count = db.fetchone()[0]
            return count
