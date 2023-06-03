You can download it here https://pypi.org/project/polywrapper/
# Welcome to the PolyWrapper wiki!

Here is the basics of using poly wrapper

### To install polywrapper run the following command
`pip install polywrapper`

Here is an example of inserting data into a database

```import polywrapper
connection = polywrapper.PolyClient("node2.lunes.host:27106", "Better_Password", "ExampleDB")

res = connection.insert("Hello", "World")
print(res)
```
This will return {"Status": "Success"} if it works.`

### You can also input sub level JSON and lists
```
connection.insert({"users": ["David", "Andrew"]})
connection.insert("meta", {"page": "2"})
```

### To get data from certain key
```res = connection.get("key")
print(res)
to get all data from database do
res = connection.get()
```
if the key value system is {"key": "value"} it will return value if it is something like {"key": {"sub": "json"}} it will return {"sub": "json"}

### To update a keys value.

`connection.update("key", "value2")`
once again this can be json or a string
to append data to a list you will need to do
`res = connection.insert("users", ["John", "Andrew"])
connection.append("users", "Mia")
`
### To remove certain keys.

`
connection.remove('key')
`