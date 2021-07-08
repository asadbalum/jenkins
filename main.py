
class user:
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age

    def hi(self):
        return 'hello '+ self.name

    def tenY(self):
        return self.age + 10