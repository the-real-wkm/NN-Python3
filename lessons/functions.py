
#region Example of a greeting function

#User and Day are default values allowing the function to be called with out that data being passed in.
# def greet(name = 'User', timeOfDay = 'Day'):
#     print(f'Good {timeOfDay} {name}, hope you are well!')

# name = input('Please enter your name: ')
# time = input('Please enter the time of day: ')

# greet(name, time)

#endregion

#region Area Function Example

# A function that takes in a radius to calculate the area of a circle
def calcArea(radius):
    area = 3.142 * radius ** 2
    return area

# A function that takes in the area of the ends and length of a cylendar to calculate the volume
def vol(area, length):
    vol = area * length
    print(vol)

# Collecting user input for the radius and casting to int
radius = int(input('Please enter a radius: '))
# Collecting user input for the length and casting to int
length = int(input('Please enter a length: '))

# Calculating and printing the volume
vol(calcArea(radius), length)

#endregion
