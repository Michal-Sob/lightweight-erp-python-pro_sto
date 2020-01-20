""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    exit_message = main.handle_menu()
    title= 'Sales'
    list_options = [
        "Show table", "Add new record", "Remove record", "Update record",
        "Lowest Price item","Which items are sold between two given dates?"
    ]
    ui.print_menu('Sales', list_options, exit_message)

    file_name = "sales.csv"
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
        get_lowest_price_item_id(table)
    elif option == ["6"]:
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
    elif option == ["0"]:
        main.main()

    # your code


def show_table(table):
    table_headers=['id','title','price','month','day','year']  
    table= data_manager.get_table_from_file(sales.csv) 
    ui.print_table(table,table_headers)

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    inputs= get_inputs(["month","day","year","type","amount"],"Please provide information to add")
    id=common.generate_random(table)
    table= table.append(table)
    table=data_manager.get_table_from_file(accounting/items.csv)
    table= data_manager.write_table_to_file(items.csv,inputs)
ui.print_table(table,table_headers)

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
    id=common.generate_random(table)
    with open (sales.csv,'r+') as file:

    # your code

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
