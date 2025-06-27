import json
from user import User


class CommandController:
    def __init__(self, command):
        self.command = command


class RegisterController(CommandController):
    def __init__(self, command):
        self.labels = {
            "first_name": "Ismingizni kiriting: ",
            "last_name": "Familiyangizni kiriting: ",
            "age": "Yoshingizni kiriting: ",
            "email": "Emailingizni kiriting: ",
            "passport_id": "Pasport id inizni kiriting: ",
            "password": "Parolingizni kiriting: ",
        }
        super().__init__(command)

    def register(self):
        userDetails = {}
        fields = list(self.labels.keys())

        for field in fields:
            value = input(self.labels[field])
            if field == "age":
                value = int(value)
            userDetails[field] = value

        user = User(
            role="customer",  # or assign dynamically if needed
            first_name=userDetails["first_name"],
            last_name=userDetails["last_name"],
            age=userDetails["age"],
            passport_id=userDetails["passport_id"],
            password=userDetails["password"],
            email=userDetails["email"],
        )

        # Prepare user data for JSON serialization (excluding password optionally)
        user_data = {
            "role": user.role,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "passport_id": user.passport_id,
            "email": user.email,
            "balance": user.balance,
            "cards": user.cards,
        }

        # Append to JSON file
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(user_data)

        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Foydalanuvchi muvaffaqiyatli qo‘shildi.")
