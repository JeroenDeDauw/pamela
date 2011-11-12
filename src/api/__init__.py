import json
import sys
from flask import Flask, request
from docGen import DocGen
from apiException import ApiException

app = Flask(__name__)

modules = {
    'addidentity': { 'package': 'apiAddIdentity', 'class': 'ApiAddIdentity' },
    'editidentity': { 'package': 'apiEditIdentity', 'class': 'ApiEditIdentity' },
    'deleteidentity': { 'package': 'apiDeleteIdentity', 'class': 'ApiDeleteIdentity' },
    'queryentities': { 'package': 'apiQueryEntities', 'class': 'ApiQueryEntities' }
}

version = ( 0, 0, 1 )

from base import Base
from entity import Entity
from engine import engine

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

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
        raise ApiException( 'There is no API module with name "%s"' % moduleName )
    

if __name__ == '__main__':
    app.run(debug=True, port=5002)
