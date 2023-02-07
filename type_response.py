from openapi_schema_validator import validate
from openapi_schema_validator import oas31_format_checker
class getSchema:
    schema = {
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "books"
    ],
    "properties": {
        "books": {
            "type": "array",
            "default": [],
            "title": "The books Schema",
            "items": {
                "type": "object",
                "title": "A Schema",
                "required": [
                    "author",
                    "id",
                    "isElectronicBook",
                    "name",
                    "year"
                ],
                "properties": {
                    "author": {
                        "type": "string",
                        "title": "The author Schema",
                        "examples": [
                            "Роберт Мартин"
                        ]
                    },
                    "id": {
                        "type": "integer",
                        "title": "The id Schema"
                    },
                    "isElectronicBook": {
                        "type": "boolean",
                        "title": "The isElectronicBook Schema"
                    },
                    "name": {
                        "type": "string",
                        "title": "The name Schema"
                    },
                    "year": {
                        "type": "integer",
                        "title": "The year Schema"
                    }
                }
                
            }
        }
    }
}
class postSchema:
    schema = {
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "books"
    ],
    "properties": {
        "books": {
            "type": "array",
            "default": [],
            "title": "The books Schema",
            "items": {
                "type": "object",
                "title": "A Schema",
                "required": [
                    "author",
                    "id",
                    "isElectronicBook",
                    "name",
                    "year"
                ],
                "properties": {
                    "author": {
                        "type": "string",
                        "title": "The author Schema",
                        "examples": [
                            "Роберт Мартин"
                        ]
                    },
                    "id": {
                        "type": "integer",
                        "title": "The id Schema"
                    },
                    "isElectronicBook": {
                        "type": "boolean",
                        "title": "The isElectronicBook Schema"
                    },
                    "name": {
                        "type": "string",
                        "title": "The name Schema"
                    },
                    "year": {
                        "type": "integer",
                        "title": "The year Schema"
                    }
                }
                
            }
        }
    }
}
class putSchema:
    schema = {
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "books"
    ],
    "properties": {
        "books": {
            "type": "array",
            "default": [],
            "title": "The books Schema",
            "items": {
                "type": "object",
                "title": "A Schema",
                "required": [
                    "author",
                    "id",
                    "isElectronicBook",
                    "name",
                    "year"
                ],
                "properties": {
                    "author": {
                        "type": "string",
                        "title": "The author Schema",
                        "examples": [
                            "Роберт Мартин"
                        ]
                    },
                    "id": {
                        "type": "integer",
                        "title": "The id Schema"
                    },
                    "isElectronicBook": {
                        "type": "boolean",
                        "title": "The isElectronicBook Schema"
                    },
                    "name": {
                        "type": "string",
                        "title": "The name Schema"
                    },
                    "year": {
                        "type": "integer",
                        "title": "The year Schema"
                    }
                }
                
            }
        }
    }
}
class deleteSchema:
    schema = {
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "result"
    ],
    "properties": {
        "result": {
            "type": "boolean",
            "title": "The result Schema",
        }
    }
}

def ValidateResponse(schema,response):
        validate(response, schema,format_checker=oas31_format_checker)
def typeResponse(method,response):#структура чуть кривая схемы в жисон файлы кинуть нужно и сам выбор типизации исправить
        if method =="GET":
          ValidateResponse(getSchema.schema,response)
        if method  == "POST":
            ValidateResponse(postSchema.schema,response)
        if method  == "PUT":
            ValidateResponse(putSchema.schema,response)
        if method  == "DELETE":
            ValidateResponse(deleteSchema.schema,response)      