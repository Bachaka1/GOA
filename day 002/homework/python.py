# 1)
# debugging ნიშნავს პრობლემის აღმოფხვრას, როდესაც პროგრამისტი პოულობს და ასწორებს შეცდომებს.
# print(my_name)
# my_name = "Your name  როდესაც ვწერთ string_ს მაშინ სიტყვას თავში და ბოლოში უნდა დავუწეროთ ბრჭყალები.
# რადგან კომპიუტერი ჩვენს მიერ დაწერილ კოდს კითხულობს ზევიდან ქვევით, ჯერ უნდა შევქმნათ ცვლადი და შემდეგ გავუშვათ ეკრანზე print() ბრძანებით.

# 2)
a = 15
b = 3.5
print(a+b)

# 3)
c = 25
d = 5
print(c+d)
print(c-d)
print(c*d)
print(c/d)

# 4) გაასწორეთ შეცდომები.
#age = "25" integer_ს არ სჭირდება ბრჭყალები.
#print(age + 5)
age = 25
print(age + 5)

# 5)
name = "mamuka bachakashvili"
age = 16
city = "tbilisi"
result = " I am " + name + " " + str(age) + " years old, living in " + city
print (result)

# 6)
# total = 100
# print(totl)
# ეს კოდი ამოაგდებს errorს რადგან print() ბრძანებაში არასწორად წერია ცვლადის სახელი.

# 7)
total = 120
people = 4
print(total / people)

# 8)
price = 80
discount = 0.5
final_price = price - (price * discount)
print(final_price)

# 9)
number = 40

if number % 2 == 0:
   print ("The number is even")
else:
   print ("The number is odd")