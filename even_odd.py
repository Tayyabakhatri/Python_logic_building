# 1. Even or Odd (Without Using if-else)

# Take an integer input and check if it’s even or odd without using if or else (hint: use boolean logic or operators).


# userInput = input("Enter an integer: ")

# if userInput == "":
#     print("Please enter a valid integer.")
# else:
#     userInput = int(userInput)
#     even = userInput % 2 == 0
#     print("Even") if even else print("Odd")


#  2. Swapping Without Temp Variable

# Write a Python program to swap two numbers without using a third (temporary) variable.

# a= 10
# b= 20
# a= a+b
# print("After Step 1: a =", a, ", b =", b)
# b=a-b
# print("After Step 2: a =", a, ", b =", b)

# #now getting original values again
# b= a-b
# print("After Step 3: a =", a, ", b =", b)
# a= a-b
# print("After Step 4: a =", a, ", b =", b)


# 3. Common Elements in Two Lists

# Given two lists, find the common elements and store them in a new list.


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# for element in list1:
#     if element in list2:
#         print("Common element:", element)

# 4. Unique Words

# Given a string, print all the unique words (ignore case).
# Example: "Python is great and python is easy" → {'python', 'is', 'great', 'and', 'easy'}
# string= "Python is great and python is easy"
# newString= string.lower()
# words= newString.split()
# print(set(words))

# newString= string.lower()
# words= newString.split()
# for word in words:
#     if words.count(word)>1:
#         print("Duplicate word:", word)


# 5. Count Vowels

# Count the number of vowels (a, e, i, o, u) in a given string using a for loop and a counter variable.

find_vowels = "This is an example string to count vowels."
a = 0
e = 0
i = 0
o = 0
u = 0
for alp in find_vowels:
    if alp == "a":
        a += 1

    elif alp == "e":
        e += 1

    elif alp == "i":
        i += 1

    elif alp == "o":
        o += 1

    elif alp == "u":
        u += 1

# print("u are ",u)
# print("o are ",o)
# print("i are ",i)
# print("e are ",e)
# print("a are ",a)


# 6. Sum of Numbers in List

# Given a list of numbers, find the sum of all numbers that are greater than 10.
# Example= [5, 11, 20, 3, 15]

# a=0

# for num in Example:
#    a=a+num

# print("Sum is:", a)


# 7.  Unpack it into three separate variables and print them in a formatted string like:
# "My name is Tayyaba, I am 22 years old, and I love Python."
# info = ("Tayyaba", 22, "Python")
# (name,age,language)=  info
# print(f"my name is {name}, I am {age} years old ,and i lave {language}.")


# 8. Set Operations

# Create two sets and:

# Find their union, intersection, and difference.

# Print each result clearly.

# A= {1, 2, 3, 4, 5}
# B= {4, 5, 6, 7, 8}
# A_union_B = A.union(B)
# print("Union:", A_union_B)


# 9. Reverse a String

# Write logic to reverse a string without using slicing ([::-1]).

# num= "Hello, World!"
# reversed_num=num[::-1]
# print(reversed_num)


# 10. Second Largest Number

# From a list of integers, find the second largest number without using max() or sort().
numbers = [10, 25, 5, 40, 15]


# numbers=input("Enter numbers i will sum your numbers seperated by space: ").split()

# sum =0
# for num in numbers:
#     sum+=int(num)

# print("The sum of your numbers is:", sum)

# total=0
# while True:
#  userInput=input("enter price of items:")
#  if( userInput != "t"):
#   total=total+int(userInput)
#  else:
#      print("total price is:", total)
#      break


# 11. calculate the factorial of a given number
# 12. find the number of trailing zeros in the factorial of a given number

# userNumber = input("Enter a number to calculate its factorial: ")
# userNumber = int(userNumber)
# def factorial(n):
#     if n==0 or n==1:
#         return print(1)

#     else:
#            fact = 1
#     for i in range(2, n + 1):
#         fact *= i
#     return fact

# def trailing_zeros(fact):
#         count=0
#         while fact > 0 :
#          fact //= 5
#          count += fact
#          return count


# fac=factorial(userNumber)
# zeros= trailing_zeros(userNumber)

# print(f"factorial of {userNumber} is: {fac}")
# print(f"number of trailing zeros in factorial of {userNumber} is: {zeros}")

# 13. Find Missing Number in a List

# Given a list of numbers from 1 to N with one missing number, find the missing number.
# Example: [1,2,4,5] → missing = 3

# expected_set = set(range(1, 21))

# userInput = input("Enter numbers from 1 to 50 with one missing number, separated by spaces: ").split()
# number_set = {int(num) for num in userInput}
# print(number_set)
# newDict={}
# for num in expected_set:
#     if num not in number_set:
#         newDict[num]= num


# Print all missing numbers at once
# print("Missing numbers are:", list(newDict.values()))


# 14. Count Frequency of Each Character

# Given a string, count how many times each character appears.
# Example: "banana" → {'b':1,'a':3,'n':2}

# userI= input("Enter a Sentence to find the frequency of letters: ")
# char_freq = {}
# for char in userI:
#     if char in char_freq:
#         char_freq[char]+=1
#     else:
#         char_freq[char]=1


# print("Character frequency:", char_freq)


# 15. Check if Two Strings Are Anagrams

# Input: "listen", "silent"
# Output: True

# str1 = input("Enter first string: ")

# # Step 1: Check if first string is empty
# if str1 == "":
#     print("Please enter a valid string for first input")
#     # Exit program or stop further execution
# else:
#     # Step 2: Take second string
#     str2 = input("Enter second string: ")

#     # Step 3: Check lengths
#     if len(str1) != len(str2):
#         print("Not Anagrams")
#     # Step 4: Check anagram by sorting
#     elif sorted(str1) == sorted(str2):
#         print("Anagrams")
#     else:
#         print("Not Anagrams")


# 16
# import nltk

# nltk.download("words")
# from nltk.corpus import words

# # Load list of valid English words
# word_list = set(words.words())

# # Take user input
# str1 = input("Enter first word: ").strip().lower()
# str2 = input("Enter second word: ").strip().lower()

# # Check if either string is empty
# if not str1 or not str2:
#     print("Please enter valid words!")
#     exit()

# # 1️⃣ Check if both are real English words
# if str1 not in word_list:
#     print(f"'{str1}' is not a valid English word.")
# if str2 not in word_list:
#     print(f"'{str2}' is not a valid English word.")

# # If any one is invalid, no need to continue
# if str1 not in word_list or str2 not in word_list:
#     exit()

# print("Both words exist in English dictionary ✔")

# # 2️⃣ Check if they are anagrams
# if len(str1) != len(str2):
#     print("Not Anagrams ❌ (Different lengths)")
# elif sorted(str1) == sorted(str2):
#     print("Anagrams ✔")
# else:
#     print("Not Anagrams ❌")


# 17. Second Largest Number Without Using max()

# Input: [10, 22, 5, 75, 65]
# Output: 65


# inp = input("Enter numbers separated by space ,so that i will tell you the second largest of it: ").split()
# num_list =[int(num) for num in inp]
# ager everse method use krni ha tu index 1 pr second largest mile ga
# werna -2 pr bhi mil jaega:
# a= num_list.reverse()
# print("Second largest number is:", num_list[1])


#  18. Find All Pairs Whose Sum Is K

# Input: arr = [2, 7, 11, 15], k = 9
# Output: (2,7)

num = input(
    "Enter any two numbers separated by space , i will tell you wheather they are equlas to 10 or not: "
).split()
numList = [int(n) for n in num]
k = 10
total = numList[0] + numList[1]
if total == k:
    print(f"Yes, the sum of {numList[0]} and {numList[1]} is equal to 10.")

else:
    print(f"No, the sum of the {numList[0]} and {numList[1]} is not equal to 10.")
