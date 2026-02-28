# ფუნქცია არის კოდის ბლოკი, რომელსაც აქვს სახელი და ასრულებს კონკრეტულ მოქმედებას.
# პარამეტრი არის ცვლადი, რომელიც იწერება ფუნქციის გამოცხადების დროს ფრჩხილებში.
# არგუმენტი არის რეალური მნიშვნელობა, რომელსაც გადავცემთ ფუნქციას გამოძახების დროს.

def check_even_or_odd(number):
    
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


check_even_or_odd(10)


# len() აბრუნებს ობიექტის სიგრძეს
numbers = [1, 2, 3, 4]
print(len(numbers)) 

# type() გვიჩვენებს თუ რა ტიპის მონაცემია
x = 10
print(type(x))

# input() საშუალებას გვაძლევს მივიღოთ მონაცემი მომხმარებლისგან
name = input("enter your name: ")
print("hello" + name)