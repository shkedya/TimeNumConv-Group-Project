# Authors: Alon Shkedy, Alexander Rhoades, Neil Thayamballi
# Date: 3/7/2022
# Description: A Group Project that consists of 3 main functions, the first takes a string and returns a base 10
#              number, the second function takes an integer in seconds and converts it to a month-day-year string,
#              and a third function that takes an integer, converts it to a hexadecimal, and returns it as a string

# First Main Function
def conv_endian(num, endian):
    hex_str = ""
    hex_str_2 = ""
    hex_str_3 = ""
    orig_num = 0
    # Convert a negative integer to its positive equivalent.
    # Before converting, save the original negative value in orig_num.
    if num < 0:
        orig_num = num
        num *= -1
    # Divide the original number (or positive equivalent) by 16
    quotient = num // 16
    # Calculate the modulus of the original number (or positive equivalent)
    modulus = num % 16
    # Convert the modulus to a string
    mod_str = str(modulus)
    # Convert the string to a list
    mod_list = list(mod_str)
    # Convert the string list to an integer list
    mod_list = [int(i) for i in mod_list]
    # Continue calculating the modulus and quotient until the quotient is 0.
    # For every loop iteration, the modulus will be appended to mod_list.
    while quotient != 0:
        modulus = quotient % 16
        quotient = quotient // 16
        mod_list.append(modulus)
    # Convert the integer list mod_list to a string list
    mod_list = [str(i) for i in mod_list]
    # Convert values between 10 and 15 to the corresponding hexadecimal letter
    conv_num_to_hex_letter(mod_list)
    # Convert the original integer (or the positive equivalent) to a string
    num_str = str(num)
    # Add 0 to mod_list if number of digits is different from original integer
    if len(num_str) != len(mod_list):
        mod_list.append("0")
    for i in range((len(mod_list))-1, -1, -1):
        # Obtain hex result by appending each value in mod_list to a string
        hex_str += mod_list[i]
        hex_str_2 += mod_list[i]
        # Add a space between each pair of 2 digits
        hex_str = add_space(hex_str, orig_num, i)
    if endian == "big":
        # Append a - sign if starting integer was negative.
        # Otherwise, just return the result as is.
        hex_str = add_negative_sign(hex_str, orig_num)
        return hex_str
    if endian == "little":
        for i in range((len(hex_str_2))-1, -1, -2):
            index = 0
            hex_str_3 += hex_str_2[i-1]
            hex_str_3 += hex_str_2[i]
            index += 2
            hex_str_3 = add_space(hex_str_3, orig_num, index)
        # Append a - sign if starting integer was negative.
        # Otherwise, just return the result as is.
        hex_str_3 = add_negative_sign(hex_str_3, orig_num)
        return hex_str_3
    if endian != "big" and endian != "little":
        return "None"


def conv_num_to_hex_letter(mod_list):
    for i in range(len(mod_list)):
        if mod_list[i] == "10":
            mod_list[i] = "A"
        if mod_list[i] == "11":
            mod_list[i] = "B"
        if mod_list[i] == "12":
            mod_list[i] = "C"
        if mod_list[i] == "13":
            mod_list[i] = "D"
        if mod_list[i] == "14":
            mod_list[i] = "E"
        if mod_list[i] == "15":
            mod_list[i] = "F"


def add_space(hex_str, orig_num, i):
    if i % 2 == 0 and i != 0:
        hex_str += " "
    return hex_str


def add_negative_sign(hex_str, orig_num):
    if orig_num < 0:
        hex_str = hex_str[:0] + "-" + hex_str[0:]
    return hex_str


# Second Main Function
def my_datetime(num_sec):
    """Takes in an integer value that represents the number of seconds since the epoch (January 1st, 1970)"""

    def leap_year(years):
        """Tests if the month is a leap year or not by using mod, a leap year is every 4 years, if the year is
         divisible by 100 and not divisible by 400"""
        if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
            return years

    def days_into_months(years, months):
        """Adds an extra day to account for leap year in February and otherwise returns days"""
        days_from_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # 12 months and how many days in each month, using 0 as month 0 to offset the range
        used_day = days_from_months[months]
        if leap_year(years) and months == 2:
            return used_day + 1
        else:
            return used_day

    num_days = num_sec // (24*60*60)
    # uses floor division for the largest value when multiplying 24 hours in a day, 60 minutes in an hour, and 60
    # seconds in 1 hour
    used_month = 1
    used_day = 1
    used_year = 1970
    # starting values from the epoch (January 1st, 1970)

    while num_days > 0:
        # while loop from num_days which is given from num_sec divided by hours, minutes, and seconds and
        # continuously subtracts num_days and adding a used_day everytime the loop continues
        num_days -= 1
        used_day += 1
        if used_day > days_into_months(used_year, used_month):
            # checks the starting day from the epoch and compares if its greater than the amount of days in a month
            # resets used_days back to 1 if its greater and sets used_months to +1 than it previously was and goes
            # to the next if statement
            used_day = 1
            used_month += 1
            if used_month > 12:
                # used_month cant be greater than 12 months since their are only 12 months in a year so it adds 1 to
                # year and changes used_months back to 1 to continue the while loop
                used_month = 1
                used_year += 1
    used_day = str(used_day)
    used_month = str(used_month)
    used_year = str(used_year)
    dash = "-"
    month_date_time = used_month + dash + used_day + dash + used_year
    return month_date_time


# Third Main Function
def conv_num(num_str):
    """Converts number strings and hex strings to integer"""
    if num_valid(num_str) is False or num_str == "":
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
        return False    # The string has an invalid non-alphanumeric char

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
            result = result + pow(0.1, power) * (ord(sec) - ord('0'))
            power += 1
        else:
            result = result * 10.0 + ord(sec) - ord('0')

    return round(sign * result, power)


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
