'''
Created on Nov 12, 2011

@author: jeroen
'''

from engine import engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

