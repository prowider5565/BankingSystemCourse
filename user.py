import sqlite3

class User:
    def __init__(self, role, passport_id, pincode, full_name,bank_name):
        self.role = role
        self.full_name = full_name
        self.passport_id = passport_id
        self.pincode = pincode
        self.bank_name = bank_name
        self.balance = 0
        self.cards = []

    def __str__(self):
        return (
            f"User({self.full_name}, Role: {self.role}, "
            f"Passport ID: {self.passport_id}, "
            f"Balance: {self.balance}, Cards: {len(self.cards)})"
        )


    def users_create(self):
        with sqlite3.connect("users.sqlite3") as conn:
            db = conn.cursor()
            db.execute(
                """
                INSERT INTO users (full_name,passport_id, pincode, role, bank_name)
                VALUES (?,?,?,?,?)
                """,
                (self.full_name, self.passport_id, self.pincode, self.role,self.bank_name)
            )
            conn.commit()
        print("User added successfully!")

    def get_balance(self):
        return self.balance
