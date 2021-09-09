from random import shuffle

words = ['Kyogre', 'Groudon', 'Rayquaza']
anagrams = []

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

#region Mapping Example
anagrams = list(map(jumble, words))
print(anagrams)
#endregion

#region For Loop Example
# for word in words:
#     anagrams.append(jumble(word))

# print(anagrams)
#endregion

#region Comprehension Method

# anagrams = [jumble(word) for word in words]
# print(anagrams)

#endregion
