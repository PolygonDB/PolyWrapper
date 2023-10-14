from polywrapper_new import *

poly = PolyLocal(exec_file="./polygondb.exe", debug=False)

poly.dbname = "bigdata"
poly.loc = "/data/0/_id"

print(json.loads(poly.read()))