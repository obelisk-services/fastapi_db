from sqlmodel import SQLModel, create_engine
import os
from pprint import pprint



# Get the environment variables
db_user = os.getenv('MYSQL_USER')
db_server = os.getenv('MYSQL_HOST')
db_password = os.getenv('MYSQL_PASSWORD')
db_name = os.getenv('MYSQL_DATABASE')
db_port = os.getenv('db_port') 

# Create the URL
bd_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_server}/{db_name}?charset=utf8mb4&collation=utf8mb4_general_ci"

# pprint(db_name)
# pprint(bd_url)
# Create the engine
connect_args ={} # {"check_same_thread": False}
engine = create_engine(bd_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    # prueba

