""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

import main

title_list = ["ID", "Name", "Manufacturer", "Purshase Year", "Durability"]

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    list_options =[
        "Add new position.",
        "Remove position.",
        "Update position.",
        "Show table",
        "Available Items",
        "Average durability"
    ]
    
    title = "Inventory module"
    exit_message = "Main menu"
    while True:
        ui.print_menu(title, list_options, "Exit to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file("inventory/inventory.csv")
<<<<<<< HEAD
        if option == "1":
            add(table)
            show_table(table)
        elif option == "2":
            ui.print_table(table,title_list)
            id_ = ui.get_inputs(["ID: "],"Input ID of game to remove")
            remove(table,id_)
        elif option == "3":
            id_ = ui.get_inputs(["ID: "],"Input ID of game to update")
            update(table, id_)
        elif option == "4":
            show_table(table)
        elif option == "5":
            year = ui.get_inputs(["Year: "], "Input Year to check available items:")
            get_available_items(table, year[0])
        elif option == "6":
            get_average_durability_by_manufacturers(table)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such list_options.")
=======
        while option != 0:
            if option == "1":
                add(table)
                show_table(table)
                break
            elif option == "2":
                ui.print_table(table,title_list)
                id_ = ui.get_inputs(["ID: "],"Input ID of game to remove")
                remove(table,id_)
                break
            elif option == "3":
                id_ = ui.get_inputs(["ID: "],"Input ID of game to update")
                update(table, id_)
                break
            elif option == "4":
                show_table(table)
                break
            elif option == "0":
                exit_to_main = 1
                break
            else:
                raise KeyError("There is no such list_options.")
>>>>>>> c739cdff74ebafcae3751f42f105e4326ce99b06


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Name", "Manufacturer", "Purshase Year", "Durability"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    inputs = ui.get_inputs(["Name: ", "Manufacturer: ", "Purshase Year: ", "Durability: "], "Please enter proper data")
    genereted_id = common.generate_random(table)
    
    table.append([genereted_id,inputs[0],inputs[1],inputs[2],inputs[3]]) # inputs[0] = można zamienić na wygenerowane ID
    
    data_manager.write_table_to_file("inventory/inventory.csv", table)


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    ID_INDEX = 0
    for row in table:
        if id_[ID_INDEX] == row[ID_INDEX]:
            print("ID found and record has been removed")
            table.remove(row)
    data_manager.write_table_to_file('inventory/inventory.csv', table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    ID_INDEX = 0
    row_counter = 0
    for row in table:
        if id_[ID_INDEX] == row[ID_INDEX]:
            print(row)
            updated_row = ui.get_inputs(["Name: ", "Manufacturer: ", "Purshase Year: ", "Durability: "], "Please update data:")
            updated_row.insert(ID_INDEX, id_[ID_INDEX])
            table[row_counter] = updated_row
            break
        row_counter += 1
    data_manager.write_table_to_file("inventory/inventory.csv", table)    
    


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    available_item_list = []
    YEAR_INDEX = 3
    DURABILITY_INDEX = 4
    for row in table:
        if int(row[YEAR_INDEX]) + int(row[DURABILITY_INDEX]) >= int(year):
            available_item_list.append(row)
    ui.print_result(available_item_list, 'Available items: ')


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    MANUFACTURER = 2
    DURABILITY = 4
    avg_durability = {}
    for row in table:
        avg_durability[row[MANUFACTURER]] = avg_durability.setdefault(row[MANUFACTURER], [])
        avg_durability[row[MANUFACTURER]].append(int(row[DURABILITY]))
    for k, v in avg_durability.items():
        result = sum(v)//len(v)
        avg_durability[k] = result
    ui.print_result(avg_durability, 'Avg expected durability: ')
