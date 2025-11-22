# 1)
names = ["Anna", "Giorgi", "Nino", "Luka"]
for name in names:
    print(name)

# 2)
animals = ["dog", "cat", "elephant"]
first_animal = animals[0]
index_2 = first_animal[1]
print(index_2)

# 3)
items= ["A","B","C","D","E","F","G"]
selected=items[1:5]
print(selected)

# 4)
# ვქმნით რეალურ პაროლს, რომლის გამოცნობაც მომხმარებელს მოუწევს
real_password = 'Nino1234!'

# მაქსიმალური მცდელობების რაოდენობა
attempts = 3

# მომხმარებლის ამჟამინდელი მცდელობების რაოდენობა (დაწყება 0-დან)
user_attempts = 0

# while ციკლი იმუშავებს მანამ, სანამ მომხმარებლის მცდელობები attempts-ზე ნაკლებია
while attempts > user_attempts:
    
    # ვანგარიშობთ რამდენი მცდელობა დარჩა
    remaining = attempts - user_attempts
    
    # input() იღებს მომხმარებლის შეყვანილ პაროლს
    user_input = input(f'Guess the password again. You have {remaining} attempt(s) left: ')
    
    # ყოველი შემოყვანის შემდეგ მცდელობა 1-ით მატულობს
    user_attempts += 1

    # ვამოწმებთ მომხმარებლის შეყვანილი პაროლი ემთხვევა თუ არა რეალურ პაროლს
    if user_input == real_password:
        print('Congrats! You have guessed the correct password!')
        break  # სწორი პაროლის შემთხვევაში ციკლი წყდება
    else:
        print('Wrong, please try again!')

# ეს else იმუშავებს მხოლოდ მაშინ, break არ შესრულდება
else:
    print('You have reached the maximum number of attempts')

# 5)
# ფუნქცია — არის კოდის ნაწილი, რომელსაც სახელს ვარქმევთ და შემდეგ შეგვიძლია რამდენჯერაც მოგვინდება გამოვიყენოთ.
# ფუნქციები გვეხმარება თავიდან ავიცილოთ ერთი და იგივე კოდის გამეორება.
# ისინი ალაგებენ პროგრამას და ხდიან მას უფრო გასაგებს და სტრუქტურულს.

# 6)
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = numbers[6]
b = numbers[8]
print(a, b)

# 7)
user_inputs=[]
for i in range(5):
    text = input("enter text: ")
    user_inputs.append(text)
print(user_inputs)

# 8)
fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
fruits.append("date")
fruits.append("strawberry")

numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
numbers.extend([7, 8])
numbers.extend([9])
numbers.extend([])
numbers.extend([10, 11, 12])


colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
colors.insert(0, "black")
colors.insert(5, "white")
colors.insert(3, "pink")
colors.insert(len(colors), "orange")

pets = ["dog", "cat", "parrot", "rabbit"]
pets.remove("cat")
pets.remove("dog")
pets.remove("rabbit")


nums = [5, 2, 9, 1, 7]
nums.sort()
nums.sort(reverse=True)
nums2 = [3, 8, 0]
nums2.sort()
nums2.append(1)
nums2.sort()
nums2.sort(reverse=True)

# 9)
# შეგვიძლია ერთ list-ში შევინახოთ სხვადასხვა ტიპის მონაცემები.
# მაგალითად, list-ში ერთად შეიძლება იყოს:
# - მთელი რიცხვები (int)
# - ათწილადები (float)
# - სტრინგები (string)
# - ლოგიკური მნიშვნელობები (bool)