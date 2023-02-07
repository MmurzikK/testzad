import yaml
class BaseEnvironment:
    filename = None
    environment = None

    def __init__(self, filename):
        self.filename = filename
        self.environment = self.read()

    def get(self):
        return self.environment
    def read(self):
        with open(self.filename, 'r') as stream:
            return yaml.safe_load(stream)    
