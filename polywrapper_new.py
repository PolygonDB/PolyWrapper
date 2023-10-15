from aiohttp import WebSocketError
from websocket import create_connection
import json


class PolyClient:
    def __init__(self, connection_url: str, exec_path: str) -> None:
        """
        Initialize a PolyWrapper instance.

        Args:
            connection_url (str): The URL of the WebSocket connection.
            password (str): The password for accessing the database.
            db_name (str): The name of the database to connect to.
        """
        try:
            self.ws = create_connection(f"ws://{connection_url}/ws")
        except WebSocketError.WebSocketBadStatusException:
            raise Exception("Connection failed")

    
    def read(self, dbname: str, location: str = ""):
      """
      Retrieve data from the database.

      Args:
          dbname (str, required): Name of Database
          
          location (str,optional): Location in Data
              Defaults to an empty string, which retrieves the entire database

      Returns:
          dict: The retrieved data as a dictionary.
      """
      self.ws.send(
          json.dumps(
              {
                  "dbname": dbname,
                  "location": location,
                  "action": "read",
                  "value" : 0
              }
          )
      )
      return json.loads(self.ws.recv())

    def create(self, dbname: str, location: str = "", value = None):
      """
      Creates data from the database.

      Args:
          dbname (str, required): Name of Database
          
          location (str,optional): Location in Data
              Defaults to an empty string, which retrieves the entire database

      Returns:
          dict: The retrieved data as a dictionary.
      """

      if value == None:
        return json.loads("""{"Status":"1", "Message":"Please Assign Value to a Variable"}""")
      
      self.ws.send(
          json.dumps(
              {
                  "dbname": dbname,
                  "location": location,
                  "action": "create",
                  "value" : value
              }
          )
      )
      return json.loads(self.ws.recv())

    def modify(self, dbname: str, location: str = "", value = None):
      """
      Modifies data from the database.

      Args:
          dbname (str, required): Name of Database
          
          location (str,optional): Location in Data
              Defaults to an empty string, which retrieves the entire database

      Returns:
          dict: The retrieved data as a dictionary.
      """

      if value == None:
        return json.loads("""{"Status":"1", "Message":"Please Assign Value to a Variable"}""")
      
      self.ws.send(
          json.dumps(
              {
                  "dbname": dbname,
                  "location": location,
                  "action": "modify",
                  "value" : value
              }
          )
      )
      return json.loads(self.ws.recv())

    def delete(self, dbname: str, location: str = ""):
      """
      Deletes data from the database.

      Args:
          dbname (str, required): Name of Database
          
          location (str,optional): Location in Data
              Defaults to an empty string, which retrieves the entire database

      Returns:
          dict: The retrieved data as a dictionary.
      """
      self.ws.send(
          json.dumps(
              {
                  "dbname": dbname,
                  "location": location,
                  "action": "delete",
                  "value" : 0
              }
          )
      )
      return json.loads(self.ws.recv())