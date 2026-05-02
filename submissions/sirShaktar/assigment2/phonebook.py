
phonebook = {}

phonebook["Ali"] = "12345"
phonebook["Sara"] = "67890"
phonebook["Omar"] = "54321"

print(phonebook.get("Ali"))
print(phonebook.get("John", "unknown"))

for name in phonebook:
    print(name)

for name, number in phonebook.items():
    print(name, number)