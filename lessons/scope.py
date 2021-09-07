
# Global Scope Variable // Accessible inside and outside of functions
user = 'Foxy'

# def print_user():
#     Calling Global Variable from inside the function to assign it
#     global user
#     user = 'RedWolf'
#     print(f'The user inside the function is {user}')

def print_user():
    # Local Variable // Accessible only inside this function
    user = 'RedWolf'
    print(f'The user inside the function is {user}')

print_user()
print(f'The user outside the function is {user}')
