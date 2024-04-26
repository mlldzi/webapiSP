from flask import Flask
from controllers.authentication_controller import authentication_controller
from controllers.user_controller import user_controller
from controllers.company_controller import company_controller

app = Flask(__name__)

app.register_blueprint(authentication_controller)
app.register_blueprint(user_controller)
app.register_blueprint(company_controller)

if __name__ == '__main__':
    app.run()
