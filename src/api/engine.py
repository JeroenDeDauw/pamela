'''
Created on Nov 12, 2011

@author: jeroen
'''

from base import Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)