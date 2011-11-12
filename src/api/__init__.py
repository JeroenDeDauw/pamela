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
    'queryentities': { 'package': 'apiQueryEntities', 'class': 'ApiQueryEntities' },
}

version = ( 0, 0, 1 )


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class Entity(Base):
    '''
    classdocs
    '''
    
    TYPE_INFRASTRUCTURE = 0
    TYPE_PERSON = 1
    TYPE_UNKNOWN = 2
    
    __tablename__ = 'entities'
    
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    isanom = Column(Boolean)
    name = Column(String)
    status = Column(Integer)
    lastseen = Column(Integer)
    
    def __init__(self, **args):
        for key in args:
            setattr(self, key, args[key])
    
    def toDict(self):
        return { 'name': self.name, 'type': self.type }
        
        
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

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
    app.run(debug=True, port=5001)
