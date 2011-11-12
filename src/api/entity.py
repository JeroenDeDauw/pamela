'''
Created on Nov 12, 2011

@author: jeroen
'''

from sqlalchemy import Column, Integer, String, Boolean
from base import Base

class Entity(Base):
    '''
    classdocs
    '''
    
    TYPE_INFRASTRUCTURE = 0
    TYPE_PERSON = 1
    TYPE_UNKNOWN = 2
    
    __tablename__ = 'entities'
    
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    isanom = Column(Boolean)
    name = Column(String)
    status = Column(Integer)
    lastseen = Column(Integer)
    
    def __init__(self, **args):
        for key in args:
            setattr(self, key, args[key])
    
    def toDict(self):
        return { 'name': self.name, 'type': self.type }