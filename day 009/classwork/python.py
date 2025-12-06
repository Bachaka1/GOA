# 1)
# პარამეტრი არის სახელი, რომელიც ფუნქციის გამოცხადებაში გვხვდება.
# არგუმენტი არის რეალური მონაცემი, რომელიც ფუნქციას გადაეცემა გამოძახების დროს.

# 2)
# 1) ვიწყებთ def საკვანძო სიტყვით

# 2) ვამატებთ ფუნქციის სახელს

# 3) ფრჩხილებში ვწერთ პარამეტრებს (სურვილისამებრ)

# 4) ვამთავრებთ ხაზს ორ წერტილით :

# 5) შემდეგ ხაზებში უნდა იყოს დაცული ინდენტაცია

# 6) თუ გვინდა, რომ ფუნქციამ მნიშვნელობა დააბრუნოს — ვიყენებთ return

# 3)
# ფუნქციები არის კოდის ბლოკები, რომლებსაც კონკრეტული ამოცანა აქვთ.
# ისინი გამოიყენება იმისთვის, რომ თავიდან ავიცილოთ კოდის გამეორება,
# გავამარტივოთ პროგრამის სტრუქტურა და გავხადოთ კოდი მარტივად შესაცვლელი.

# 4)
def check_number(num):
    if num % 2 == 0:
     print("even")
    else:
     print("odd")
number = int(input("enter number: "))
check_number(number)

# 5)
def count_number(array, number):
  count = 0
  for item in array:
    if item == number:
      count += 1
  return count

array_input = input("Enter numbers separated by space: ")
array = [int(x) for x in array_input.split()]

num = int(input("Enter the number to search: "))

result = count_number(array, num)

print("The number appears", result, "times.")