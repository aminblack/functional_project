import os
from log import logger
shopping_list = list()
EXIT_COMANDS = ["q", "exit", "quit", "ex"]
faktor = {}
count_list = {}
count_item = []
prudoct = {
            'vegtables': [
                'carrot',
                'onion',
                'potaito',
                'tomaito'
            ],
            'fruits': [
                'banana',
                'orange',
                'apple',
                'peach'
            ],
            'liquit': [
                'water',
                'coca',
                'milk',
                'soda'
            ],
            'snacks': [
                'cheeps',
                'chooklate',
                'cake',
                'icecream'
            ]
}
price = {
        'vegtables': [
            20,
            15,
            15,
            30
        ],
        'fruits': [
            60,
            30,
            25,
            50
        ],
        'liquit': [
            5,
            10,
            20,
            25
        ],
        'snacks': [
            35,
            40,
            20,
            25
        ]
}
stuck = {
        'vegtables': [
            10,
            11,
            12,
            13
        ],
        'fruits': [
            14,
            15,
            16,
            17
        ],
        'liquit': [
            10,
            11,
            12,
            13
        ],
        'snacks': [
            20,
            21,
            22,
            23
        ]
}


def repeated_username(get_user):
    with open('user_login.txt', 'r') as file:
        check = file.readlines()
        for index in range(0, len(check)):
            if (get_user + '\n') == check[index]:
                return "not ok"


def join_user(get_user, get_pass, func_repeated):
    repeated = repeated_username(get_user)
    if repeated != "not ok":
        with open('user_login.txt', 'a')as file:
            file.write(get_user)
            file.write('\n')
            file.write(get_pass)
            file.write('\n')
    else:
        return "repeated"


def check_user(name, secret):
    with open('user_login.txt', 'r') as file:
        check = file.readlines()
        for index in range(0, len(check)):
            if (name + '\n') == check[index]:
                if (secret + '\n') == check[index + 1]:
                    return "ok"


def beautify_list(my_list):
    """
for show item in shopping_list step by step
Parameters
----------
my_list :shopping_list
    """
    for item in my_list:
        print(f"> {item}")


def show_help():
    """ show help for to do key word """
    print("enter the item in", EXIT_COMANDS, "to exit and see the list")
    print("enter help to see help")
    print("enter serch to search the item as you want")
    print("if you want remove the item in list enter removecd")


def add_item(my_list, item):
    """
for join item in shoping list
    Parameters
    ----------
    my_list :shoping_list
    item :item
    """
    my_list.append(item)


def remove_item(my_list, item):
    """
if user want to delit a item in shopping_list
    Parameters
    ----------
    my_list :shoping_list
    item :item
    Returns
    -------
shopping_list
    """
    if item not in my_list:
        print("item that you are trying to remove is not in the list")
    else:
        my_list.remove(item)
    return my_list


def search_list(my_list, cal):
    """
    if user want to search item in shopping_list
    Parameters
    ----------
    my_list :shopping_list
    cal :search
    """
    if cal in my_list:
        print(cal)
    else:
        print("you have been never enter", cal)


def edit_list(my_list, item, new):
    if item in my_list:
        for index in range(0, len(my_list)):
            if my_list[index] == item:
                my_list[index] = new
    else:
        print("you have been never enter", item)


def price_list(prudoct, my_list, price):
    for key, valu in prudoct.items():
        for item in range(0, len(my_list)):
            if my_list[item] in valu:
                for item2 in range(0, len(valu)):
                    if valu[item2] == my_list[item]:
                        print(f'{my_list[item]} : {price[key][item2]} $')
                        count_list[my_list[item]] = (int(price[key][item2]))


def to_shop(my_list):
    for _ in my_list:
        yield _



def clear_screen():
    """after run a code clear terminal """
    return os.system("cls")


keep = "not ok"
while keep == "not ok":
    enter = input("if you want to join wright:'join', else :'enter': ")
    if enter == "enter":
        user = input("enter your user: ")
        password = input("enter your password: ")
        try:
            if check_user(user, password) == "ok":
                print("your welcome")
                keep = "ok"
                logger.info(f'{user},join the shopping list')
                continue
            else:
                raise ValueError("user or pass is wrong")
        except ValueError:
            print("user or pass is wrong!")
            logger.error('user or pass is wrong!')
    else:
        while True:
            try:
                new_user = input("enter your new_user: ")
                new_password = input("enter your new_password: ")
                if join_user(new_user, new_password, repeated_username) != "repeated":
                    print("you successes")
                    break
                else:
                    raise ValueError("user is repeated")
            except ValueError:
                print("user is repeated")
                logger.error('user is repeated')

while True:
    item = input("pleas enter the item you want to add your list: ").casefold()
    clear_screen()
    if item in EXIT_COMANDS:
        beautify_list(shopping_list)
        logger.info(f'{user}, left the shopping list')
        break
    elif item == "help":
        show_help()
    elif item == "search":
        search = input("what thing you want: ")
        search_list(shopping_list, search)
    elif item in shopping_list:
        print(input("repeated item"))
        continue
    elif item == "remove":
        itemToRemove = input("please enter the item you want to remove: ")
        remove_item(shopping_list, itemToRemove)
    elif item == "edit":
        edit_item = input("enter the item in your list you want to change: ")
        new_item = input("enter the item as a new item in your list: ")
        edit_list(shopping_list, edit_item, new_item)
    else:
        add_item(shopping_list, item)
        print(f"{item} added to list")
        print(f"we have {len(shopping_list)} items")
price_list(prudoct, shopping_list, price)
shopping = to_shop(shopping_list)
x = 0
while x < len(shopping_list):
    print(next(shopping))
    number = int(input("pleas enter count of this item: "))
    count_item.append(number)
    x += 1
total = 0
final_shopping_list = dict(zip(shopping_list, count_item))
for itms, prices in count_list.items():
    for itm, count in final_shopping_list.items():
        if itms == itm:
            faktor[itms] = prices * count
            total += prices * count
            print(f'{itms} -> count : {count} , price : {prices} $,total : {prices * count} $') 
            print(50 * '-')
print(f' total of all items : {total} $')