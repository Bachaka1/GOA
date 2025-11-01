# 1)
# ლოგიკური ოპერატორები გვეხმარება გადავწყვიტოთ, მართალია თუ არა რაღაც პირობა.
# მათი დახმარებით ვადარებთ პირობებს და ვიღებთ პასუხს: true ან false.
# მაგალითად:
# true or true = true
# true or false = true
# false or false = false
# true and true = true
# true and false = false

print(True and True or False or True and True and False)
# ვპოულობთ and_ებს: true and true = true, true and false = false. გამოდის: true or false or false = true


# 2)
name = input("enter your name: ")
age = int(input(" enter your age: "))
if name == "John" and age == 25:
    print("true")
else:
    print("false")


# 3)
num_1 = int(input("enter number 1: "))
num_2 = int(input("enter number 2: "))
num_3 = int(input("enter number 3: "))
total = num_1 + num_2 + num_3
avarage = total/3
print(avarage)


# 4)
# sequencing - ასრულებს კოდს ნაბიჯ-ნაბიჯ.
# მაგალითად: print(step 1), print(step 2), print(step 3).
# selection - ამოწმებს პირობას და ირჩევს მოქმედებას.
# მაგალითად:
age = 16

if age >= 18:
    print("you are an adult")
else:
    print("you are a kid")
# iteration - იმეორებს მოქმედებას.
# მაგალითად:
for i in range(5):
    print("hello", i)


# 5)
# for loop - გამოიყენება მოქმედების გამეორებისთვის.
# 3 არგუმენტის გადაცემა შევიძლია:
# start: რიცხვი, რომლითაც იწყება.
# stop: რიცხვი, სადაც შეწყდება.
# step: რამდენი ნაბიჯით უნდა გაზარდოს თითოეული ეტაპი.


# 6)
# For loop: გამოიყენება, როცა ცნობილია რამდენჯერ უნდა გამეორდეს.
# While loop: გამოიყენება, როცა არ არის ცნობილი რამდენჯერ უნდა გამეორდეს.


# 7)
num = int(input("enter number: "))
factorial = 1

for i in range (1, num + 1):
    factorial *= i
print(factorial)


# 8)
n = int(input("enter score: "))
if n >= 90:
    print("A")
elif n >= 80:
    print("B")
elif n >= 70:
    print("C")
else:
    print("F")


# 9)
a = int(input("enter num 1: "))
b = int(input("enter num 2: "))
c = int(input("enter num 3: "))

if a > b and a > c:
    print("highest num is", a)
elif b > a and b > c:
    print("highest num is", b)
else:
    print("highest num is", c)



# 10) 
number = 10
for i in range(0, number + 1):
    print(i)


# 11)
t = 0
for i in range(0,21):
    t += i
print(t)

# 12)
my_name = "mamuka"
for letter in my_name:
    print(letter)