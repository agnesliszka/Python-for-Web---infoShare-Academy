# 3rd party imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Project imports
from first_database_schema_design import Base


# Set a database name
engine = create_engine('sqlite:///offers.db')
# Create a structure
Base.metadata.create_all(engine)
# Create session object
Session = sessionmaker(bind=engine)
