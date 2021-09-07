starter_pkmn = {}

def promptToContinue():
    if len(starter_pkmn) == 0:
        return True
    else:
        addAnother = input('Do you want to add another Pokemon? (Enter y to add more!): ')
        if addAnother == 'y':
            return True
        else:
            return False

def starterTypings(dict):
    for key, val in dict.items():
        print(f'{key} is a {val} type Pokemon!')

def typeCounts(dict):
    types = list(dict.values())
    for t in set(types):
        count = types.count(t)
        print(f'There are {count} {t} type starters.')


while promptToContinue():
    starter = input('Starter Pokemon Name: ')
    typing = input('Start Pokemon Type: ')

    starter_pkmn[starter] = typing

print('\n\n--------------\n')
starterTypings(starter_pkmn)
typeCounts(starter_pkmn)
