""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.
kk
    Returns:
        string: Random and unique string
    """

    generated = ''

    lower_let = 'qwertyuioplkjhgfdsazxcvbnm'
    upper_let = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    digit = '1234567890'
    special = '!@#$%^&*'
    

    for i in range(2):
        generated += random.choice(lower_let)
        generated += random.choice(upper_let)


    for i in range(2):
        generated += random.choice(digit)


    for i in range(2):
        generated += random.choice(special)

    
    return generated


def check_int_input(list_labels, title):
    """
    Checks if input from user is int type.
    Useful for choosing menu switching options.
    """
    is_error = False
    while not is_error:
        try:
            inputs = [int(data) for data in input(f"{title} \n {list_labels}")]
            is_error = True
        except ValueError:
            print("Your input should be a number.")
    return inputs
