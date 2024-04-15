import random as rand

global_user_list = []

# maybe make it so the list can be a specific type I.E list of strings, list of ints, or unspecified. 
# list of strings can be sorted alphabetically, list of int sorted by value

# list init 
def list_init():
    user_list = []
    while True:
        user_value = input('Command: EXIT, UNDO, GENERATE) \n Input list value: ')
        if user_value == 'EXIT':
            print(user_list)
            return user_list
        elif user_value == 'UNDO':
            user_list.pop()
        elif user_value == 'GENERATE':
            # generate a random list of ints with rand length ranging from 3-10 values long
            # generate how long the list is then generate each value
            user_list.clear()
            list_length = rand.randint(3,10)
            for i in range(list_length):
                user_list.append(rand.randint(0, 10))
            print(user_list)
            return user_list
        else:
            user_list.append(user_value)
            print(user_list)

def list_edit(user_list):
    while True:
        user_choice = int(input('Input choice: \n 1. Append list \n 2. Remove item \n 3. Remove specific index \n 4. Exit \n'))
        match user_choice:
            case 1:
                user_value = input('Input list value: ')
                user_list.append(user_value)
                print(user_list)
            case 2:
                pass
            case 3:
                pass
            case 4:
                print(user_list)
                break
            case _:
                print('Please input number \n')

global_user_list = list_init()
print('Your list: {}' .format(global_user_list))
list_edit(global_user_list)
