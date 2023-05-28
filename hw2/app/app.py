from flask import Flask
from calculate_average import calculate_average_route
from generate_password import generate_password_route

app = Flask(__name__)

app.register_blueprint(calculate_average_route)
app.register_blueprint(generate_password_route)

if __name__ == '__main__':
    app.run()