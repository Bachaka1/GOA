# 1)
my_name = "mamuka bachakashvili"
for letter in my_name:
    print(letter)

# 2)
# for i in name აკლია :
# print(i) ინდენტაცია არ არის დაცული

# 3)
# For loop: გამოიყენება, როცა ცნობილია რამდენჯერ უნდა გამეორდეს.
# While loop: გამოიყენება, როცა არ არის ცნობილი რამდენჯერ უნდა გამეორდეს.

# 4)
i = 1
while i <= 10:
    print(i)
    i += 1

# 5)
i = 10
while i >= 1:
    print(i)
    i -= 1

# 6)
name = input("enter your name: ")
vowels = "aeiou"
count = 0
for letter in name:
    if letter.lower() in vowels:
        count += 1
print(count)

# 7)
password = "python"
guess = input("enter the password: ")
while guess != password:
    print("Incorrect password, try again.")
    guess = input("enter the password: ")
print("access granted!")