from websocket import create_connection
import json

class PolyWrapper():
    def __init__(self, connection_url: str, password: str, db_name: str) -> None:
        self.ws = create_connection(f"ws://{connection_url}/ws")
        self.password = password
        self.db_name = db_name
    def get(self, key: str=""):
        

        self.ws.send(json.dumps(
            {
                'password': self.password,
                'dbname': self.db_name,
                'location' : key,
                'action' : 'retrieve'
            }
        ))
        return json.loads(self.ws.recv())
        
    def insert(self, key: str, value: any):
        if type(value) == dict:
            input_value = json.dumps(value)
        else:
            input_value = value
        self.ws.send(json.dumps(
            {
                'password': self.password,
                'dbname': self.db_name,
                'location' : key,
                'action' : 'record',
                'value': json.dumps(input_value)
            }
        ))
        return json.loads(self.ws.recv())
    
    def remove(self, key: str):
        self.ws.send(json.dumps(
            {
                'password': self.password,
                'dbname': self.db_name,
                'location' : key,
                'action' : 'record',
                'value': ""
            }
        ))
        return json.loads(self.ws.recv())
    
    def search(self, key: str, input: str):
        self.ws.send(json.dumps(
            {
                'password': 'Better_Password', 
                'dbname': 'CatoDB',
                'location' :key,
                'action' : 'search',
                'value': json.dumps(input)
            }
        ))
        return json.loads(self.ws.recv())
