
users = [ 'Foxy', 'RedWolf', 'Zeeker', 'Kyleptomaniac', 'SkullKid' ]

# region Print Users For-Loop
# print('\nUSERS:\n')

# for user in users:
#     print(f'\t{user}')

# print('\n')

# for user in users[1:4]:
#     print(user)

for user in users:
    if user == 'Zeeker':
        print(f'{user}: Pleb of the Realm')
        break
    else:
        print(user)
