from apiBase import ApiBase
from param import Param
from db import *

'''
Created on Nov 11, 2011

@author: jeroen
'''

class ApiAddEntity(ApiBase):
    '''
    API module to add a single entity.
    '''
    
    def getParams(self):
        return [
            Param(name='name', ),
            Param(name='type', default=Entity.TYPE_PERSON, type=Param.TYPE_INT, values=Entity.getTypes()),
            Param(name='isanon', default=False, type=Param.TYPE_BOOL),
            Param(name='status', default=Entity.STATUS_UNKNOWN, type=Param.TYPE_INT, values=Entity.getStatuses()),
        ]
    
    def getResult(self):
        entity = Entity.newFromDict( self.args )
        
        session.add( entity )
        session.commit()
        
        return { 'success': 'true' }
    
    def requiresPost(self):
        return True