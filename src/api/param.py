'''
Created on Nov 12, 2011

@author: jeroen
'''

class Param(object):
    '''
    Parameter definition
    '''
    
    TYPE_STR = 0
    TYPE_INT = 1
    TYPE_BOOL = 2
    
    # static
    map = {
        TYPE_STR: 'string',
        TYPE_INT: 'integer',
        TYPE_BOOL: 'boolean'
    }
    
    def __init__(self, **args):
        '''
        Constructor
        '''
        self.name = args['name'] # TODO: exception
        self.type = args['type'] if 'type' in args else Param.TYPE_STR
        self.default = args['default'] if 'default' in args else None
        self.islist = args['islist'] if 'islist' in args else False
        self.values = args['values'] if 'values' in args else None
        self.required = args['required'] if 'required' in args else not 'default' in args
        
    def getTypeName(self):
        return self.map[self.type]
        