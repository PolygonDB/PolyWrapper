import random
import string
from polywrapper_new import *

poly = PolyClient(connection_url="localhost:8080", exec_path="./polygondb.exe")

print(poly.read(dbname="bigdata", location=""))

poly.close()