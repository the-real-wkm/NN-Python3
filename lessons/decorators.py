
def cough_dec(func):
    
    def func_wrapper():
        #code before function
        print('\n*cough cough*')
        func()
        #code after function
        print('*cough*\n')
    
    return func_wrapper

@cough_dec
def question():
    print('Can you give me a discount on that?')

@cough_dec
def answer():
    print("It's only 50 cents man.")

question()
answer()
