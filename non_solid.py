class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_details(self):
        return f'Name: {self.name}, Email: {self.email}'

    def send_email(self, message):
        # A simple print to simulate sending an email
        print(f'Sending email to {self.email}: {message}')


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        user = User(name, email)
        self.users.append(user)

    def get_all_user_details(self):
        details = []
        for user in self.users:
            details.append(user.get_details())
        return details

    def send_email_to_all_users(self, message):
        for user in self.users:
            user.send_email(message)


# Initializing UserManager and adding users
user_manager = UserManager()
user_manager.add_user('John Doe', 'john@example.com')
user_manager.add_user('Jane Doe', 'jane@example.com')
