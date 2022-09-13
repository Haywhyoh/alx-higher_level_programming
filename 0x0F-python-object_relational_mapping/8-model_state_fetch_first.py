#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa.
model_state_fetch_first.py <mysql username> /
                            <mysql password> /
                            <database name>
"""
from logging import NullHandler
import sys
from model_state import Base, State
from sqlalchemy.orm import create_engine
from sqlalchemy import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost;3306{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).first()

    for state in states:
        if state:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")

    session.close()
