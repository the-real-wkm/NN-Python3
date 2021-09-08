# List Comprehension Examples

# Double prize money weekend bonanza

prizes = [ 5, 10, 50, 100, 1000]
doubled = []

for prize in prizes:
    double = prize * 2
    doubled.append(double)

print(prizes)
print(doubled)

# Comprehension Method

doubled = [ prize*2 for prize in prizes]

print(doubled)

# Squaring Numbers

nums = list(range(1, 11))
squared_even_nums = []

for num in nums:
    if (num**2) % 2 == 0:
        squared_even_nums.append(num**2)

print(squared_even_nums)

# Squaring using Comprehension Method
squared_even_nums = [ num ** 2 for num in nums if (num ** 2) % 2 == 0 ]

print(squared_even_nums)
