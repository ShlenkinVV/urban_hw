class User:
    def __init__(self, nickname, age, password):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

    def __str__(self):
        return f'nickname: {self.nickname}, age: {self.age}, password: {self.password}'

    def __repr__(self):
        return str(self)

