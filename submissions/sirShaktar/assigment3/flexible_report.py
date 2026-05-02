def total(*numbers):
    return sum(numbers)

def profile(**info):
    for k, v in info.items():
        print(k, ":", v)

print(total(1, 2, 3))
print(total(5, 10))
print(total())

profile(name="Ali", age=20)
profile(name="Sara", country="Somalia", job="Student")