'''
Created on Nov 12, 2011

@author: jeroen
'''

from apiException import ApiException

class Param(object):
    '''
    classdocs
    '''
    
    TYPE_STR = 0
    TYPE_INT = 1
    TYPE_BOOL = 2
    
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
        