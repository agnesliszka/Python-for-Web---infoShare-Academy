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


QUERY_MAP = {
    'all': 'select * from offers;',
    'number_of_offers': 'SELECT COUNT (*) FROM offers;',
    'models_of_cars': 'SELECT model FROM offers GROUP BY model;',
    'count_models_of_cars': 'SELECT COUNT (model) FROM offers GROUP BY model;',
}

dirname = os.path.dirname(__file__)
db_name = 'offers.db'
path_to_db = os.path.join(dirname, db_name)

# Numbers of offers in the database - second method
number_of_offers = run_query(QUERY_MAP['number_of_offers'], path_to_db)
print('Number of offers in the database: ' + str(number_of_offers))

print(run_query(QUERY_MAP['all'], path_to_db))
print(run_query(QUERY_MAP['models_of_cars'], path_to_db))
print(run_query(QUERY_MAP['count_models_of_cars'], path_to_db))


# Models of cars in the database
# models_of_cars = run_query(QUERY_MAP['models_of_cars'], path_to_db))
# print(models_of_cars)


# results = session.query(Offer).all()
# # model_results = session.query(Offer).filter(Offer.model == '').all()


# Function to get minimum and maximum price and minimum and maximum course
def min_max():
    min_price_value = session.query(func.min(Offer.price)).one()
    print('Mix price:', min_price_value[0])

    max_price_value = session.query(func.max(Offer.price)).one()
    print('Max price:', max_price_value[0])

    min_course = session.query(func.min(Offer.course)).one()
    print('Mix course:', min_course[0])

    max_course = session.query(func.max(Offer.course)).one()
    print('Max course:', max_course[0])

# Create a menu representing available options
def menu():
    while True:
        user_choice = input('''
        What would you like to do now? 
        Please choose one of the following options:
                
        1 - show statistics,
        2 - show min/max price and min/max course
        3 - quit  

        ''')

        if user_choice == "1":
            statistics()

        elif user_choice == "2":
            min_max()

        elif user_choice == "3":
            return
        else:
            print("You have inputted incorrect value.")

if __name__ == "__main__":
    menu()


# Offer.query.count().filter(model='cos')

# max_val_from_Poland = session.query(func.max(Offer.price)).filter(Goods.origin == 'Poland').one()
# print('Max price:', max_val_from_Poland[0])
#
# min_val_from_Poland = session.query(func.min(Offer.price)).filter(Goods.origin == 'Poland').one()
# print('Min price:', min_val_from_Poland[0])

