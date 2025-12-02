import math

# 1. Write a function to return the square of a number.

# Input: 4 → Output: 16

# num = input("Enter a number to find its square: ")
# num = int(num)


# def square(n):
# return n**2
# return  pow(n,2)
# return math.pow(n, 2)  # ye flooat men dega


# result = square(num)
# print("Square is:", result)


# 2. Write a function that takes two numbers and returns their sum.
# Input: 3, 7 → Output: 10

# userInput = input(
#     "Enter two numbers separated by space , i will sum them for you: "
# ).split()
# numList = [int(n) for n in userInput]


# def sumOfNumbers(num1, num2):
#     return num1 + num2


# result = sumOfNumbers(numList[0], numList[1])
# print("Sum is:", result)


# 3. Write a function to check whether a number is even or odd.

# Input: 5 → Output: Odd

# b = input("Enter a number to check whether it is even or odd: ")
# b = int(b)
# def evenOdd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# res= evenOdd(b)
# print(f"The number {b} is {res}")


# 4. Write a function that returns the factorial of a number.

# Input: 5 → Output: 120

# userInput = input("Enter a number to find its factorial: ")
# userInput = int(userInput)


# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         fact = 1
#         for i in range(2, num+1):
#             fact *= i
#         return fact
# result = factorial(userInput)
# print(f"The factorial of {userInput} is: {result}")


# 5. Write a function that takes a list and returns the maximum element.

# Input: [3, 6, 2, 8] → Output: 8

# maxInput = input("Enter numbers separated by space , so that i will tell you the maximum number: ").split()
# numList = [int(num) for num in maxInput]

# def maxInList(numList):
#     numList.sort()
#     return numList[-1]

# maximum = maxInList(numList)
# print("The maximum number in the list is:", maximum)


#  ✅ Intermediate Level Problems
# 6. Write a function to count the number of vowels in a string.

# Input: "hello" → Output: 2
# stringInput = input("Enter a string , so that i will count number of vowels in it: ")


# method 1
# def countVowels(v):
#     count =0
#     vowels = "aeiouAEIOU"
#     if len(v)==0:
#         print("String is empty")
#         exit()
#     else:
#         for char in v:
#             if char in vowels:
#                 count +=1
#     return count

# vowelCount = countVowels(stringInput)
# print("Number of vowels in the string is:", vowelCount)


# method 2
# dict={}
# def vowelCountDict(stringInput):
#  for char in stringInput:
#     if char in "aeiouAEIOU":
#         if char in dict:
#             dict[char] +=1
#         else:
#             dict[char] =1

# vowelCountDict(stringInput)
# print("Vowel count dictionary is:", dict)


# 7. Write a function that returns the reverse of a list.
# Without using reverse() or slicing.

# method 1 using slicing
# listInput = input("Enter elements of list separated by space , so that i will reverse it for you: ").split()
#  method 1
# numList = [int(num) for num in listInput]
# def reverseList(lst):
#  print(lst[::-1])

# reverseList(numList)

# method 2
# if len(listInput)==0:
#     print("List is empty")
#     exit()

# finalList=[]

# for i in listInput:
#     if i.isdigit():
#         finalList.append(int(i))
#     else:
#         finalList.append(i)


# def reverseList(lst):
#   print(lst[::-1])

# reverseList(finalList)


#  5. Find All Pairs Whose Sum Is K

# Input: arr = [2, 7, 11, 15], k = 9
# Output: (2,7)

# userInput = input(
#     "Enter numbers separated by space , so that i will find pairs whose sum is k: "
# ).split()
# k = 10
# numList = [int(num) for num in userInput]
# if numList[0] + numList[1] == k:
#     print(f"({numList[0]},{numList[1]}) is equals to {k}")
# else:
#     print(f"({numList[0]},{numList[1]}) is not equals to {k}")
    
    
#match function
name = "tayyaba khatri"
match name:
    case "tayyaba khatri":
        print("Hello Tayyaba!")
    case "john doe":
        print("Hello John!")    
    case _:
        print("Hello Stranger!") #default case
