import re


with open("resume.txt") as file:
    text = file.readlines()

# print(text)


for line in text:

    # check email through regex
    email_mactch = re.search(r"\S+@\S+", line)
    if email_mactch:
        print(email_mactch.group())

    # check number through regex
    number = re.search(r"03[0-4][0-9]{8}", line)
    if number:
        print(number.group())

    # check skill
    skill = re.findall(r"\bsql\b|\bpython\b|\bpowerbi\b|\bexcel\b", line, re.IGNORECASE)
    if skill:
        print(skill)

    # check experiance
    exp = re.search(r"experiance[:\s]*(\d+)", line, re.IGNORECASE)
    if exp:
        print(exp.group())
