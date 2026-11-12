# Dictionary
person = {"name": "Ian", "age": 18, "city": "Paris"}

## access value by key
print(person["name"])
print(person.get("country"))

## modify value by key
person["city"] = "Lisbon"
print(person)

## add / delete key
person["school"] = "EPITA"
del person["age"]
print(person)