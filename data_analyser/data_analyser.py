"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm

import data_manager
# common module


import main


def start_module():
    
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    list_options =[
        'Get the last buyer name',
        'Get the last buyer id', 
        'Get the buyer name spent most and the money spent',
        'Get the buyer id spent most and the money spent',
        'Get the most frequent buyers names',
        'Get the most frequent buyers ids'
    ]
    
    title = "Data analyser module"
    exit_message = "Main menu"
    exit_to_main = 0
    while True:
        ui.print_menu(title, list_options, "Exit to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            get_the_last_buyer_name()
        elif option == "2":
            get_the_last_buyer_id()
        elif option == "3":
            get_the_buyer_name_spent_most_and_the_money_spent()
        elif option == "4":
            get_the_buyer_id_spent_most_and_the_money_spent()
        elif option == "5":
            get_the_most_frequent_buyers_names()
        elif option == "6":
            get_the_most_frequent_buyers_ids()
        elif option == "0":
            exit_to_main = 1
            break
        else:
            raise KeyError("There is no such list_options.")



def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """
    item_id = sales.get_item_id_sold_last()
    customer_id = sales.get_customer_id_by_sale_id(item_id)
    ui.print_result(crm.get_name_by_id(customer_id), "Last buyer name was: ")
    return crm.get_name_by_id(customer_id)



def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """
    item_id = sales.get_item_id_sold_last()
    ui.print_result(sales.get_customer_id_by_sale_id(item_id), "Last buyer id was: ")
    return sales.get_customer_id_by_sale_id(item_id)


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    buyers_and_expenditures_dict = sales.get_the_sum_of_money_spend_by_each_buyer()
    sorted_buyers_and_expenditures = sorted([(value, key) for (key, value) in buyers_and_expenditures_dict.items()],reverse=True) #reverse sorted list of tuples (sum,id)
    buyer_id, sum_spent=(sorted_buyers_and_expenditures[0][1], sorted_buyers_and_expenditures[0][0])
    # buyer_id, sum_spent = get_the_buyer_id_spent_most_and_the_money_spent()
    customer_name = crm.get_name_by_id(buyer_id)
    result = (customer_name, sum_spent)
    ui.print_result(result, "Name of the buyer who spent the most and the ammount: ")
    return result

    # your code


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    buyers_and_expenditures_dict = sales.get_the_sum_of_money_spend_by_each_buyer()
    sorted_buyers_and_expenditures = sorted([(value, key) for (key, value) in buyers_and_expenditures_dict.items()],reverse=True) #reverse sorted list of tuples (sum,id)
    result_of_function=(sorted_buyers_and_expenditures[0][1], sorted_buyers_and_expenditures[0][0])
    ui.print_result(result_of_function, "Id of the buyer who spent the most and the ammount: ")
    return result_of_function


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # your code


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # your code
