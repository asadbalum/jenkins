from flask import Flask

app = Flask(__name__)

class user:
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age

    def hi(self):
        return 'hello '+ self.name

    def tenY(self):
        return self.age + 10


@app.route('/')
def home():
    agent = user('Asad','',25)
    return '<b>Hello '+ agent.name + '</b>'

if __name__=='__main__':
    app.run(debug=True)