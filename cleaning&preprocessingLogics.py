import statistics

# import my_string as rl

# userInput = input(
#     "Enter elements of list separated by space , so that i will reverse it for you: "
# ).split()
# numList = [int(num) for num in userInput]
# a = rl.reverseList(numList)

# Q1 — Remove Outliers

# A list of product prices is given:
product = [120, 130, 125, 121, 122, 4000, 119, 118, 115, 117]
product.sort()
print(product)
n = len(product)

#finding median of lower
middleIndex = n // 2  #value is 122
a=(middleIndex)+1 # value is 4000
value1=product[middleIndex]
value2=product[a]
sum=value1+value2
div=sum/2



lower_half = product[:middleIndex]
print(lower_half)

# short method
print(statistics.median(product))

# median formula 1 for odd numbers n+1/2
# median formula 2 for even numbers (n/2 and (n/2)+1)/2
