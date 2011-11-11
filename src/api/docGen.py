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
        html = '<b>Available modules:</b><br />'
        
        html += '\n'.join( ['<li>' + self.getModuleDocs( module, data ) + '</li>' for module, data in self.modules.items()] )
        html = '<ul>' + html + '</ul>'
        
        return html
    
    def getModuleDocs(self, module, data):
        return module
    