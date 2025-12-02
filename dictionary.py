# 1 Create a dictionary for a student containing: name, age, roll_no.
# Print each value using keys.

# student={
#     "name":"John Doe",
#     "age":20,
#     "roll_no":101
# }
# for x in student:
#     print(x ,":" ,student[x])

# 2 Given a dictionary:
car = {"brand": "Toyota", "year": 2020}

# Use get() to access "model" and provide a default message if not found.

# a = car.get("model")
# print(a)
# if a is None:
#     car.setdefault("model", "BMW")
#     print(car)

# 3 Write a program that asks user for 3 fruits and stores
# them as key-value pairs where key is fruit name and value is its color.


# dict = {}
# num = 0
# while num <= 2:
#     num = num + 1
#     fruit = input(f"Enter fruit name {num}:")
#     color = input("Enter its color ")
#     dict[fruit] = color
# print(dict.items())


# 4 Print all keys, values, and key-value pairs using loops.
data = {"a": 1, "b": 2, "c": 3}

#method #1
# for k in data:
#     print(k) #key
#     print(data[k])#value
#     print(k, " :",data[k]) #key value pair

#method 2
for j in data:
    print(data.keys())
    print(data.values())
    print(data.items())


#5 Write a program using items() to print:
# key = x , value = y

dict={
    "a":"b",
    "c":"d",
    "e":"f"
}
print(dict.items())


#6 Create a person dictionary and update it with "city": "Karachi" using update().
person={
    "name":"Tayyaba",
    "age":26,
}
#method 1
person["country"]="pakistan"
#method 2
person.update({"city":"karachi"})
print(person)

#7 Combine two dictionaries using update().
dict_1={
    "a":"b",
    "c":"d",
}
dict_2={
    "e":"f",
    "g":"h"
}
dict_1.update(dict_2)
print(dict_1)



  #8 Remove key "y" using pop().
d = {"x":10, "y":20, "z":30}

# d.pop("y")
# print(d)


#9 Remove the last inserted item using popitem() and print updated dictionary.

# d.update({"a":"40"})
# print(d)
# d.popitem()
# print(d)

#10 Delete a specific key using del and clear the dictionary using clear().
 
# del d["x"]
# print(d)

# d.clear()
# print(d)

