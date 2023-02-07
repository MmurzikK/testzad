from environment import base_environment
from base import TestBase
import  pytest 
import json
environment_adapter = base_environment.BaseEnvironment(
        "environment/test_dev.yaml")
path ="/api/books"  

class PostTest:      
        @pytest.mark.parametrize("dody,asser",[({"book": {"name": "TestAme"}},"name")])
        def test_post_method(dody,asser):
                TestBase.types_response(TestBase(
            environment_adapter,path=path).request("POST",dody).test().get_json())
        def test_post():
                dody ={"name": "Чистый код"}
                reponse= TestBase(
            environment_adapter,path=path,headers={
  'Content-Type': 'application/json'
}).request("POST",dody)
                assert reponse.response.status_code ==201

                
PostTest.test_post()            