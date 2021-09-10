from random import randint

# List of common words I might say while playing games
knile_words = [
    'BrUh', 'Fuck', 'Heh', 'NO!', 'Shit', 'Help', 'Kek', 'Pepega', 'Snazzy', 'Interesting', 'Indeed'
    'Wat?', 'Stop'
]

# Prompting the User for paragraph count
userPrompt = input('How many paragraphs of customized Knile Ipsum? ')
paragraphs = int(userPrompt)

# Establishing file names as vars
ipsum = 'ipsum.txt'
knile_ipsum = 'knile_ipsum.txt'

# Function used to "Knilize" the lorem ipsum
def knilize(word):
    random_position = randint(0, len(knile_words) - 1)
    return f'{word} {knile_words[random_position]}'

# Open Original Lorem Ipsum file
with open(ipsum) as ipsum_original:
    # Read in file and split into list of words
    items = ipsum_original.read().split()

    # Clears file
    with open(knile_ipsum, 'w') as ipsum_knile:
        ipsum_knile.write('')

    # For each paragraph the user would like made
    for n in range(paragraphs):
        # "Knilize" the lorem ipsum and map it to a new list
        knile_text = list(map(knilize, items))

        # Open the knile_ipsum.txt file
        with open(knile_ipsum, 'a') as ipsum_knile:
            #Write the "knilized" lorem ipsum to the file.
            ipsum_knile.write(f"{' '.join(knile_text)} \n\n")
