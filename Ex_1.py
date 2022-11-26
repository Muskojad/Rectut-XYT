import numpy as np


print("this is simple stock model")


def printing_action(string):
    print("what kind of order would You like to ",{string},
          "\n type: \n sell - to", {string}, "sell order",
                   "\n buy - to", {string}, "buy order")
    
def loop(void):
   
    user_imput_1 = input ("\n type: \n add - if You wish to add an order",
                 "\n remove - if You wish to remove an order",
                 "\n exit - if You wish to stop the program")
    
    match user_imput_1:
        case "add"
            pass
        case
        

str_remove = "remove"
str_add = "add"


sell_orders = np.array([[np.NaN],
                        [np.NaN]])
buy_orders = np.array([[np.NaN],
                       [np.NaN]])





def make_new_order(quant, pice):
    if quant < 0:
        print("can't place order")
        return np.NaN
    new_oder = np.array([[pice],[quant]])
    return new_oder


def add_sell_order(new_sell_order, sell_orders):
    if new_sell_order == np.NaN:
        return sell_orders
    elif new_sell_order[0] in sell_orders[0]:
        in_array = np.where(sell_orders[0] == new_sell_order[0])
        sell_orders[1][in_array] += new_sell_order[1]
    else:
        sell_orders = np.column_stack(sell_orders, new_sell_order)
    
    return sell_orders    


def remove_sell_order(new_sell_order, sell_orders):
    if new_sell_order == np.NaN:
        return sell_orders
    elif new_sell_order[0] in sell_orders[0]:
        in_array = np.where(sell_orders[0] == new_sell_order[0])
        result = sell_orders[1][in_array] - new_sell_order[1]
        if result < 0:
            print("can't place order")
            return sell_orders
        else:
            sell_orders[1][in_array] -= result
    else:
        print("can't place order")
    return sell_orders



def add_buy_order(new_buy_order, buy_orders):
    if new_buy_order == np.NaN:
        return buy_orders
    elif new_buy_order[0] in buy_orders[0]:
        in_array = np.where(buy_orders[0] == new_buy_order[0])
        buy_orders[1][in_array] += new_buy_order[1]
    else:
        buy_orders = np.column_stack(buy_orders, new_buy_order)
    
    return buy_orders    


def remove_buy_order(new_buy_order, buy_orders):
    if new_buy_order == np.NaN:
        return buy_orders
    elif new_buy_order[0] in buy_orders[0]:
        in_array = np.where(buy_orders[0] == new_buy_order[0])
        result = buy_orders[1][in_array] - new_buy_order[1]
        if result < 0:
            print("can't place order")
            return buy_orders
        else:
            buy_orders[1][in_array] -= result
    else:
        print("can't place order")
    return buy_orders


def pirnt_best_orders(sell_orders, buy_orders):
    
    sell_best_idex = sell_orders[0].argmin()
    best_sell_pirce = sell_orders[0][sell_best_idex]
    best_sell_quant = sell_orders[1][sell_best_idex]
    print("Best selling price is:",{best_sell_pirce}, "available in amount of", {best_sell_quant})

    buy_best_idex = buy_orders[0].argmin()
    best_buy_pirce = buy_orders[0][buy_best_idex]
    best_buy_quant = buy_orders[1][buy_best_idex]
    print("Best buying price is:",{best_buy_pirce}, "available in amount of", {best_buy_quant})
    
    
def clean_order_lists(sell_orders, buy_orders):
    idex_sell_list = np.where(sell_orders[1] == 0)
    index_buy_list = np.where(buy_orders[1] == 0)
    
    np.delete(sell_orders, idex_sell_list, 1)
    np.delete(buy_orders, index_buy_list, 1)
    
    return sell_orders, buy_orders

