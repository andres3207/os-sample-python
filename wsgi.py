from flask import Flask
application = Flask(__name__)

@application.route("/asd")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
