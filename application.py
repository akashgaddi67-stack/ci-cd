from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return "Application Deployed Successfully on AWS"

if __name__ == '__main__':
    application.run(debug=True) 