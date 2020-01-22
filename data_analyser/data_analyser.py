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
        'Get the last buyer name (working)',
        'Get the last buyer id (working)', 
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
    sales_table=data_manager.get_table_from_file("sales/sales.csv")
    customer_table=data_manager.get_table_from_file("crm/customers.csv")
    extracted_data = {}
    for row in sales_table:
        full_date = common.date_converter(row[-2], row[-3], row[-4]) # converts to consistent data format
        if full_date in extracted_data.keys(): #checks if key already has ben used
            extracted_data[full_date].append(row[-1]) #adds another value to value list
        else:
            extracted_data[full_date]=[row[-1]] # adds first k/v pair with value as a list

    desc_dates = sorted(extracted_data.keys(), reverse=True) #creates list with sorted key val from dict
    last_buy = desc_dates[0] #assigns highest date number
    cust_id = extracted_data[last_buy] 
    
    if len(cust_id)==1: #checks if there is only one cust_id for latest date
        for row in customer_table:
            if "".join(cust_id) in row:
                print(f"Last buyer name is {row[1]}, game was bought on: {last_buy} \n")
        return str(row[1])
    else: #if more than one buyer bought product on the same last date
        counter, name_list = 1, []
        print(f"There are more than one buyer, who purchased product on the last date in database:")
        for row in customer_table:
            for position in cust_id:
                if "".join(position) in row:
                    print(f"{counter}: {row[1]}")
                    counter += 1
                    name_list.append(row[1])
                    #[print(f"{counter}: {row[1]}"), counter += 1, name_list += str(row[1]) for position in cust_id if if "".join(position) in row]
        return ",".join(name_list) # returns a string from list
# your code


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    sales_table=data_manager.get_table_from_file("sales/sales.csv")
    customer_table=data_manager.get_table_from_file("crm/customers.csv")
    extracted_data = {}
    for row in sales_table:
        full_date = common.date_converter(row[-2], row[-3], row[-4]) # converts to consistent data format
        if full_date in extracted_data.keys(): #checks if key already has ben used
            extracted_data[full_date].append(row[-1]) #adds another value to value list
        else:
            extracted_data[full_date]=[row[-1]] # adds first k/v pair with value as a list

    desc_dates = sorted(extracted_data.keys(), reverse=True) #creates list with sorted key val from dict
    last_buy = desc_dates[0] #assigns highest date number
    cust_id = extracted_data[last_buy] 
    
    if len(cust_id)==1: #checks if there is only one cust_id for latest date
        for row in customer_table:
            if "".join(cust_id) in row:
                print(f"Last buyer id is {row[0]}, game was bought on: {last_buy} \n")
        return str(row[0])
    else: #if more than one buyer bought product on the same last date
        counter, id_list = 1, []
        print(f"There are more than one buyer, who purchased product on the last date in database, their id:")
        for row in customer_table:
            for position in cust_id:
                if "".join(position) in row:
                    print(f"{counter}: {row[0]}")
                    counter += 1
                    id_list.append(row[0])
        return ",".join(id_list)


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
