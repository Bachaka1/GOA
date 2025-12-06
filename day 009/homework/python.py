# 1)
# Default parameters არის პარამეტრები, რომლებსაც თავიდანვე აქვთ მნიშვნელობა.
# თუ ფუნქციის გამოძახებისას არ გავცემთ მნიშვნელობას, გამოიყენება default მნიშვნელობა.

# return არის სიტყვა, რომელიც ფუნქციას აძლევს შედეგის დაბრუნების შესაძლებლობას.
# ეს საშუალებას გვაძლევს, რომ ფუნქციის მიერ გამოთვლილი მნიშვნელობა გამოვიყენოთ სხვაგან.

# 2)
def which_is_greater(a, b):
    if a > b:
        print("The first number is greater than the second number")
    elif b > a:
        print("The second number is greater than the first number")
    else:
        print("They are equal to each other")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

which_is_greater(num1, num2)

# 3)
def sum_array(array):
    total = 0
    for num in array:
        total += num
    return total
array_input = input("Enter numbers separated by space: ")
array = [int(x) for x in array_input.split()]
result = sum_array(array)
print("The sum of the array is:", result)

# 4)
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

user_text = input("Enter a text: ")

vowel_count = count_vowels(user_text)
print("Number of vowels in the text:", vowel_count)

# 5)
def is_palindrome(text):
    text = text.lower()
    if text == text[::-1]:
        print("This text is palindrome")
    else:
        print("This text is not a palindrome")

user_text = input("Enter a text: ")

is_palindrome(user_text)

# 6)
def is_uppercase(text):
    if text.isupper():
        return True
    else:
        return False

user_text = input("Enter a text: ")

result = is_uppercase(user_text)
print(result)

# 7)
# list method
fruits = ["apple", "banana", "cherry"]

# append() - ელემენტის დამატება ბოლოში
fruits.append("orange")
# insert() - ელემენტის დამატება მითითებულ პოზიციაზე
fruits.insert(1, "kiwi") 

# string methods
text = " Hello World "

# upper() - დიდი ასოებში გადაყვანა
print(text.upper())

# lower() - პატარა ასოებში გადაყვანა
print(text.lower())

# 8)
def remove_duplicates(array):
    unique_elements = []
    for item in array:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements

array_input = input("Enter numbers separated by space: ")
array = [int(x) for x in array_input.split()]

result = remove_duplicates(array)
print("Array without duplicates:", result)