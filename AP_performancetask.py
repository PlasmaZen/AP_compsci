import random as rand

global_user_list = []

# maybe make it so the list can be a specific type I.E list of strings, list of ints, or unspecified. 
# list of strings can be sorted alphabetically, list of int sorted by value

# list initializer 
def list_init():
    user_list = []
    while True:
        user_value = int(input('Finish: -1, Undo: -2, Generate: -3 \n Input integer: '))
        if user_value == -1:
            print(user_list)
            return user_list
        elif user_value == -2:
            user_list.pop()
            print(user_list)
        elif user_value == -3:
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
        user_choice = int(input('Append list: 1, Remove last: 2, Remove specific index: 3, Remove section: 4, Exit: 5 \n Input Integer: '))
        if user_choice == 5:
            break
        match user_choice:
            case 1:
                user_value = input('Input integer: ')
                user_list.append(user_value)
                print(user_list)
            case 2:
                user_list.pop()
                print(user_list)
            case 3:
                user_value = int(input('Input value to remove (List starts at 0): '))
                user_list.pop(user_value)
                print(user_list)
            case 4:
                pass
            case 5:
                print(user_list)
                break
            case _:
                print('Please input valid int\n')

global_user_list = list_init()
while True:
    print('Your list: {}' .format(global_user_list))
    list_edit(global_user_list)
