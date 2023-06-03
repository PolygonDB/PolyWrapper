from websocket import create_connection
import json
import websocket
class PolyClient:
    def __init__(self, connection_url: str, password: str, db_name: str) -> None:
        """
        Initialize a PolyWrapper instance.

        Args:
            connection_url (str): The URL of the WebSocket connection.
            password (str): The password for accessing the database.
            db_name (str): The name of the database to connect to.
        """
        try:
            self.ws = create_connection(f"ws://{connection_url}/ws")
        except websocket.WebSocketBadStatusException:
            raise Exception("Connection failed")
        self.password = password
        self.db_name = db_name

    def get(self, key: str = ""):
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
                    "password": self.password,
                    "dbname": self.db_name,
                    "location": key,
                    "action": "retrieve",
                }
            )
        )
        return json.loads(self.ws.recv())

    def insert(self, key: str, value: any):
        """
        Insert data into the database.

        Args:
            key (str): The key or location to insert the data.
            value (any): The data to be inserted. It can be a JSON-serializable value or a dictionary.

        Returns:
            dict: The response received from the database server.
        """
        if type(value) == dict:
            input_value = json.dumps(value)
        else:
            input_value = value
        self.ws.send(
            json.dumps(
                {
                    "password": self.password,
                    "dbname": self.db_name,
                    "location": key,
                    "action": "record",
                    "value": json.dumps(input_value),
                }
            )
        )
        return json.loads(self.ws.recv())

    def remove(self, key: str):
        """
        Remove data from the database.

        Args:
            key (str): The key or location of the data to be removed.

        Returns:
            dict: The response received from the database server.
        """
        self.ws.send(
            json.dumps(
                {
                    "password": self.password,
                    "dbname": self.db_name,
                    "location": key,
                    "action": "record",
                    "value": "",
                }
            )
        )
        return json.loads(self.ws.recv())

    def update(self, key: str, value: any):
        """
        Update data in the database.

        Args:
            key (str): The key or location of the data to be updated.
            value (any): The updated value to be stored. It can be a JSON-serializable value or a dictionary.

        Returns:
            dict: The response received from the database server.
        """
        if type(value) == dict:
            input_value = json.dumps(value)
        else:
            input_value = value
        self.ws.send(
            json.dumps(
                {
                    "password": self.password,
                    "dbname": self.db_name,
                    "location": key,
                    "action": "record",
                    "value": input_value,
                }
            )
        )
        return json.loads(self.ws.recv())

    def append(self, key: str, value: any):
        if type(value) == dict:
            input_value = json.dumps(value)
        else:
            input_value = value
        self.ws.send(
            json.dumps(
                {
                    "password": self.password,
                    "dbname": self.db_name,
                    "location": key,
                    "action": "append",
                    "value": input_value,
                }
            )
        )
        return json.loads(self.ws.recv())