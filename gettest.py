from environment import base_environment
from base import TestBase
import requests
environment_adapter = base_environment.BaseEnvironment(
        "environment/test_dev.yaml")
path ="/api/books"       
class GetTest: 
        def test_get_method():
                TestBase.types_response(TestBase(
                environment_adapter,path=path).request().test().get_json())
        def test_get_method_id():
                response = TestBase(
            environment_adapter,path =path).request().test().get_json()
                for i in response["books"]:
                        id =i["id"]
                        TestBase(
            environment_adapter,path =path +f"/{id}").request().test().get_json()
        def test_get_method_ids():
                response = TestBase(
            environment_adapter,path =path +f"/0").request()
                assert response.response == 404
                TestBase.types_response(response)

