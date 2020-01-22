""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    back_to_main_menu = True
    while back_to_main_menu:
        list_options = [
            "Show table", 
            "Add new record", 
            "Remove record", 
            "Update record",
            "Lowest Price item",
            "Which items are sold between two given dates?",
            "Get title by id", 
            "Get title by id from table",
            "Get item id sold last", 
            "Get item id sold last from table",
            "Get item title sold last from table", 
            "Get the sum of prices",
            "Get the sum of prices from table",
            "Get customer id by sale id",
            "Get customer id by sale id from table",
            "Get all customer ids",
            "Get all customer ids from table",
            "Get all sales ids for customer ids",
            "Get all sales ids for customer ids from table",
            "Get num of sales per customer ids",
            "Get num of sales per customer ids from table"]
        ui.print_menu('Sales', list_options, 'main menu')
        inputs = ui.get_inputs(["number: "], "Choose menu option.")
        option = inputs[0]
        table = data_manager.get_table_from_file('sales/sales.csv')
        if option == "1":
            show_table(table)
        elif option == '2':
            add(table)
        elif option == "3":
            id_ = ui.get_inputs(["id: "], "Enter id of record to be deleted.")
            remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["id: "], "Enter id of record to be updated")
            update(table, id_)
        elif option == "5":
            get_lowest_price_item_id(table)
        elif option == "6":
            month_from, day_from, year_from, month_to, day_to, year_to = ui.get_inputs(["month_from: ", "day_from: ", "year_from: ", "month_to: ", "day_to: " , "year_to: "], "Please add dates to search between: ")
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif option == "7":
            get_title_by_id(id)
        elif option == "8":
            id_ = ui.get_inputs(["id: "], "Enter ID: ")
            get_title_by_id_from_table(table, id_)
        # elif option == "9":

        # elif option == "10":
        # elif option == "11":
        # elif option == "12":
        # elif option == "13":
        # elif option == "14":
        # elif option == "15":
        # elif option == "16":
        # elif option == "17":
        # elif option == "18":
        # elif option == "19":
        # elif option == "20":
        # elif option == "21":
        # elif option == "22":
            back_to_main_menu = False

    # your code


def show_table(table):
    table_headers = ['id', 'title', 'price', 'month', 'day', 'year', 'Customer ID']
    ui.print_table(table, table_headers)

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    ID_INDEX = 0
    record = ui.get_inputs(['title: ', 'price: ','month: ', 'day: ', 'year: '], "Please insert data:" )
    record.insert(ID_INDEX, common.generate_random(table))
    table.append(record)
    data_manager.write_table_to_file('sales/sales.csv', table)
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

    ID_LIST_INDEX = 0
    for row in table:
        if row[ID_LIST_INDEX] == id_[ID_LIST_INDEX]:
            table.remove(row)
    data_manager.write_table_to_file('sales/sales.csv', table)
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

    ID_LIST_INDEX = 0
    iterate = 0
    for row in table:
        if row[ID_LIST_INDEX] == id_[ID_LIST_INDEX]:
            updated_record = ui.get_inputs(['title: ', 'price: ', 'month: ', 'day: ', 'year: '], row)
            updated_record.insert(ID_LIST_INDEX, id_[ID_LIST_INDEX])
            table[iterate] = updated_record
            data_manager.write_table_to_file('sales/sales.csv', table)
            break
        iterate += 1
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
    ID_INDEX = 0
    PRICE_INDEX = 2
    TITLE_INDEX = 1
    smallest_price = table[0][PRICE_INDEX]
    id_list = []
    for row in table:
        if row[PRICE_INDEX] < smallest_price:
            smallest_price = row[PRICE_INDEX]
            id_list.clear()
            id_list.append(row[ID_INDEX : PRICE_INDEX + 1])
        elif row[PRICE_INDEX] == smallest_price:
            id_list.append(row[ID_INDEX : PRICE_INDEX + 1])
    
    title_smallest_price = max([row[TITLE_INDEX] for row in id_list])
    # dupa = [row[ID_INDEX] == title_smallest_price for row in id_list]
    for row in id_list:
        if row[TITLE_INDEX] == title_smallest_price:
            id_smallest_price = row[ID_INDEX]
    print(id_smallest_price)






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

# functions supports data abalyser
# --------------------------------


def get_title_by_id(id_):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """
    ID_INDEX = 0
    TITLE_INDEX = 1
    sales_table = data_manager.get_table_from_file("sales/sales.csv")
    #[(ui.print_result(row[TITLE_INDEX], "The title is: "), return None) for row in sales_table if id_[0] == row[ID_INDEX]]
    for row in sales_table:
        if id_[0] == row[ID_INDEX]:
            ui.print_result(row[TITLE_INDEX], "The title is: ")
            return row[TITLE_INDEX]
    return None


def get_title_by_id_from_table(table, id_):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code
    for row in table:
        if id_ == row[0]:
            return ui.print_result(row[1], "The game's title is: ")


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code
    sales_table = data_manager.get_table_from_file("sales/sales.csv")
    return get_all_customer_ids_from_table(customer_table)


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    all_id = set()
    for row in table: 
        all_id.add(str(row[-1]))
    ui.print_result(all_id, "All customers ID: ")  
    return all_id


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code
    sales_table = data_manager.get_table_from_file("sales/sales.csv")
    return get_all_sales_ids_for_customer_ids_from_table(sales_table)



def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    CUSTOMER_ID_INDEX=-1
    SALE_ID_INDEX=0
    customer_sale_ids={}
    for row in table:
        if row[CUSTOMER_ID_INDEX] in customer_sale_ids.keys():
            customer_sale_ids[row[CUSTOMER_ID_INDEX]].append(row[SALE_ID_INDEX])
        else:
            customer_sale_ids[row[CUSTOMER_ID_INDEX]]=[row[SALE_ID_INDEX]]
    return customer_sale_ids


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
    print(table)
