# 1)
weather = "sunny"

if weather == "sunny":
    print("wear a hat")
elif weather == "rainy":
    print("wear boots")
elif weather == "cloudy":
    print("wear a jacket")
else:
    print("wear a T-shirt")

# 2)
# if ვიყენებთ მაშინ, როცა ვამოწმებთ პირველ პირობას.
# elif ვიყენებთ როცა ვამოწმებთ დამატებით პირობას,
# მხოლოდ იმ შემთხვევაში თუ if პირობა არ შესრულდა.


# 3)
# მომხმარებელს ვთხოვთ შეიყვანოს სახელი
name = input('Enter your name: ')

# ვქმნით ცვლადს, სადაც ჩამოთვლილია ყველა ხმოვანი ასო 
vowels = 'aeiouAEIOU'

# ვქმნით ცვლადს, რომელიც დაითვლის რამდენი ხმოვანი ასოა სახელში
count = 0

# ვატარებთ ციკლს სახელის თითოეულ ასოზე
for i in name:
    if i in vowels:
        count = count + 1

# ვბეჭდავთ შედეგს — რამდენი ხმოვანი ასოა შეყვანილ სახელში
print(count)

# 4)
# for მუშაობს მხოლოდ: string, range()