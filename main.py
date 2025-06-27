import sqlite3
from database import create_bank_table,create_users_table
from user import User
from bank import Bank



commands = ["register", "balance", "create_card", "quit", "create_bank"]
user = None  # global user object
admin_password = "admin"
print(f"Mavjud buyruqlar:  {commands}")


def mainloop():
    while True:
        inp = input("Buyruq kiriting: ").lower()
        if inp == "register":
            bank_count = Bank.get_banks_count()
            if bank_count == 0:
                print("Banklar mavjud emas. Iltimos, avval bank yarating.")
                continue
            bank_names = Bank.list_bank_names()
            print(bank_names)
            bank_name = input("Bank nomini tanlang: ")
            bank = Bank.get_bank_by_title(bank_name)
            full_name = input("Ism-familiyangizni kiriting: ")
            passport_id = input("Passport IDingizni kiriting: ")
            pincode = input("Pinkod kiriting: ")
            users = User(role="Customer",passport_id=passport_id,pincode=pincode,full_name=full_name,bank_name=bank_name)
            users.users_create()
        elif inp == "create_bank":
            title = input("Bank nomini kiriting: ")
            description = input("Bank haqida qisqacha ma'lumot: ")
            address = input("Bank manzilini kiriting: ")
            bank = Bank(title=title, description=description, address=address)
            bank.create()
        elif inp == "admin":
            pp = input("Parol: ")
            if pp == "admin":
                print("Welcome to admin panel")
                while True:
                    commands = ["users","bank_users","id_search","quit"]
                    print(commands)
                    command = input("Buyruqni kiriting: ")
                    if command == "users":
                        print("Users: ")
                        with sqlite3.connect("users.sqlite3") as conn:
                            db = conn.cursor()
                            db.execute("SELECT id, full_name, passport_id, pincode, bank_name, role FROM users")
                            users = db.fetchall()

                            if not users:
                                print("Hozircha foydalanuvchilar yo‘q.")
                            else:
                                for user in users:
                                    id, full_name, passport_id, pincode, bank_name, role = user
                                    print(f"ID: {id}, Ism: {full_name}, Passport: {passport_id}, Pin: {pincode}, Bank: {bank_name}, Rol: {role}")
            
                    elif command == "bank_users":
                        bank_name = input("Qaysi bank foydalanuvchilarini ko‘rmoqchisiz? ")
                        with sqlite3.connect("users.sqlite3") as conn:
                            db = conn.cursor()
                            db.execute("""
                                SELECT id, full_name, passport_id, pincode, bank_name, role
                                FROM users
                                WHERE bank_name = ?
                            """, (bank_name,))
                            users = db.fetchall()

                        if users:
                            for user in users:
                                print(f"ID: {id}, Ism: {full_name}, Passport: {passport_id}, Pin: {pincode}, Bank: {bank_name}, Rol: {role}")
                        else:
                            print("Ushbu bank foydalanuvchilari topilmadi.")
                    elif command == "quit":
                        break
                    else:
                        print("Noto‘g‘ri buyruq. Iltimos, qaytadan urinib ko‘ring.")
                    
        elif inp == "quit":
            print("Dastur tugatildi.")
            break
        elif inp not in commands:
            print("Noto'g'ri buyruq. Iltimos, qayta urinib ko'ring.")
            continue


if __name__ == "__main__":
    create_bank_table()
    create_users_table()
    mainloop()
