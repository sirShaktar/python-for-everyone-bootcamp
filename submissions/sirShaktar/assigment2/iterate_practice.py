nums = list(range(10))

print(nums[::2])
print(nums[::-1])

for i in range(3, 8):
    print(i)

words = ["apple", "banana", "cherry"]

for index, word in enumerate(words):
    print(index, word)

d = {"a": 1, "b": 2}

for k, v in d.items():
    print(k, v)