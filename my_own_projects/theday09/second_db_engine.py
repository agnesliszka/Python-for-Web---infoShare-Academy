# 3rd party imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Project imports
from first_database_schema_design import Base

engine = create_engine('sqlite:///offers.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
