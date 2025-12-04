# 1)
numbers = [10,20,30,40,50,60,70,80]
selected=numbers[1:6]
print(selected)

# 2)
# Indexing - აბრუნებს ერთ კონკრეტულ ელემენტს.
# Slicing - აბრუნებს ელემენტების დიაპაზონს.

# 3)
#append() – ელემენტის დამატება.
numbers = [1, 2, 3]
numbers.append(4)
print(numbers) 

fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)

# pop() –  ელემენტის ამოღება.
colors = ["red", "green", "blue"]
colors.pop()
print(colors)

letters = ["A", "B", "C"]
letters.pop(0)
print(letters)

# insert() – ელემენტის შეტანა კონკრეტულ ინდექსზე.
nums = [1, 3, 4]
nums.insert(1, 2)
print(nums)

cities = ["Tbilisi", "Batumi"]
cities.insert(0, "Kutaisi")
print(cities)

# remove() – შლის ელემენტს მნიშვნელობით.
nums2 = [1, 2, 3, 2]
nums2.remove(2)
print(nums2)

fruits2 = ["apple", "banana", "apple"]
fruits2.remove("apple")
print(fruits2)