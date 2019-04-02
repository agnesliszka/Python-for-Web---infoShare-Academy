# Standard library imports
import os
import sqlite3

# 3rd party imports
from sqlalchemy.sql import func

# Project imports
from first_database_schema_design import Offer
from second_db_engine import Session

session = Session()

def run_query(query, db):
    with sqlite3.connect(db) as conn:
        cursor = conn.execute(query)
        result = cursor.fetchall()
        return result

# Numbers of offers in the database - first method
def statistics():
    offers = os.listdir('offers')
    number_of_offers = len(offers)
    print('Number of offers in the database: ' + str(number_of_offers))

# Numbers of offers in the database - second method
QUERY_MAP = {
    'all_offers': 'SELECT COUNT * FROM offers;',
    'searched_data': 'SELECT id, price, course, model;',
    'models': 'SELECT id, price, model FROM offer GROUP BY model;',
    'count_models_of_cars': 'SELECT COUNT model FROM offer GROUP BY model;',
    'models_of_cars': 'SELECT model FROM offer GROUP BY model;'
}
dirname = os.path.dirname(__file__)
db_name = 'offers.db'
path_to_db = os.path.join(dirname, 'example_dbs', db_name)
print(path_to_db)
print(run_query(QUERY_MAP['all'], path_to_db))

results = session.query(Offer).all()
# model_results = session.query(Offer).filter(Offer.model == '').all()
print('Number of offers in the database: ' + results)

# Function to get minimum and maximum price and minimum and maximum course
def min_max():
    max_price_value = session.query(func.max(Offer.price)).one()
    print('Max price:', max_price_value[0])

    min_price_value = session.query(func.min(Offer.price)).one()
    print('Min price:', min_price_value[0])

    max_course = session.query(func.max(Offer.course)).one()
    print('Max course:', max_course[0])

    min_course = session.query(func.min(Offer.course)).one()
    print('Min course:', min_course[0])

# Create a menu representing available options
def menu():
    while True:
        user_choice = input('''
        Please choose one of the following options:
        1 - show statistics,
        2 - show min/max price and min/max course
        3 - quit  

        ''')

        if user_choice == "1":
            statistics()
            return
        elif user_choice == "2":
            min_max()
            return
        elif user_choice == "3":
            return
        else:
            print("You have inputted incorrect value.")

if __name__ == "__main__":
    menu()

# max_val_from_Poland = session.query(func.max(Offer.price)).filter(Goods.origin == 'Poland').one()
# print('Max price:', max_val_from_Poland[0])
#
# min_val_from_Poland = session.query(func.min(Offer.price)).filter(Goods.origin == 'Poland').one()
# print('Min price:', min_val_from_Poland[0])

