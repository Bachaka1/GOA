# 1)
correct_password = "password123"
attempts = 0
max_attempts = 3
success = False

while attempts < max_attempts and not success:
    user_input= input("enter password: ")
    attempts += 1
    if user_input == correct_password:
        success = True
        print("password is correct, access granted!")
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
         print(f"Incorrect password. You have {remaining} attempt(s) left.")
if attempts == max_attempts and not success:
   print("You have reached the maximum number of attempts.")


# 2)
print(True and False and 5 > 9 and 90 * 30 > 1089 or False and 'Nino' != '' or False or True and 56 * 2 > 90)
# true and false = false, false and false = false, false and true = false, false and true = false, true and true = true
# false or false = false, false or false = false, false or true = true
# საბოლოოდ გამოიტანს true-ს.

# 3)
# მასივი არის მონაცემთა სტრუქტურა, რომელიც საშუალებას გვაძლევს ერთ ცვლადში შევინახოთ ერთზე მეტი მნიშვნელობა.
# მასივში შეგვიძლია ნებისმიერი მონაცემთა ტიპის შენახვა მაგალითად: str, int, float, boolean და ა.შ.

# 4)
family_members = ("eduard", "sopiko", "salome", "mari", "mamuka")
for member in family_members:
   print(member)

# 5)
numbers = (43,16,21,35)
total = 0
for num in numbers:
   total += num
print(total)

# 6)
# Indexing ნიშნავს ელემენტზე წვდომას მისი მდებარეობის მიხედვით.
# ყველა ელემენტს აქვს თავისი ინდექსი, ინდექსით შეგვიძლია დავბეჭდოთ სიიდან ნებისმიერი ელემენტი.
# ინდექსის გამოყენება შეგვიძლია string-ზეც.

# 7)
# Indexing გვაძლევს საშუალებას სწრაფად და ზუსტად მივწვდეთ კონკრეტულ ელემენტს.
# ინდექსით შეგვიძლია ელემენტზე პირდაპირ წვდომა მაგალითად, სიიდან მხოლოდ პირველი ან ბოლო ელემენტის ამოღება.

# 8)
numbers = [10, 20, 30, 40, 50]
print (numbers[0])
print (numbers[2])
print (numbers[4])

text = "python"
print (text[0])
print (text[3])
print (text[4])

# 9)
fruits = ["apple", "banana", "orange", "grape", "pear", "lemon", "kiwi"]
every_second = fruits[0:None:2]
print(every_second)

# 10)
# python-ში for loop არ იღებს არგუმენტებს როგორც ფუნქცია, მაგრამ შეგვიძლია ერთ ციკლში მივიღოთ მრავალი მნიშვნელობა:
#Tuple unpacking
# enumerate()
# zip()
names = ["nika","luka"]
ages = [17,21]
for name, age in zip(names, ages):
   print(name, age)

cities = ["Paris","London"]
countries = ["France","UK"]
for city, country in zip(cities, countries):
   print(city, country)