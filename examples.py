import random
import string
from polywrapper_new import *

poly = PolyClient(connection_url="localhost:8080", exec_path="./polygondb.exe", dbname="bigdata")

print(poly.read(dbname="bigdata", location="")) 

print(poly.modify(dbname="bigdata", location="/data/0/_id", value=30))
      
print(poly.read(dbname="bigdata", location="/data/0/_id")) 