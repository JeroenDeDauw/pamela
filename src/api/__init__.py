import json
import sys
from flask import Flask, request
from docGen import DocGen
from apiException import ApiException
from mods import getModule

app = Flask(__name__)

version = ( 0, 0, 1 )

@app.route('/')
@app.route('/api')
def index():
    html = 'Pamela API version %s.%s.%s' % version
    html += '<hr />'
    
    html += DocGen.getDocs()
    
    return html

@app.route('/api/<moduleName>')
def apiRequest(moduleName):
    module = getModule( moduleName, request.args )
    
    if module == False:
        raise ApiException( 'There is no API module with name "%s"' % moduleName )
    else:
        result = module.getResult()
        return json.dumps( { 'result': result } )

if __name__ == '__main__':
    app.run(debug=True, port=5002)
