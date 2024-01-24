from os import system, name


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


'''Printing coding ninjas five times'''
print('Coding Ninjas!\n' * 5)

'''Sleep for 5 seconds after printing coding ninjas five times'''
inp = input("Code: ")

'''Clearing the Screen after 5 second halt '''
clear()
