from sqlmodel import Session, create_engine
from .database import engine

# Dependencias
def get_session():
    with Session(engine) as session:
        yield session
