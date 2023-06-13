import requests
import csv
from faker import Faker
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')
fake = Faker()

current_currency = 'USD'

def generate_students():
    count = int(request.args.get('count', 1000))
    count = max(1, min(count, 999))
    students = []

    for _ in range(count):
        student = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(length=8),
            'birthday': fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%Y-%m-%d')
        }
        students.append(student)

    save_students_to_csv(students)
    return students


def save_students_to_csv(students):
    fieldnames = ['first_name', 'last_name', 'email', 'password', 'birthday']

    with open('csv/students.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


def get_currency_symbol(currency):
    currency_url = 'https://bitpay.com/currencies'
    try:
        currency_response = requests.get(currency_url)
        currencies_data = currency_response.json()

        currency_symbol = next(
            (currency_data['symbol'] for currency_data in currencies_data['data'] if currency_data['code'] == currency),
            '')
        return currency_symbol
    except (requests.RequestException, ValueError, KeyError):
        return ''


def get_bitcoin_value(currency=current_currency, convert=100):
    base_url = 'https://bitpay.com/api/rates'
    try:
        rates_response = requests.get(base_url)
        rates = rates_response.json()

        bitcoin_rate = next((rate['rate'] for rate in rates if rate['code'] == 'BTC'), None)
        currency_rate = next((rate['rate'] for rate in rates if rate['code'] == currency), None)
        currency_symbol = get_currency_symbol(currency)

        if bitcoin_rate is None or currency_rate is None:
            return None

        converted_value = int(convert * (float(currency_rate) / float(bitcoin_rate)))

        return f"{convert} Bitcoins = {converted_value:,} {currency} {currency_symbol}"
    except (requests.RequestException, ValueError, KeyError):
        return None


@app.route('/generate_students', methods=['GET'])
def generate_students_endpoint():
    students = generate_students()
    return render_template('students.html', students=students, limit=1000)


@app.route('/get_bitcoin_value', methods=['GET'])
@app.route('/get_bitcoin_value/<currency>', methods=['GET'])
def get_bitcoin_value_endpoint(currency=current_currency):
    convert = int(request.args.get('convert', 100))
    bitcoin_value = get_bitcoin_value(currency, convert)

    if bitcoin_value is None:
        return "Error: Failed to retrieve bitcoin value."

    return bitcoin_value


if __name__ == '__main__':
    app.run()