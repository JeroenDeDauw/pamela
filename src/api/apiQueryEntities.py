from apiBase import ApiBase
from param import Param
from entity import Entity
from db import *

'''
Created on Nov 11, 2011

@author: jeroen
'''

class ApiQueryEntities(ApiBase):
    '''
    classdocs
    '''
    
    def getParams(self):
        return [
            Param(name='name', default=None),
            Param(name='type', type=Param.TYPE_INT, default=1) # Enity.TYPE_PERSON
        ]
    
    def getResult(self):
        entities = []
        
        for entity in session.query(Entity).filter_by(type=self.args['type']): 
            entities.append( entity.toDict() )
            
        return { 'success': 'true', 'entities': entities } # TODO: query continue