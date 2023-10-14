import timeit
import json
import Polyutils


class PolyLocal:
  def __init__(self, exec_file: str, debug: bool) -> None:
    self.polygon = Polyutils.Polygon(exec_file, debug)
    #action is take care of
    self.dbname = None
    self.loc = None
  
  def execute(self, input:str) -> str:
     return self.polygon.execute(str(input).replace(" ", ""))
  
  def read(self) -> str:
    x = f'{{"dbname": "{self.dbname}", "location": "{self.loc}", "action": "read", "value": 20}}'
    return self.execute(x)
  
  def create(self, value) -> str:
    x = f'{{"dbname": "{self.dbname}", "location": "{self.loc}", "action": "create", "value": {value}}}'
    return self.execute(x)
  
  def modify(self, value) -> str:
    x = f'{{"dbname": "{self.dbname}", "location": "{self.loc}", "action": "create", "value": {value}}}'
    return self.execute(x)

  def modify(self) -> str:
    x = f'{{"dbname": "{self.dbname}", "location": "{self.loc}", "action": "delete", "value": "0"}}'
    return self.execute(x)
    

def benchmark(func, num_runs=1):
    total_time = timeit.timeit(func, number=num_runs)
    print(f"\nAverage execution time over {num_runs} runs: {total_time / num_runs:.6f} seconds")


Poly = PolyLocal("./polygondb.exe", False)
