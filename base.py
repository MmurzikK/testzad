import json
import requests
from urllib.parse import unquote
import os
import type_response
import json  
baseurl = os.getenv('baseUrl')
class TestBase:
    environment_adapter = None
    environment = None
    variables = None
    response = None
    errors = None
    faker = None
    path = None
    headers = None
    def __init__(self, environment_adapter,path,headers):
        self.environment_adapter = environment_adapter
        self.environment = environment_adapter.get()
        self.path= path
        self.headers  = headers
        # self.init_variables()

    def test(self):
        assert self.response.status_code == 200
        return self

    def request(self,method="GET",dody=None):
        self.response = requests.request(
            method=method, url=self.environment["host"] + self.environment["port"]+ self.path,json = dody,headers=self.headers)
        return self
      
    def types_response(method,responses):
        return type_response.typeResponse(method,responses)    
        
    def get_json(self):
        return self.response.json()   
    