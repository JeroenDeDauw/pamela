from apiBase import ApiBase
from param import Param
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
            Param(name='name', default=None, islist=True),
            Param(name='type', default=None, islist=True, type=Param.TYPE_INT, values=Entity.getTypes()),
            Param(name='isanon', default=None, islist=True, type=Param.TYPE_BOOL),
            Param(name='status', default=None, islist=True, type=Param.TYPE_INT, values=Entity.getStatuses()),
        ]
    
    def getResult(self):
        entities = []
        
        query = session.query(Entity)
        
        # TODO: loop
        if self.args['name'] is not None:
            query = query.filter(Entity.name.in_(self.args['name']))
            
        if self.args['type'] is not None:
            query = query.filter(Entity.type.in_(self.args['type']))
            
        if self.args['isanon'] is not None:
            query = query.filter(Entity.isanon.in_(self.args['isanon']))
        
        if self.args['status'] is not None:
            query = query.filter(Entity.status.in_(self.args['status']))
        
        for entity in query: 
            entities.append( entity.toDict() )
            
        return { 'success': 'true', 'entities': entities } # TODO: query continue