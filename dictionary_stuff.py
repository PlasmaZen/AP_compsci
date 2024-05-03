def make_dict():
    user_dict = {} 
    while True:
        dict_key = str(input("Input dictionary key (EXIT) "))
        if dict_key == 'EXIT':
            print(user_dict)
            return user_dict
        dict_value = str(input("input dictionary value (EXIT) "))
        if dict_value == 'EXIT':
            print(user_dict)
            return user_dict
        user_dict[dict_key] = dict_value
        print(user_dict)

def append_list(user_dict):
    while True:
        dict_key = str(input("Input dictionary key (EXIT) "))
        if dict_key == 'EXIT':
            print(user_dict)
            return user_dict
        dict_value = str(input("input dictionary value (EXIT) "))
        if dict_value == 'EXIT':
            print(user_dict)
            return user_dict
        user_dict[dict_key] = dict_value
        print(user_dict)

def index_dict(dict):
    pass

def user_choice_switch(choice, user_dict):
    match choice:
        case 1:
            return make_dict()
        case 2:
            return index_dict()
        case 3:
            print(user_dict)
        case 4:
            append_list(user_dict)
        case 5:
            return False
        
def user_menu():
    user_dict = {}
    while True:
        user_choice = int(input('Welcome to Dict Maker - input choice: \n 1. Make Dictionary \n 2. Index Dictionary \n 3. Print Dictionary \n 4. EXIT \n'))
        user_dict = user_choice_switch(user_choice, user_dict)
        if user_dict is False:
            break

user_menu()
