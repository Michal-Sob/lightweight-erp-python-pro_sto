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

    inputs = ui.get_inputs(["number: "], "Choose menu option.")
    option = inputs[0]

    table = data_manager.get_table_from_file("crm/customers.csv")

    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        ui.get_inputs(["id: "], "Enter id of record to be deleted.")
        id_ = ui.get_inputs(["id: "], "Enter id of record to be deleted.")[0]
        remove(table, id_)
    elif option == "4":
        ui.get_inputs(["id: "], "Ented id of record to be updated")
        id_ = ui.get_inputs(["id: "], "Ented id of record to be updated")
        update(table, id_)
    elif option == "5":
        label = "Id of the customer with the longest name is: "
        result = get_longest_name_id(table)
        ui.print_result(result, label)
    elif option == "6":
        get_subscribed_emails(table)
    elif option == "0":
        main.main()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    table = data_manager.get_table_from_file("crm/customers.csv")
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
    table = data_manager.get_table_from_file("crm/customers.csv")
    longest_name = table[0][1]
    result = table[0][0]
    for line in table:
        if len(line[1]) >= len(longest_name) and line[1][0] >= longest_name[0]:
            longest_name = line[1]
            result = line[0]
    return result


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


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code



def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code
