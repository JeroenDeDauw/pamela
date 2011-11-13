from api.apiBase import ApiBase
from api.param import Param
from api.db import *

'''
Created on Nov 11, 2011

@author: jeroen
'''

class ApiDeleteEntity(ApiBase):
    '''
    API module that deletes the matching entities.
    '''
    
    def getParams(self):
        return [
            Param(name='id', type=Param.TYPE_INT, islist=True ),
        ]
    
    def getResult(self):
        entity = Entity.newFromDict( self.args )
        
        session.add( entity )
        session.commit()
        
        return { 'success': 'true' }
    
    def requiresPost(self):
        return True