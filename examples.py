import random
import string
from polywrapper_new import *

poly = PolyLocal(exec_file="./polygondb.exe", debug=True)

poly.dbname = "bigdata"
poly.loc = "/data/0/_id"

print(json.loads(poly.read()))

poly.value = 20
print(poly.update())

print(poly.read())