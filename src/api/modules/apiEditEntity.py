from apiBase import ApiBase
from param import Param
from db import *

'''
Created on Nov 11, 2011

@author: jeroen
'''

class ApiEditEntity(ApiBase):
    '''
    API module to edit a single entity.
    '''


    def requiresPost(self):
        return True