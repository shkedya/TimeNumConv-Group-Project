def conv_endian(num, endian):
    hex_str = ""
    hex_str_2 = ""
    hex_str_3 = ""
    orig_num = 0
    # Convert a negative integer to its positive equivalent.
    # Before converting, save the original negative value in orig_num.
    if(num < 0):
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
    while(quotient != 0):
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
    if (len(num_str) != len(mod_list)):
        mod_list.append("0")
    for i in range((len(mod_list))-1, -1, -1):
        # Obtain hex result by appending each value in mod_list to a string
        hex_str += mod_list[i]
        hex_str_2 += mod_list[i]
        # Add a space between each pair of 2 digits
        hex_str = add_space(hex_str, orig_num, i)
    if(endian == "big"):
        # Append a - sign if starting integer was negative.
        # Otherwise, just return the result as is.
        hex_str = add_negative_sign(hex_str, orig_num)
        return hex_str
    if(endian == "little"):
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
    if(endian != "big" and endian != "little"):
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
    if(i % 2 == 0 and i != 0):
        hex_str += " "
    return hex_str


def add_negative_sign(hex_str, orig_num):
    if orig_num < 0:
        hex_str = hex_str[:0] + "-" + hex_str[0:]
    return hex_str
