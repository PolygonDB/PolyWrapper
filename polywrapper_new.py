import timeit
import json
import Polyutils


class PolyLocal:
  def __init__(self, exec_file: str, debug: bool) -> None:
    self.polygon = Polyutils.Polygon(exec_file, debug)
    #action is take care of
    self.dbname = None
    self.loc = None
    self.value = None
  
  def execute(self, input:str) -> str:
     return self.polygon.execute(str(input).replace(" ", ""))
  
  def read(self) -> str:
    x = f'{{"dbname": "{self.dbname}", "location": "{self.loc}", "action": "read", "value": 20}}'
    print(x)
    return self.execute(x)
  
  def create(self) -> str:
    x = f'{{"dbname": "{self.dbname}", "location": "{self.loc}", "action": "create", "value": {self.value}}}'
    print(x)
    return self.execute(x)
  
  def update(self) -> str:
    x = f'{{"dbname": "{self.dbname}", "location": "{self.loc}", "action": "update", "value": {self.value}}}'
    print(x)
    return self.execute(x)

  def delete(self) -> str:
    x = f'{{"dbname": "{self.dbname}", "location": "{self.loc}", "action": "delete", "value": 0}}'
    return self.execute(x)
    