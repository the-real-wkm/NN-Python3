num1 = 3.1425467389
num2 = 10.2903948


#region PREVIOUS

# print('#1 is', num1, 'and #2 is', num2)

#endregion

#region FORMAT METHOD

# You can use :.3 to assign a precision of 3 to the numbers (i.e. 3.14 / 10.2)
# You can also use :.3f to assign a precision of 3 spaces following the decimal to the numbers

# print('#1 is {0:.3f} and #2 is {1:.3f}'.format(num1, num2))

#endregion

#region USING F-STRINGS

print(f'#1 is {num1:.4f} and #2 is {num2:.4f}')

#endregion
