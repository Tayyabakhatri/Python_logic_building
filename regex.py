# Q1 — Extract only digits
# Given string:
# "Order123 has tracking 4567 and code 89"
# Regex likho jo sirf numbers extract kare.

import re

# text = "Order123 has tracking 4567 and code 89"
# digits = re.findall(r"\d+", text)
# print("Extracted digits:", digits)


# Q2 — Extract all words
# Given string:
# "Hello, world! Python_3 is awesome."
# Regex likho jo sirf alphabetic words return kare (symbols ko ignore kare).



# text2 = "Hello, world! Python_3 is awesome."
# words = re.findall(r"[a-zA-Z]+", text2)
# print("Extracted words:", words)





# Q3 — Match specific pattern (3 letters + 3 digits)
# Example valid values:
# ABC123
# xyz987
# Regex banao jo isi pattern ko match kare
# match= "abc123 xyz987 wrong1 12ab34"
# pattern = re.findall(r"\d{3}[a-zA-Z]{3}",match)
# print("Matched patterns:", pattern)


# Q4 — Find all vowels
# String: "Regular Expressions Are Powerful!"
# Vowels (a, e, i, o, u) find karo.


# match= input("Enter a string , so that i will find all vowels in it: ")
# vowelPattern = re.findall(r"[aeiouAEIOU]",match)
# print("Vowels found:", vowelPattern)



# Q5 — Check if a string starts with 'py'
# Example:
# python
# pycharm
# pyramid
# Regex likho jo ‘py’ se start hone wale words identify kare.

# words="python pycharm pyramid java ruby"
# match=re.findall(r"^py",words)
# print("Words starting with 'py':", match)


# Q6 — Extract all mobile numbers
# "My numbers are 03451234567, 03007894512 and 111-222-333"
# Regex likho jo sirf Pakistani mobile numbers (03XXXXXXXXX) extract kare.
# userInput = input("Enter a mobile number , so that i will validate it: ")
# matchNum= re.findall(r"^03[0-4][0-9]{8}$",userInput)
# if matchNum:
#     print("Valid Pakistani mobile number ✔")
# else:
#     print("Invalid Pakistani mobile number ❌")
    
    
    
# 7 Question for Practice

# Tumhare paas dataset me 1000 mobile numbers hain.

# Task: Identify karna ke kitne valid Pakistan numbers hain

# Task: Invalid numbers ko new column me “Invalid” label do

# Extra Challenge:

# Identify karna ke kaun sa operator hai (Jazz, Ufone, Zong, Telenor) based on prefix.    

names = ["Ali", "Sara", "Ahmed", "Zoya", "Usman", "Hassan", "Ayesha", "Bilal", "Fatima", "Owais"]
mobiles = [
    "03001234567",  # valid Jazz
    "03451234567",  # valid Telenor
    "0356123456",   # invalid (short)
    "03123456789",  # valid Zong
    "04001234567",  # invalid (wrong prefix)
    "03211234567",  # valid Warid/Jazz
    "03351234567",  # valid Ufone
    "03001234",     # invalid (too short)
    "034512345678", # invalid (too long)
    "03601234567"   # invalid (6 not allowed after 03)
]

# for name, mobile in zip(names, mobiles):
#      print(name, "->", mobile)
     
# def is_valid_pakistani_number(number):
#     pattern = r"^03[0-4][0-9]{8}$"
#     return re.match(pattern, number)

# for name, num in zip(names, mobiles):
#     if is_valid_pakistani_number(num):
#         print(f"{name}  ->  {num}  ->  valid ")
#     else:
#         print(f"{name}  ->  {num} ->  invalid")
    
    
    
# Q8 — Extract only words that start with capital letter

# Strin="Ali is from Pakistan and he likes Python Programming"    

# reg= re.findall(r"\b[A-Z][a-z]*\b",Strin)
# print("Words starting with capital letter:", reg)


# Q9 — Match only valid emails
# From this text:
# "Contact us at help@gmail.com or admin@company.org, but not fake@com"
# fake@com match nahi hona chahiye.
# userInput= "Contact us at help@gmail.com or admin@company.org, but not fake@com"

# mat=re.findall(r'\.' , userInput)
# print(mat)

# Q10 — Regex
# Extract all emails from the string
# line = "Ali: ali@gmail.com, Sara: sara123@yahoo.com"

line = "Ali: ali@gmail.com, Sara: sara123@yahoo.com"

match=re.findall(r'\S@\S*',line)
print(match)



