# Standard library imports
import os


if __name__ == '__main__':
    from first_database_schema_design import Offer
    from create_db_create_engine import Session
    from sqlalchemy.sql import func

    session = Session()

# with open('stored_offers_data.json', 'w', encoding="utf-8") as data_file:
    offers = os.listdir('offers')
    number_of_offers = print(len(offers))

    max_price_value = session.query(func.max(Offer.price)).one()
    print('Max price:', max_val[0])

    min_price_value = session.query(func.min(Offer.price)).one()
    print('Min price:', min_val[0])

    max_val = session.query(func.max(Offer.course)).one()
    print('Max course:', max_val[0])

    min_val = session.query(func.min(Offer.course)).one()
    print('Min course:', min_val[0])

    # max_val_from_Poland = session.query(func.max(Offer.price)).filter(Goods.origin == 'Poland').one()
    # print('Max price:', max_val_from_Poland[0])
    #
    # min_val_from_Poland = session.query(func.min(Offer.price)).filter(Goods.origin == 'Poland').one()
    # print('Min price:', min_val_from_Poland[0])
