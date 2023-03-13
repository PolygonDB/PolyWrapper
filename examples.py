from PolyWrapper import *
connection = PolyWrapper("node2.lunes.host:27023", "Better_Password", "ExampleDB")
res = connection.insert("helloz", {"suss": "yes"})
print(res)
res = connection.insert("hello2", "no")
print(res)
res = connection.get("key")
print(res)