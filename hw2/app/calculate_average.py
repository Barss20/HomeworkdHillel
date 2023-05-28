from flask import Blueprint
import pandas as pd

calculate_average_route = Blueprint('calculate_average', __name__)

@calculate_average_route.route('/calculate_average')
def calculate_average():
    data = pd.read_csv('hw.csv')
    average_height = data['Height(Inches)'].mean()
    average_weight = data['Weight(Pounds)'].mean()
    response = f"""
        <html>
        <head>
            <title>Average Height and Weight</title>
        </head>
        <body>
            <h1>Average Height and Weight</h1>
            <p>Average Height: {average_height:.2f} inches</p>
            <p>Average Weight: {average_weight:.2f} pounds</p>
        </body>
        </html>
    """
    return response