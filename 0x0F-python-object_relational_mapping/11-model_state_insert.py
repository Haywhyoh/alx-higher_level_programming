#!/usr/bin/python3
"""
This is what we discovered about it
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

louisiana = State(name="Louisiana")
session.add(louisiana)
session.commit()
print(louisiana.id)
