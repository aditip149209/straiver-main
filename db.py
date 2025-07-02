from sqlmodel import *

import os

POSTGRES_URL = os.environ["POSTGRES_URL"]

engine = create_engine(POSTGRES_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session


