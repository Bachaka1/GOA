# 1)
# a = 5
# b = "3"

# sum = 5 + b
# print(sum)
a = 5
b = 3

sum = a + b
print(sum)

# 2)
x = "100"
print(int(x))
print(float(x))

y = "155"
print(int(y))
print(float(y))

# 3)
c = float(input("enter float number: "))
d = float(input("enter float number: "))
result = c + d
print(result)

# 4)
e = int(input("enter number 1: "))
f = int(input("enter number 2: "))

if e % 2 == 0 and f % 2 == 0:
    
    total = e + f
    print(total)
else:
    
    print("The given numbers are not even so they will not be summed")

# 5)
name = input("enter your name: ")
surname = input("enter your surname: ")
age = input("enter your age: ")
city = input("enter where you live: ")
country = input("enter country where you live: ")
print("your name is:", name)
print("your surname is:", surname)
print("your age is:", age)
print("you live in:", city)
print("the country where you live in is:", country)

# 6)
print(30 < 25)
print(55 < 100)

# 7)
h =int(input("enter number: "))
i =int(input("enter number: "))
print(h+i)
print(h-i)
print(h*i)
print(h/i)

# 8)
my_name="mamuka"
user_name=input("enter your name: ")
if my_name == user_name:
    print("we have the same name")
else:
    print("our names do not match")

# 9)
# კონკანდინაცია ნიშნავს ტექსტების შეერთებას.
print('45' + "45") # ეს კოდი გამოიტანს 4545 , რადგან ბრჭყალებში ჩაწერილ რიცხვს კომპიუტერი აღიქვამს როგორც ტექსტს.

# 10)
s =int(input("enter number: "))
if s % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")