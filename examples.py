import random
import string
from polywrapper_new import *

poly = PolyClient(connection_url="localhost:8080", dbname="bigdata")

print(poly.read(location="")) 

print(poly.modify(location="/data/0/_id", value=30))
      
print(poly.read(location="/data/0/_id")) 