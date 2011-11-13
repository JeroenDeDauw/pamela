'''
Created on Nov 13, 2011

@author: jeroen
'''

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean

class Entity(Base):
    '''
    classdocs
    '''
    
    #static
    TYPE_INFRASTRUCTURE = 0
    TYPE_PERSON = 1
    TYPE_UNKNOWN = 2
    
    #static
    STATUS_ACTIVE = 0
    STATUS_IDLE = 1
    STATUS_AWAY = 2
    STATUS_BUSSY = 3
    
    __tablename__ = 'entities'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True)
    type = Column(Integer, index=True)
    isanom = Column(Boolean, index=True)
    status = Column(Integer, index=True)
    lastseen = Column(Integer, index=True)
    
    def __init__(self, **args):
        for key in args:
            setattr(self, key, args[key])
    
    def toDict(self):
        dict = {
            'name': 'anon' if self.isanom else self.name,
            'type': self.type,
            'isanom': self.isanom,
            'status': self.status,
            'lastseen': self.lastseen
        }
        
        return dict
    
    @staticmethod
    def getTypes():
        return [Entity.TYPE_INFRASTRUCTURE, Entity.TYPE_PERSON, Entity.TYPE_UNKNOWN]
    
    @staticmethod
    def getStatuses():
        return [Entity.STATUS_ACTIVE, Entity.STATUS_AWAY, Entity.STATUS_BUSSY, Entity.STATUS_IDLE]

from sqlalchemy import create_engine

engine = create_engine('sqlite:////home/jeroen/www/pam', echo=True)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()