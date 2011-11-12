'''
Created on Nov 11, 2011

@author: jeroen
'''

from apiException import ApiException

class ApiBase(object):
    '''
    classdocs
    '''

    def __init__(self, args):
        '''
        Constructor
        '''
        self.args = {}
        params = {}

        for param in self.getParams():
            params[param.name] = param
        
        for name in args:
            if name in params:
                if self.argIsValid( params[name], args[name] ):
                    self.args[name] = args[name]
                else:
                    raise ApiException( 'Value "%s" is not valid for parameter %s' % args[name], name )
            else:
                raise ApiException( 'Unknown parameter %s' % name ) 
        
        # TODO: make sure all params w/o default are set
    
    def argIsValid(self, param, value):
        return True # TODO
    
    def requiresPost(self):
        return False
    
    def getParams(self):
        return []
    
    def getResult(self):
        raise ApiException( "This API module still needs to implement it's getResult method" )
    
    