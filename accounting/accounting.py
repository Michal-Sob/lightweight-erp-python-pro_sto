""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
import main

def start_module():
    exit_message = main.handle_menu()
    title= 'Accounting'
    list_options = [
        "Show table", "Add new record", "Remove record", "Update record",
        "Year with the higher profit","Average (per item) profit in a given year"
    ]
    ui.print_menu('Accounting', list_options, exit_message)

    file_name = "items.csv"
    inputs = ui.get_inputs(["number: "], "Choose menu option.")
    option = inputs[0]

    table = data_manager.get_table_from_file("accounting/items.csv")

    if option == ["1"]:
        show_table(table)
    elif option == ["2"]:
        add(table)
    elif option == ["3"]:
        ui.get_inputs(["id: "], "Enter id of record to be deleted.")
        id_ = ui.get_inputs(["id: "], "Enter id of record to be deleted.")[0]
    elif option == ["4"]:
        ui.get_inputs(["id: "], "Ented id of record to be updated")
        id_ = ui.get_inputs(["id: "], "Ented id of record to be updated")
        update(table, id_)
    elif option == ["5"]:
        which_year_max(table)
    elif option == ["6"]:
        avg_amount(table,year)
    elif option == ["0"]:
        main.main()

def show_table(table):
    table_headers=['id','month','day','year','type','amount']  
    table= data_manager.get_table_from_file(items.csv) 
    ui.print_table(table,table_headers)
    # your code

def add(table,id):
    id_ = common.generate_random(table)

    datauser = ui.get_inputs(['input your name: ', 'Choose your hire year:  '], "Please provide your personal information")
    table.append([id_, datauser[0],datauser[1]])
    ui.print_result(datauser, "You add new record")
    
    data_manager.write_table_to_file("hr/persons.csv", table)

def remove(table, id_):
    id=common.generate_random(table)
    inputs= get_inputs(['table','id'],'Please provide id and table to remove')
    table=table.remove(inputs)
    ui.print_table(table,title_list)
    
    #return table


def update(table, id_):
    

    # your code

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
   

    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    # inputs= ui.get_inputs.(['table','year'],'Please provide a year to calculate profit')
    # with open.(items.csv,'r')
    


    # your code
