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
        'Get the most frequent buyers ids', 
        'Get the most frequent buyers names',
        'Get the buyer id spent most and the money spent',
        'Get the buyer name spent most and the money spent',
        'Get the last buyer id', 'Get the last buyer name'
    ]
    
    title = "Data analyser module"
    exit_message = "Main menu"
    exit_to_main = 0
    while exit_to_main == 0:
        ui.print_menu(title, list_options, "Exit to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        while option != 0:
            if option == "1":
                get_the_last_buyer_name()
                break
            elif option == "2":
                get_the_last_buyer_id()
                break
            elif option == "3":
                get_the_buyer_name_spent_most_and_the_money_spent()
                break
            elif option == "4":
                get_the_buyer_id_spent_most_and_the_money_spent()
                break
            elif option == "5":
                get_the_most_frequent_buyers_names()
                break
            elif option == "6":
                get_the_most_frequent_buyers_ids()
                break
            elif option == "0":
                exit_to_main = 1
                break
                main.main(table, id_)
            else:
                raise KeyError("There is no such list_options.")



def get_the_last_buyer_name(): #still working on it PP
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """
    sales_table=data_manager.get_table_from_file("sales/sales.csv")
    # extracted_data = [[y,m,d,c_id] for y,m,d,c_id in zip(sales_table[-1],sales_table[-2],sales_table[-3],sales_table[-4])]
    extracted_data = {}
    for row in sales_table:
        full_date = common.date_converter(row[-2], row[-3], row[-4])
        extracted_data[full_date] = []
        extracted_data[full_date].append(row[-1])
        # date_cust_id_list = common.date_converter(row[-2], row[-3], row[-4]), row[-1]
        # if full_date in extracted_data:
        #     extracted_data[full_date].append(row[-1])
        # else:
        #     extracted_data[full_date]=row[-1]
        # print(m,d,y,c)
    print("extracted data",extracted_data)
    # your code


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    # your code


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # your code


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # your code


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
