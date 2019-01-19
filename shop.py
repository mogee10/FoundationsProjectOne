####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Mogee_Cupcake"
signature_flavors = ["Pecan pie", "peanut butter", "watermelon"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    for key,value in menu.items():
        print(key,value)



def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for cupcake in original_flavors:
        print (cupcake)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for cupcake in signature_flavors:
        print (cupcake)


def is_valid_order(order):
    if order in signature_flavors:
        return True
    elif order in original_flavors:
        return True
    elif order in menu:
        return True
    else:
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code
    user_input = input("what would you like to order? or Type exit to checkout\n")
    while user_input.lower()!= "exit":
        if is_valid_order(user_input) == True:
             order_list.append(user_input)
             print ("[%s] has been added to the cart" % user_input)
             user_input = input("Anything else? \n")
        else:
            print("unavailable")
            user_input = input ("order something else \n")
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        print ("we accept credit card")
    else:
        print ("cash only")

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        if order in original_flavors:
            total += original_price
        elif order in signature_flavors:
            total += signature_price
        elif order in menu:
            total += menu[order]
    # for original_flavor in original_flavors:
    #     if order == original_flavors 
    #     total += 2
    # for signature_flavor in signature_flavors:
    #     if order == signature_flavors
    #     total += 2.750

    # your code goes here!


    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    print("this is your final order %s" % order_list)
    x= get_total_price(order_list)
    print ("%0.3f KWD" % x)


