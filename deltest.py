from environment import base_environment
from base import TestBase
import json
environment_adapter = base_environment.BaseEnvironment(
    "environment/test_dev.yaml")
path = "/api/books"

class DelTest:
    def test_delete_one():
        dody ={
            "book": {
                "name": "TestAme"
            }
        }#не рабоаю некоорые кнопк на клаве соре поэому аке названя 
        response = TestBase(
            environment_adapter, path=path).request(method="POST",dody=dody).test().get_json()
        assert response["name"] == "TestAme"
        id  =response["books"]["id"]
        TestBase.types_response("DELETE", TestBase(
            environment_adapter, path=path + f"/{id}").request(method="DELETE").test().get_json())
        TestBase.types_response("DELETE",response)
    def test_delete_nothing():
        id = 0
        response =  TestBase(
            environment_adapter, path=path + f"/{id}").request(method="DELETE").get_json()   
        assert {
    "error": f"Book with id {id} not found"
} == response    

    #def test_delete_all_pooks_id():
    #    response = TestBase(
    #        environment_adapter, path=path).request().test().get_json()
    #    for i in response["books"]:
    #        id = i["id"]
    #        TestBase(
    #            environment_adapter, path=path + f"/{id}").request(method="DELETE").test().get_json()
