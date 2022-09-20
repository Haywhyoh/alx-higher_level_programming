#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py <mysql username> /
                                         <mysql password> /<database name>
"""
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bine=engine)
    session = Session()
    cities = session.query(City, State).\
        filter(State.id == City.state_id).order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
