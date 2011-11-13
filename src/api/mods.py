'''
Created on Nov 13, 2011

@author: jeroen
'''

_modules = {
    'addidentity': { 'package': 'apiAddEntity', 'class': 'ApiAddEntity' },
    'editidentity': { 'package': 'apiEditEntity', 'class': 'ApiEditEntity' },
    'deleteentity': { 'package': 'apiDeleteEntity', 'class': 'ApiDeleteEntity' },
    'queryentities': { 'package': 'apiQueryEntities', 'class': 'ApiQueryEntities' }
}

def getModuleNames():
    return _modules.keys()

def getModules():
    return [getModule( name, {}, False ) for name in _modules.keys()]

def getModule( moduleName, args, handleArgs=True ):
    if moduleName in _modules:
        module = _modules[moduleName]
        mod = __import__( 'modules.' + module['package'], fromlist=[module['class']] )
        module = getattr(mod, module['class'])( args, handleArgs )
        module.moduleName = moduleName
        return module
    else:
        return False