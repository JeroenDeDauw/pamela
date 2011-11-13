import json
import sys
from flask import Flask, request
from docGen import DocGen
from apiException import ApiException

app = Flask(__name__)

modules = {
    'addidentity': { 'package': 'apiAddEntity', 'class': 'ApiAddEntity' },
    'editidentity': { 'package': 'apiEditEntity', 'class': 'ApiEditEntity' },
    'deleteentity': { 'package': 'apiDeleteEntity', 'class': 'ApiDeleteEntity' },
    'queryentities': { 'package': 'apiQueryEntities', 'class': 'ApiQueryEntities' }
}

version = ( 0, 0, 1 )

@app.route('/')
@app.route('/api')
def index():
    html = 'Pamela API version %s.%s.%s' % version
    html += '<hr />'
    
    docGen = DocGen( modules )
    html += docGen.getDocs()
    
    return html

@app.route('/api/<moduleName>')
def apiRequest(moduleName):
    if moduleName in modules:
        module = modules[moduleName]
        mod = __import__( 'modules.' + module['package'], fromlist=[module['class']] )
        module = getattr(mod, module['class'])( request.args )
        result = module.getResult()
        return json.dumps( { 'result': result } )
    else:
        raise ApiException( 'There is no API module with name "%s"' % moduleName )
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)
