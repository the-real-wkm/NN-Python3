
write_file = 'files/written.txt'

#  Writing to a file deletes all contents of a file and writes the provided content
with open(write_file, 'w') as written_file:
    written_file.write('This string has been added to the written.txt file as a line of text.')

# Appending to a file leaves the file contents alone and writes the new content at the end.
with open(write_file, 'a') as written_file:
    written_file.write('\nhere is a second string of text on a new line!')

quotes = [
    '\nDon\'t Dream It, Be It.',
    '\nFuck the police coming straight from the underground.',
    '\nWe\'re all dogs in gods hot car.'
]

with open(write_file, 'a') as written_file:
    written_file.writelines(quotes)
