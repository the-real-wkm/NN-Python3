
#ipsum_file = open('files/ipsum.txt')

#region For Loop Example

# # This for loop reads through each individual line of text in the file and prints it
# # also strips the line of a return carriage to avoid extra spacing
# for line in ipsum_file:
#     print(line.rstrip())

#endregion

#region Seek / file.readlines() example

# # Resets cursor to start of file. By default at end from reading through each line in the for loop
# # file.seek([character in file you wish to be at])
# ipsum_file.seek(0)

# lines = ipsum_file.readlines()

#endregion

#region Reading a portion of a file / file.close() Example

# #Starting at character 50, read and print 100 characters
# ipsum_file.seek(50)
# file_text = ipsum_file.read(100)
# print(file_text)

# # Closes file so it does not remain open in background and affect performance
# ipsum_file.close()

#endregion

def sequence_filter(line):
    return '>' not in line

# Using the 'with' Keyword, you can interact with a file as an object with out having to
# close the file later.
with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    lines = list(filter(sequence_filter, lines))
    print(lines)
