
#region For-Loop stuff

users = [ 'Foxy', 'RedWolf', 'Zeeker', 'Kyleptomaniac', 'SkullKid' ]

# print('\nUSERS:\n')

# for user in users:
#     print(f'\t{user}')

# print('\n')

# for user in users[1:4]:
#     print(user)

# for user in users:
#     if user == 'Zeeker':
#         print(f'{user}: Pleb of the Realm')
#         break
#     else:
#         print(user)

#endregion

#region While-Loop Stuff
age = 25
num = 0

while num < age:
    if num == 0:
        continue
    if num % 2 == 0:
        print(num)
    num += 1
    if num > 20:
        break

#endregion
