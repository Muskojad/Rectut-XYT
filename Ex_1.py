import numpy as np
import os

################################FUNCTION DEFINITIONS############################

def clear_console():
    os.system('cls')

#funtion taking user imputs cotaining order details in the loop(look: last section of code)
def make_new_order():
    price = int(input("Type in price as an integer:"))
    quant = int(input("Type in quantity as an integer:"))
    new_oder = np.array([[price],[quant]])
    return new_oder

#priting funciton helping to reduce redunand code
def printing_action(string):
    print("what kind of order would You like to ",string,
          "\n type: \n sell - to", string, "sell order",
                   "\n buy - to", string, "buy order")

#################################CLASS DEFINITIONS##############################
    
#it is a class containing out stock data and methods helping to maniuplate that data
class Stocky:

#defning lists that contain date from out model
#they are predefined with values that won't intervene later processes
    def __init__(self):
        self.sell_orders = np.array([[np.inf],[0]])                
        self.buy_orders = np.array([[0],[0]])
                              
#here are methods used to add or remove orders
#their names are self explanatory               
    def add_sell_order(self, new_sell_order):
        if new_sell_order[0] in self.sell_orders[0]:
            in_array = np.where(self.sell_orders[0] == new_sell_order[0])[0]
            self.sell_orders[1][in_array] += new_sell_order[1]
        else:
            self.sell_orders = np.column_stack((self.sell_orders, new_sell_order))

    def add_buy_order(self, new_buy_order):
        if new_buy_order[0] in self.buy_orders[0]:
            in_array = np.where( self.buy_orders[0] == new_buy_order[0])[0]
            self.buy_orders[1][in_array] += new_buy_order[1]
        else:
            self.buy_orders = np.column_stack((self.buy_orders, new_buy_order))
    
    def remove_sell_order(self, new_sell_order):
        if new_sell_order[0] in self.sell_orders[0]:
            in_array = np.where(self.sell_orders[0] == new_sell_order[0])[0]
            result = self.sell_orders[1][in_array] - new_sell_order[1]
            if result < 0:
                print("can't place order")
            else:
                self.sell_orders[1][in_array] -= result
        else:
            print("can't place order")

    def remove_buy_order(self, new_buy_order):
        if new_buy_order[0] in self.buy_orders[0]:
            in_array = np.where(self.buy_orders[0] == new_buy_order[0])[0]
            result = self.buy_orders[1][in_array] - new_buy_order[1]
            if result < 0:
                print("can't place order")
            else:
                self.buy_orders[1][in_array] -= result
        else:
            print("can't place order")

    def pirnt_best_orders(self):
        
        clear_console()
        
        sell_best_idex = self.sell_orders[0].argmin()
        best_sell_pirce = self.sell_orders[0][sell_best_idex]
        best_sell_quant = self.sell_orders[1][sell_best_idex]
        print("Best selling price is:",{best_sell_pirce}, "available in amount of", {best_sell_quant})
    
        buy_best_idex = self.buy_orders[0].argmax()
        best_buy_pirce = self.buy_orders[0][buy_best_idex]
        best_buy_quant = self.buy_orders[1][buy_best_idex]
        print("Best buying price is:",{best_buy_pirce}, "available in amount of", {best_buy_quant})
              

print("this is simple stock model")

#i'm creating object of class "Stocky" 
Stock = Stocky()
#######################################MAIN LOOP###################################

#this loop is an endless loop until user dcides to leave
def loop():
    while True:
        
#this if first stage of placing an order
        print("\n type: \n add - if You wish to add an order",
              "\n remove - if You wish to remove an order",
              "\n exit - if You wish to stop the program")
        user_input_1 = input()
        

#those are second and third stages combined due to usage of "make_new_order" function
#they could be made using "match/case"
#however it is python 3.8 project which does not contain it yet
        if user_input_1 == "add":
            printing_action(user_input_1)
            user_input_2 = input()
            if user_input_2 == "sell":
                new_oder = make_new_order()
                Stock.add_sell_order(new_oder)
            elif user_input_2 == "buy":
                new_oder = make_new_order()
                Stock.add_buy_order(new_oder)
            else:
                print("can't place order")
                pass
            
        elif user_input_1 == "remove":
            printing_action(user_input_1)
            user_input_2 = input()
            if user_input_2 == "sell":
                new_oder = make_new_order()
                Stock.remove_sell_order(new_oder)
            elif user_input_2 == "buy":
                new_oder = make_new_order()
                Stock.remove_buy_order(new_oder)
            else:
                print("can't place order")
                pass
            
#if used decided to leave the loop in first of placing order  
        elif user_input_1 == "exit":
            print("bye bye")
            break
        else:
            pass
        Stock.pirnt_best_orders()

##########################################CALLING THE LOOP########################
loop()