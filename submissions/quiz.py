name = input("What is your name? ")
print("Welcome " + name + "!")

score = 0

# Question 1
print("Q1: What keyword prints text to the screen?")
answer1 = input("Your answer: ")

if answer1 == "print":
    print("Correct!")
    score = score + 1
else:
    print("Wrong")

# Question 2
print("Q2: What symbol is used for equality comparison in Python?")
answer2 = input("Your answer: ")

if answer2 == "==":
    print("Correct!")
    score = score + 1
else:
    print("Wrong")

# Question 3
print("Q3: Is Python case-sensitive? (yes/no)")
answer3 = input("Your answer: ")

if answer3 == "yes":
    print("Correct!")
    score = score + 1
else:
    print("Wrong")

print(name + ", your score is " + str(score) + " out of 3")