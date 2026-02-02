# string= "Python is great and python is easy"
# newString= string.lower()
# words= newString.split()
# searcjhword= input("Enter word to search: ").lower()
# newdict= {}
# for word in words:
#     if word == searcjhword:
#         if word in newdict:
#             newdict[word] += 1
#         else:
#             newdict[word] = 1
# print(newdict)

# 1 ✅ STRING COMPLETE PRACTICE PACK
# ⭐ Level-1: Beginner Questions
# Count vowels in a string.

# Count consonants in a string.

# Check if a string is palindrome.

# Reverse a string without using slicing.

# Check if two strings are anagrams.

# Find length of string without using len().

# Convert string to uppercase/lowercase without using built-in functions.

# Count spaces in a string.

# Count digits in a string.

# Count special characters.

# 1 Count vowels in a string.

# inputString = input("Enter a string , so that i will count number of vowels in it: ")
# vowels = "aeiouAEIOU"
# dict = {}
# for char in inputString:
#     if char in vowels:
#         if char in dict:
#             dict[char] += 1
#         else:
#             dict[char] = 1

# print("Vowel count is:", dict)


# inputString = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# counts = {}

# for ch in inputString:
#     if ch in vowels:
#         counts[ch] = counts.get(ch, 0) + 1

# print(counts)

# 2 Count consonants in a string.
# inputString = input("Enter a string , so that i will count number of consonants in it: ")
# vowels = "aeiouAEIOU"
# dict = {}
# for char in inputString:
#     if char not in vowels:
#         if char in dict:
#             dict[char] += 1
#         else:
#             dict[char] = 1

# print("Vowel count is:", dict)

# 3 Check if a string is palindrome.
# import nltk
# nltk.download('words')
# from nltk.corpus import words
# wordList = words.words()
# inputString = input("Enter a string , so that i will check whether it is palindrome or not: ").lower()


# def isPalindrome(s):
#     return s == s[::-1]
# if not inputString:
#     print("string is empty")
#     exit()

# if inputString.lower() not in wordList:
#     print("Not a valid word")
#     exit()
# if inputString in wordList:
#     print("Valid word")
#     palindrome= isPalindrome(inputString)
#     print("string is palindrome", palindrome)



# 4 Reverse a string without using slicing.
# string="he is a boy"
# string = string.split()
# reversedString = string.reverse()
# print("Reversed string is:", string)


# 5 Check if two strings are anagrams.

# inp1 = input("Enter first string: ").strip().lower()
# inp2 = input("Enter second string: ").strip().lower()
# if  not inp1 or not inp2:
#     print("please enter valid strings")
#     exit()
#     # Check if both are valid words
# if inp1 not in wordList:
#     print(f"'{inp1}' is not a valid English word.")
#     exit()
# if inp2 not in wordList:
#     print(f"'{inp2}' is not a valid English word.")
#     exit()
# print("Both words exist in English dictionary ✔")
# #check anagram
# if len(inp1)!= len(inp2):
#     print("Not Anagrams ❌ (Different lengths)")
# elif  len(inp1)== len(inp2):
#     if sorted(inp1) != sorted(inp2):
#         print("Not Anagrams ❌")

# else:
#  sorted(inp1) == sorted(inp2)
#  print("Anagrams ✔")


# 6 Find length of string without using len().
# inputString = input("Enter a string , so that i will find length of it: ")
# count= 0
# if inputString=="":
#     print("String is empty")
#     exit()
# for char in inputString:
#     if char == " ":
#         continue
#     count +=1
# print ("Length of string is:", count)


# 7 Convert string to uppercase/lowercase without using built-in functions.
# inputString = input("Enter a string , so that i will convert it to uppercase into lowercase and viseversa: ")
# if inputString=="":
#     print("String is empty")
#     exit()
# for char in inputString:
#     if 'a' <= char <= 'z':
#         upperChar = chr(ord(char) - 32)
#         print(upperChar, end="")
#     elif 'A' <= char <= 'Z':
#         lowerChar = chr(ord(char) + 32)
#         print(lowerChar, end="")
#     else:
#         print(char, end="")

# 8 Count vowels using ord()
# Input: "Hello World"
# Count vowels (a, e, i, o, u) using ASCII comparison
# inputString = input("Enter a string , so that i will count number of vowels in it: ")
# if inputString=="":
#     print("String is empty")
#     exit()
# for char in inputString:
#     if char == " ":
#         continue
#     else:
#         if ord(char) in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]:
#             print(char)

# 9 Swapcase manually using ord() / chr()
# Input: "PyThOn"
# Output: "pYtHoN"
# inputString = input("Enter a string , so that i will swapcase it for you: ")
# if inputString=="":
#     print("String is empty")
#     exit()
# for char in inputString:
#     if "a" <= char <= "z":
#         upperChar = chr(ord(char)-32)
#         print(upperChar)
#     elif "A" <= char <= "Z":
#         lowerChar = chr(ord(char) +32)
#         print(lowerChar)


# 10: Convert all lowercase to uppercase using upper() method

# Input: "hello" → "HELLO"
# userInput = input("Enter a string , so that i will convert it to uppercase for you: ")
# upperString = userInput.upper()
# print("Uppercase string is:", upperString)


# 11: Identify uppercase and lowercase letters using isupper() / islower()

# Input: "PyThOn123"

# userInput = input(
#     "Enter a string , so that i will identify uppercase and lowercase letters for you: "
# )
# upper=""
# lower=""
# for char in userInput:
#     if char.isupper():
#         upper = f"{userInput} is Uppercase"

#     else:
#         if char.islower():
#             lower = f"{userInput} is Lowercase"

# print(lower)
# print(upper)


# strip and lstrip and rstrip


# 12 User se ek string lo. Leading aur trailing spaces remove karke print karo.

# userInput = input("Enter a string with leading and trailing spaces: ")
# strippedString = userInput.strip()
# print("String after removing leading and trailing spaces:", strippedString)

# 13 Ek string "---Hello---" di hui hai.
# strip('-') use kar ke output print karo.
# userInput = "---Hello---"
# strippedString = userInput.strip("-")
# print("String after removing leading and trailing '-':", strippedString)


# 14 Input: " Python "
# lstrip() use karke sirf left side ke spaces remove karo.
# userInput = "     Python "
# leftString=userInput.lstrip()
# print("String after removing leading spaces:", leftString)


# 15 Input: "Python......"
# rstrip('.') use karke dots remove karo.

# userInput = "Python......"
# rightString=userInput.rstrip('.')
# print("String after removing trailing dots:", rightString)


# 16 User se string lo:
# "***I Love Coding***"
# strip('*') use karo.


# userInput = "***I Love Coding***"
# strippedString = userInput.strip('*')
# print("String after removing leading and trailing '*':", strippedString)

# 17  Check karo ke input string empty to nahi after using strip().
# Agar empty ho to print "Empty string"
# Example: " " → Empty string

# userInput = input("Enter a string with spaces: ")
# strippedString = userInput.strip()
# if not strippedString:
#     print("Empty string")
# else:
#     print("String after removing leading and trailing spaces:", strippedString)

# 18  Input: "0001234000"
# 000 ko left se remove karna hai (sirf lstrip use karo).
# Expected: "1234000"

# stringInput = "0001234000"
# leftString= stringInput.lstrip("0")
# print("String after removing leading zeros:", leftString)


# 19 Input: "0001234000"
# 000 ko right se remove karna hai (sirf rstrip use karo).
# Expected: "0001234"

# stringInput = "0001234000"
# rightString= stringInput.rstrip("0")
# print("String after removing trailing zeros:", rightString)


# 20  User multiple comma se values enter karta hai:
# ",,,apple,banana,orange,,,"
# strip(',') use kar ke clean list banao.
# Output: "apple,banana,orange"


# userInput = ",''''''',,apple,banana,orange,,....,"
# strippedString = userInput.strip(",.'")
# print("String after removing leading and trailing commas and dots:", strippedString)

# 21  User se sentence lo, jitne bhi newline characters \n aur tab \t hain strip karo.

# userInput = "\n\tHello, World!\n\t"
# print(userInput)
# strippedString = userInput.strip("\n\t")
# print("String after removing leading and trailing newlines and tabs:", strippedString)


# 22  Ek log file ki line di hui hai:
# "#### Error: File not found ####"
# Tumhe sirf hashtags (#) remove karne hain, text safe rehna chahiye.
# Expected:
# "Error: File not found"

# inputString = "#### Error: File not found ####"
# cleanedString = inputString.strip("# ")
# print("Cleaned string:", cleanedString)


# 23 User input email:
# " myemail@gmail.com "
# Spaces strip() se remove karo
# Aur validate karo ke email correct format me hai.


# 24  You have multiple strings:
# "----Python----"
# "****Java****"
# "~~Ruby~~"
# Ek program banao jo automatically side characters detect karke strip kare, bina manually character type kiye.
userInput = input("Enter multiple strings separated by comma: ")


def stripList(strings):
    result = []
    wordList = strings.split(",")
    for s in wordList:
        strippedString = s.strip("`~!@#$%^&*()_=+[]{}|;:'\",.<>?/ -")
        result.append(strippedString)
    return result

strippped=stripList(userInput)
print("Stripped strings are:", strippped)
   
# 25 ⭐ Intermediate Logic Questions
#  — Loop / Condition
# 1 se 50 tak numbers print karo, lekin:
# Agar number 3 se divisible ho → "Fizz" print karo
# Agar number 5 se divisible ho → "Buzz" print karo
# Agar dono se divisible ho → "FizzBuzz" print karo

# for num in range(1,51):
#     if num % 2 ==0:
#         print(f'{num}fizz')
#     elif num % 3 == 0:
#         print(f'{num}buzz')
#     elif num %2 ==0 and num %3 == 0:
#         print(f'{num}fizzbuzz')    
        
# 26 — String / Count
# text = "Python is Powerful Programming"
# Count karo kitne words capital letter se start ho rahe hain.
# Hint: .split() aur [0].isupper() use kar sakte ho

# text = "Python is Powerful Programming"
# text1= text.split()
# for txt in text1:
#     if txt[0].isupper():
#         print(txt)

#27 Calculate karo sum of all even numbers
# nums = [4, 7, 1, 9, 2]
# count=0
# for n in nums:
#     if n % 2==0:
#         count=count+n

# print(count)    

# 28 — Nested Loops
# Star pattern print karo:
# *
# **
# ***
# ****
# Hint: loop ke andar loop use hoga
# stri="*"
for p in range(1,6):
    for q in range(p) :
        print("*",end="")
    print()      









