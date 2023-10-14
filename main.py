import timeit
import json
import Polyutils

def benchmark(func, num_runs=1):
    total_time = timeit.timeit(func, number=num_runs)
    print(f"\nAverage execution time over {num_runs} runs: {total_time / num_runs:.6f} seconds")

test = Polyutils.Polygon("./polygondb.exe")

def use_polygon():
   return test.test("test")

def use_json():
  with open('databases/bigdata.json') as f:
    return json.load(f)
   
if __name__ == '__main__':
    benchmark(use_polygon, num_runs=90)
    benchmark(use_json, num_runs=90)