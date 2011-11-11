'''
Created on Nov 11, 2011

@author: jeroen
'''

class ApiBase(object):
    '''
    classdocs
    '''


    def __init__(self, args):
        '''
        Constructor
        '''
        self.args = args
    
    def requiresPost(self):
        return False
    
    def getParams(self):
        return []
    
    def getResult(self):
        return self.args
    
    