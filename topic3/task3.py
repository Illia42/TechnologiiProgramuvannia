user = {"name": "Ivan", "age": 20, "city": "Kyiv"}
print("Start:", user)

user.update({"group": "KB-251", "status": "student"})
print("update:", user)

print("keys:", list(user.keys()))
print("values:", list(user.values()))
print("items:", list(user.items()))

del user["age"]
print("del user['age']:", user)

user.clear()
print("clear:", user)