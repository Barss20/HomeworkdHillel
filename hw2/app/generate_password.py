from flask import Blueprint
import random
import string

generate_password_route = Blueprint('generate_password', __name__)

@generate_password_route.route('/generate_password', methods=['GET'])
def generate_password():
    length = random.randint(10, 20)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
