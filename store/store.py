""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common




def start_module():
    list_options =[
        "Add new game.",
        "Remove game.",
        "Update game.",
        "Show table"
    ]
    title = "Games store"
    exit_message = "Main menu"
    ui.print_menu(title, list_options, exit_message)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    list_options = inputs[0]
    table = data_manager.get_table_from_file("games.csv")
    if list_options == "1":
        add(table)
    elif list_options == "2":
        ui.print_table(table)
        ui.get_inputs(["ID"],"Input ID of game to remove")
        remove(table)
    elif list_options == "3":
        update(table, id_)
    elif list_options == "4":
        show_table(table,)
    elif list_options == "5":
        main.main(table, id_)
    else:
        raise KeyError("There is no such list_options.")

"""
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "Title", "Manufacturer", "Price", "In stock" ]
    ui.print_table(table, title_list)
    

    


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    inputs = ui.get_inputs(["ID", "name", "developer", "price", "numbers is stock"], "Input: ID, name, developer, price, numbers is stock" )
    table.append[inputs[0],inputs[1],inputs[2],inputs[3],inputs[4]] # inputs[0] = można zamienić na wygenerowane ID
    
    return table
    data_manager.write_table_to_file("games.csv", table)

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
    table.remove()
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
