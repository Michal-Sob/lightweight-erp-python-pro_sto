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
    title_list = ["ID", "Title", "Manufacturer", "Price", "In stock" ]
    title = "Games store"
    exit_message = "Main menu"
    ui.print_menu(title, list_options, exit_message)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file("/home/lukasz/programs/light_EPR/lightweight-erp-python-pro_sto/store/games.csv")
    print(table)
    if option == "1":
        add(table)
    elif option == "2":
        ui.print_table(table,title_list)
        id_ = str(ui.get_inputs(["ID "],"Input ID of game to remove"))
        remove(table,id_)
    elif option == "3":
        update(table, id_)
    elif option == "4":
        show_table(table,)
    elif option == "5":
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
    
    ui.print_table(table, title_list)
    

    


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    inputs = ui.get_inputs(["name ", "developer ", "price ", "numbers is stock "], "Input: ID, name, developer, price, numbers is stock" )
    genereted_id = common.generate_random(table)
    
    table_temp = table.append([genereted_id,inputs[0],inputs[1],inputs[2],inputs[3],]) # inputs[0] = można zamienić na wygenerowane ID
    
    data_manager.write_table_to_file("/home/lukasz/programs/light_EPR/lightweight-erp-python-pro_sto/store/games.csv", table)
    
    return table
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
    count = 0
    print(str(id_))
    for line in range(0,len(table))
        if id_ == [table[count][0]]:
            print(table[count])
            table = table.remove(table[count])
            break

        
        count+=1
    
    data_manager.write_table_to_file("/home/lukasz/programs/light_EPR/lightweight-erp-python-pro_sto/store/games.csv", table)
    
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
