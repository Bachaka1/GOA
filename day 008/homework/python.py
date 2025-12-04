# 1)
# ფუნქცია Python-ში არის კოდის ბლოკი, რომელსაც აქვს სახელი და შეგვიძლია გადავცეთ არგუმენტები.

# 2)
numbers = [10, 20, 30, 40, 50]

index_of_30 = numbers.index(30)
print(index_of_30)

for i in range(len(numbers)):
    print(numbers[i],i)

# 3)
names = ["example_name", "example_name_2", "example_name_3", "example_name_4"]
index = int(input("enter number: "))
text = input("enter name: ")
names.insert(index, text)
print(names)


# 4)
name = input("enter your name: ")
formatted_name = name.capitalize()
print(formatted_name)

# 5)
# function: ფუნქცია არის კოდის ნაწილი, რომელიც არ ეკუთვნის კონკრეტულ ობიექტს. ფუნქციის გამოძახება შეგვიძლია სახელით.
# method: მეთოდი არის ფუნქცია, რომელიც ეკუთვნის კონკრეტულ ობიექტს. მეთოდის გამოძახება შეგვიძლია ობიექტზე.

# 6)
name1 = '    N I N O     '
name2 = name1.strip()
print(name2)

# 7)
def greet(name_1):
    print("hello", name_1)
greet("mamuka")