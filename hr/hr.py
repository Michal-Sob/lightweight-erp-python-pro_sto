""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    back_to_main_menu = True
    while back_to_main_menu:
        title = "Human resources manager"
        list_options = ['Show table Hr', 'Add User', 'Remove' , 'Update', 'Olders','Closeset Year'  ]
        ui.print_menu(title, list_options, "Main menu")
        # id_ =
        table = data_manager.get_table_from_file("hr/persons.csv")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            # ui.print_table(table, title_list)
            id_ = ui.get_inputs(['Choose ID which do you want remove:  '], "Please provide your personal information")
            remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs(['Choose ID which do you want update:  '], "Please provide your personal information")
            update(table,id_)
        elif option == "5":
            get_oldest_person(table)
        elif option == "6":
            get_persons_closest_to_average(table)
        elif option == "0":
            back_to_main_menu = False


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['ID', 'Name', 'Year']
    ui.print_table(table, title_list)
    # ui.print_menu(title, list_options, "Human Resources Manager")

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    message = ("Please check your input")
    CURRENT_YEAR = 2020
    id_ = common.generate_random(table)
    datauser = ui.get_inputs(['input your name: ', 'Choose your hire year:  '], "Please provide your personal information")
    datauser[1] = int(datauser[1])
    # while isinstance(datauser[0], str) and isinstance(datauser[1], int) and datauser[1] <= CURRENT_YEAR:
    if isinstance(datauser[0], str) and isinstance(datauser[1], int) and datauser[1] <= CURRENT_YEAR:
        table.append([id_, datauser[0],str(datauser[1])])
        label = "You added the new emploee"
        ui.print_result(datauser, label)
        data_manager.write_table_to_file("hr/persons.csv", table)
    else:
        ui.print_error_message(message)
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

    id_ = ("".join(map(str, id_)))

    for row in table:
        if row[0] == id_:
            ui.print_result(row, f"This is  employee who  you going to remove ")
            table.remove(row)
            ui.print_result(row, f"You removed this record")
        
    data_manager.write_table_to_file("hr/persons.csv", table)

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
    id_ = ("".join(map(str, id_)))
    index_table = 0
    for row in table:
        if row[0] == id_:
            ui.print_result(row, f"This is  employee which you choose ")
            datauser = ui.get_inputs(['input your name: ', 'Choose your hire year:  '], "Please insert new information")
            table[index_table][1:] = datauser
            ui.print_result(table[index_table],f"This is your record after changes")
        index_table += 1


    data_manager.write_table_to_file("hr/persons.csv", table)
    
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
