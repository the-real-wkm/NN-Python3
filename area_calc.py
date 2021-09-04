# Use the pound sign/hashtag to comment.

#region Standard Input

# input( [string you would like to output/prompt with] )
# name: A new variable being set to the input provided.

# name  = input('Tell me your name please: ')
# age = input('What about your age? ')

# print('Hello ' + name + '!', 'You are', age, 'years old.')

#endregion

# Calc the area of a circle
# Data collected from input() is stored as a String
# int() can be used to type cast a variable as an integer
radius = input('Enter the radius of your circle (m): ')
area = 3.142 * int(radius) ** 2
print('The area if your circle is:', area)