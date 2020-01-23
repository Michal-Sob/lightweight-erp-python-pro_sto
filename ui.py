""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.
    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/
    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers
    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    separator = " | "
    max_length_column = []
    whole_length = 0
    spacebar_between_columns = 3
    separtor = "|"
    for column in range(len(title_list)):   
        temp_lenght_column = 0
        for row in range(len(table)):
            if len(str(table[row][column])) > temp_lenght_column:
                temp_lenght_column = len(str(table[row][column]))
                temp_lenght_column = int(temp_lenght_column) + spacebar_between_columns
        max_length_column.append(temp_lenght_column)
    
    for i in range(len(title_list)):
        temp_lenght_titel = len(str(title_list[i]))
        if temp_lenght_titel > max_length_column[i]:
            max_length_column[i] = temp_lenght_titel
        


    for i in range(len(max_length_column)):     # dlugosc wszyskich znakow / suma znakow z wierszywiersza max
        whole_length += max_length_column[i]
    whole_length += len(title_list) * len(str(separator))

    print("\n\n")
    print(whole_length * "-")

    for i in range(len(title_list)):
        print(f"{title_list[i]:>{max_length_column[i]}}", end=separator)

    print()

    print(whole_length * "-")
    for row in table:
        for i in range(len(title_list)):
            print(f"{row[i]:<{max_length_column[i]}}", end=separator) 

        print()
        print(whole_length * "-")
    print("")


def print_result(result, label):
    """
    Displays results of the special functions.
    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result
    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f"\n{label}")
    if type(result) == dict:
        [print(f"{i[0]} | {i[1]}") for i in result.items()]
        # [print(f"{i[0]} | {i[1]}") for i in result.items() if type(result) == dict]
    if type(result) == str:
        print(f"{result}")
    if type(result) == list:
        [print(str(single_list).strip("()")) for single_list in result]
    if type(result) == int:
        print(f"{result}")
    if type(result) == set:
        [print(f"{single_element}") for single_element in result]
    if type(result) == tuple:
        [print(f"{single_element}") for single_element in result]
    print()
    

def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program
    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")
    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(title)
    for index, value in enumerate(list_options):
        print(f"\t({index+1}) {value}")
    print("\t(0) %s" % exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>
    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"
    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """

    inputs = []
    print(f'{title}')
    list_labels = list(list_labels)
    for label in list(list_labels):
        get_input = input(label)
        inputs.append(get_input)
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)
    Args:
        message (str): error message to be displayed
    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f'\n\t{message}\n')
    # your code
