# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
dic={
    "name": "John",
    "age": 36,
    "country": "Norway"
}
print(dic)

print(dic["name"])
print(dic.get("age"))#This is not give error when the key is not present in the dictionary
print(dic.get("name"))