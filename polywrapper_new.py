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
          key (str, optional): The key or location to retrieve data from.
              Defaults to an empty string, which retrieves the entire database.

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