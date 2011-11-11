'''
Created on Nov 11, 2011

@author: jeroen
'''

class DocGen(object):
    '''
    classdocs
    '''

    def __init__(self, modules):
        '''
        Constructor
        '''
        self.modules = modules
        
    def getDocs(self):
        return 'Available modules:<br />' + '<br />'.join( [self.getModuleDocs( module, data ) for module, data in self.modules.items()] )
    
    def getModuleDocs(self, module, data):
        return module
    