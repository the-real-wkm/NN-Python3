grades = ['A', 'B', 'F', 'C', 'F', 'A']

#filter(testing_function, grades)

def remove_failing_grades(grade):
    return grade != 'F'

filtered_grades = list(filter(remove_failing_grades, grades))
print(filtered_grades)

#region For Loop Example

# filtered_grades = []

# for grade in grades:
#     if grade != 'F':
#         filtered_grades.append(grade)

# print(filtered_grades)

#endregion

#region Comprehension Method Example

# filtered_grades = [ grade for grade in grades if grade != 'F']
# print(filtered_grades)

#endregion
