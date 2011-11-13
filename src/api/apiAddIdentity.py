from apiBase import ApiBase
from param import Param
from db import *

'''
Created on Nov 11, 2011

@author: jeroen
'''

class ApiAddIdentity(ApiBase):
    '''
    classdocs
    '''
    
    def getParams(self):
        return [
            Param(name='name'),
            Param(name='type', type=Param.TYPE_INT)
        ]
    
    def getResult(self):
        entity = Entity( name=self.args['name'], type=self.args['type'] )
        
        session.add(entity)
        session.commit()
        
        return { 'success': 'true' }