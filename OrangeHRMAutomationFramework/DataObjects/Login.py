class Login:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get_userName(self):
        return self.username

    def set_userName(self, username):
        self.username = username

    def get_passWord(self):
        return self.password

    def set_passWord(self, password):
        self.password = password
