import json
import sys
from flask import Flask, request
from docGen import DocGen

app = Flask(__name__)

modules = {
    'addidentity': { 'package': 'apiAddIdentity', 'class': 'ApiAddIdentity' },
    'editidentity': { 'package': 'apiEditIdentity', 'class': 'ApiEditIdentity' },
    'deleteidentity': { 'package': 'apiDeleteIdentity', 'class': 'ApiDeleteIdentity' }
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
        mod = __import__( module['package'], fromlist=[module['class']] )
        module = getattr(mod, module['class'])( request.args )
        result = module.getResult()
        return json.dumps( { 'result': result } )
    else:
        return 'onoez!'
    

if __name__ == '__main__':
    app.run(debug=True)
    