nums = [1, 2, 3, 4, 5, 6]

#region Using a Function

# def square(n):
#     return n**2

# nums_squared = list(map(square, nums))

#endregion

#region Using a Lambda

# lambda [var]: [function]

nums_squared = list(map(lambda n: n**2, nums))
print(nums_squared)

#endregion
