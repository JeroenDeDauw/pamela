'''
Created on Nov 11, 2011

@author: jeroen
'''

from apiException import ApiException

class ApiBase(object):
    '''
    Base API module class. 
    '''

    def __init__(self, args):
        '''
        Constructor
        '''
        self.handleParams( args )
    
    def handleParams(self, args):
        self.args = {}
        params = {}

        for param in self.getParams():
            params[param.name] = param
        
        for name in args:
            if name in params:
                if self.argIsValid( params[name], args[name] ):
                    value = args[name]
                    
                    if params[name].islist:
                        value = value.split( '|' )
                    
                    self.args[name] = value
                else:
                    raise ApiException( 'Value "%s" is not valid for parameter %s' % args[name], name )
            else:
                raise ApiException( 'Unknown parameter %s' % name ) 
        
        for name in params:
            if name not in self.args:
                if params[name].required:
                    raise ApiException( 'Missing parameter %s' % name )
                else:
                    self.args[name] = params[name].default
    
    def argIsValid(self, param, value):
        return True # TODO
    
    def requiresPost(self):
        return False
    
    def getParams(self):
        return []
    
    def getResult(self):
        raise ApiException( "This API module still needs to implement it's getResult method" )
    
    