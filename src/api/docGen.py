'''
Created on Nov 11, 2011

@author: jeroen
'''

from api.mods import getModules, getModuleNames

class DocGen(object):
    '''
    classdocs
    '''

    @staticmethod
    def getDocs():
        html = '<br />Modules are called by <i>/api/modulename?param=value&more=stuff</i>.<br /><br />'
        
        html += '<b>Available modules:</b><br />'
        
        list = '\n'.join( ['<li>' + name + '</li>' for name in getModuleNames()] )
        html += '<ul>' + list + '</ul>'
        
        html += '\n'.join( [ DocGen.getModuleDocs( module ) for module in getModules()] )
        
        return html
    
    @staticmethod
    def getModuleDocs(module):
        html = '<b>********** /api/' + module.moduleName + '/ **********</b><br />'
        
        params = '\n'.join( ['<li>' + DocGen.getParamDocs( param ) + '</li>' for param in module.getParams()] )
        html += 'Parameters:<ul>' + params + '</ul>'
        
        return html
    
    @staticmethod
    def getParamDocs(param):
        items = [
            'type: ' + param.getTypeName()
        ]
        
        if param.islist:
            items.append( 'list' )
            
        items.append( 'required' if param.required else 'default: ' + str( param.default ) )
            
        return param.name + ' (' + ', '.join( items ) + ')'
        
    