""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
# main module
import main


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    list_options = [
        "Show table", "Add new record", "Remove record", "Update record",
        "Show id of the longest name",
        "Show customers subscribed to newsletter"
    ]
    ui.print_menu("CRM", list_options, "Main menu")

    file_name = "customers.csv"
    inputs = ui.get_inputs(
        ["number of menu option ", "id(mandatory for updating or adding) "],
        "Please provide operation details:")
    option = inputs[0]
    id_ = inputs[1]

    table = data_manager.get_table_from_file(file_name)

    if option == ["1"]:
        show_table(table)
    elif option == ["2"]:
        add(table)
    elif option == ["3"]:
        remove(table, id_)
    elif option == ["4"]:
        update(table, id_)
    elif option == ["5"]:
        get_longest_name_id(table)
    elif option == ["6"]:
        get_subscribed_emails(table)
    elif option == ["0"]:
        main.main()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    table_headers = ["id", "name", "e-mail", "subscribed"]
    ui.print_table(table, table_headers)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

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

    return table


# special functions:
# ------------------


def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code