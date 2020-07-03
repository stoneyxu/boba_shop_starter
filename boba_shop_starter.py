# Make our own boba tea shop!
menu = {
    "Black Sugar Boba Tea" : 3.50,
    "Taro Boba Tea" : 4.00,
    "Thai Milk Tea" : 3.75,
    "Regular Bubble Tea" : 3.00
}

order = {
    
}
# Skills Required: Functions, Dictionaries, Arithmetic, Input
# Optional Skills:

# Tasks
  # 1. Allow the shopowner to add items to the menu
  # 2. Allow the shopowner to delete item from the menu
  # 3. Allow the shopowner to update items on the menu (price, name)
  # 4. Allow customers to read the menu, and select specific menu items

# Bonus Tasks
  # 5. Allow customers to purchase specific items, and calculate an order total
  # 6. Allow customers to receive a receipt with their total and a message

# Starter code (add parameters to functions if needed)
def add_item(item_name, item_price):
    if item_name in menu:
        print('The item already exists!')
    else:
        menu[item_name]=item_price
        print('Success!')
    return

def delete_item(item_name):
    if item_name in menu:
        menu.pop(item_name)
        print('Success!')
    else:
        print('The item does not exist, so it cannot be deleted.')
    return


def update_item(item_name, item_price):
    menu[item_name]=item_price
    print('Successfully updated!')
    return
    

def purchase_item():
    item_name = input('What do you want to buy? \t')
    if item_name in menu:
        number_items = int(input('How many do you want? \t'))
        item_price = menu.get(item_name)
        total = item_price * number_items
        order[item_name] = total
        print('You purchased {0} cups of {1} for ${2}!'.format(number_items, item_name, total))
        get_receipt()
    else:
        print('There isn\'t such a drink!')
    return


def get_receipt():
    if_receipt=int(input('''\tDo you want a receipt?
    Type 1 for \'yes\' and 2 for \'no\' then enter\n'''))
    if if_receipt==1:
        print(order)
    else:
        print('Thank you!')
    return



# Simulation goes here:
if __name__ == "__main__":
    # Shopowner perspective
    # add_item("test", 1.01)
    # print(menu)
    # add_item("Taro Boba Tea", 4.50)
    # print(menu)
    # delete_item('Taro Boba Tea')
    # print(menu)
    # delete_item('test_delete')
    # print(menu)
    # update_item('test', 2.01)
    # print(menu)
    # update_item('test#2', 3.01)
    # print(menu)
    

    # Customer perspective
    purchase_item()
