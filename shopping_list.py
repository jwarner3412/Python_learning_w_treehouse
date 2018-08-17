import os

shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    clear_screen()
    print("What would you like th pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'REMOVE' to delete an item.
    Enter 'HELP' for this help.
    Enter 'SHOW' to view list.
    """)


def add_to_list(item):
    print_list()
    if shopping_list:
        position=input("Where should I add {}?\n"
                       "Press Enter to add to end of list.\n"
                       "> ".format(item))
    else:
        position=0
    try:
        position = abs(int(position))
    except ValueError:
        position=None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(item)
        
    print_list()



def print_list():
    clear_screen()
    print("Here are your items: ")
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1
    print("-"*10)


def remove_item():
    print_list()
    item = input("Which item would you like to remove?\n> ")
    try:
        shopping_list.remove(item)
    except ValueError:
        try:
            item = abs(int(item))
            del shopping_list[item-1]
        except ValueError:
            pass
        except IndexError:
            pass
    print_list()


show_help()

while True:
    new_item = input('> ')
    
    if new_item.lower() == "done" or new_item.lower() == "quit":
        break
    
    elif new_item.lower() == "help":
        show_help()
        continue
        
    elif new_item.lower() == "show":
        print_list()
        continue
    
    elif new_item.lower() == "remove":
        remove_item()
        continue
        
    add_to_list(new_item)
    print(new_item + " added, there are {} items on your list".format(len(shopping_list)))
    
print_list()
