

def conv_num(num_str):
    """Converts number strings and hex strings to integer"""
    if num_valid(num_str) is False:
        return None

    if num_str.lstrip("-").isdigit() is True:
        return atoi(num_str)
    elif num_str.count(".") == 1:
        return atof(num_str)
    else:
        return hexadecimal(num_str)


def num_valid(num_str):
    """Checks if the number string is valid"""
    num_str = num_str.upper()
    dec_count = num_str.count(".")  # Checks the number of decimal dots in a string
    hex_count = num_str.count("0X")  # Checks the number of hexadecimal prefixes

    # Check for if there are too many special char to be valid
    if num_str.lstrip("-").isdigit() is False:
        if hex_count == 0 and dec_count == 0:
            return False    # An invalid alphanumeric string with no prefix or decimal point
        elif hex_count > 1 or dec_count > 1:
            return False    # Too many hex prefixes or decimal points
        elif hex_count > 0 and dec_count > 0:
            return False    # A hex with a decimal point is invalid

    num_str = num_str.replace(".", "")  # Makes it so that a float can still be evaluated
    if num_str.lstrip("-").isalnum() is False:
        return False

    # Detecting if a hexadecimal character is invalid
    for place in num_str.lstrip("-0X"):
        char_ascii = ord(place)
        if char_ascii > 70:
            return False

    return True


def atoi(num_str):
    """Converts a regular number string to an integer"""
    result = 0  # The actual number that the string converts to
    sign = 1  # The sign of the number
    num_str = num_str.strip()  # Removing whitespace

    if num_str[0] == '-':
        sign = -1
        num_str = num_str.lstrip("-")

    # Calculating the number value
    for sec in num_str:
        result = result * 10 + ord(sec) - ord('0')

    return sign * result


def atof(num_str):
    """Coverts a string to float"""
    result = 0  # The actual number that the string converts to
    sign = 1  # The sign of the number
    power = 1  # Used in the calculation of the decimal
    dec_check = False  # Checked if a decimal has been found
    num_str = num_str.strip()  # Removing whitespace

    if num_str[0] == '-':
        sign = -1
        num_str = num_str.lstrip("-")

    # Calculating the number value
    for sec in num_str:
        if sec == ".":
            dec_check = True
        elif dec_check is True:
            result = result + (0.1 ** power) * (ord(sec) - ord('0'))
            power += 1
        else:
            result = result * 10.0 + ord(sec) - ord('0')

    return sign * result


def hexadecimal(num_str):
    """Convert a hexadecimal to a number"""
    num_str = num_str.upper()
    hex_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                 'C': 12, 'D': 13, 'E': 14, 'F': 15}  # Table used for hex conversion
    sign = 1  # The sign of the number
    result = 0  # The value of the number, in terms of absolute value
    start = 2  # Area of the index where the hex starts

    # Changing the sign if the hex is negative
    if num_str[0] == '-':
        sign = -1
        start = start + 1

    new_str = num_str[start:len(num_str)]  # removing the hex prefix before conversion
    length = len(new_str) - 1
    for sec in new_str:
        result += hex_table[sec] * 16 ** length
        length -= 1

    return sign * result
