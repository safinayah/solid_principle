class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_details(self):
        return f'Name: {self.name}, Email: {self.email}'

    def update_email(self, new_email):
        self.email = new_email

class EmailService:
    @staticmethod
    def send_email(email, message):
        # A simple print to simulate sending an email
        print(f'Sending email to {email}: {message}')

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_all_user_details(self):
        return [user.get_details() for user in self.users]

    def update_user_email(self, name, new_email):
        for user in self.users:
            if user.name == name:
                user.update_email(new_email)

# Initializing UserManager and adding users
user_manager = UserManager()
user_manager.add_user(User('John Doe', 'john@example.com'))
user_manager.add_user(User('Jane Doe', 'jane@example.com'))
