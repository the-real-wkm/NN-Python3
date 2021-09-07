
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
        # Continue skips this iteration of the while loop. Must add one before continuing or num will never increase
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    if num > 20:
        break
    num += 1

#endregion
