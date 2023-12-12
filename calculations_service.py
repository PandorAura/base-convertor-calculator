def prepare_numbers_for_addition(number1, number2):
    """
    Function that gets two numbers as parameters and prepares them for addition by adding insignificant zeros until they
    have the same number of digits
    :param number1: a number in an arbitrary base
    :param number2: a number in an arbitrary base
    :return: the numbers with the same numbers of digits, with insignificant zeros added
    """
    if len(number1) != len(number2):
        if len(number1) > len(number2):
            while len(number1) > len(number2):
                number2 = number2[::-1]
                number2 = number2 + '0'
                number2 = number2[::-1]
        if len(number1) < len(number2):
            while len(number1) < len(number2):
                number1 = number1[::-1]
                number1 = number1 + '0'
                number1 = number1[::-1]

    return number1, number2


def add(number1, number2, base):
    """
    Function that gets two numbers written in a base base and performs their addition in that base
    :param number1: the first operand of the addition, given in base base
    :param number2: the second operand of the addition, given in base base
    :param base: the base of the operands
    :return: the addition of the operands in the given base
    """
    number1, number2 = prepare_numbers_for_addition(number1, number2)
    max_length = max(len(number1), len(number2))
    result = ""
    carry = 0

    # Iterate through digits from right to left
    for i in range(max_length - 1, -1, -1):
        if is_hexa_digit(number1[i]) and is_hexa_digit(number2[i]):
            digit_sum = get_decimal_digits(number1[i]) + get_decimal_digits(number2[i]) + carry
        elif is_hexa_digit(number1[i]):
            digit_sum = get_decimal_digits(number1[i]) + int(number2[i]) + carry
        elif is_hexa_digit(number2[i]):
            digit_sum = int(number1[i]) + get_decimal_digits(number2[i]) + carry
        else:
            digit_sum = int(number1[i]) + int(number2[i]) + carry

        if could_be_hexa_value(str(digit_sum % int(base))):
            result = get_hexa_values(str(digit_sum % int(base))) + result
        else:
            result = str(digit_sum % int(base)) + result
        carry = digit_sum // int(base)

    # If there's a carry left, add it to the leftmost position
    if carry:
        result = str(carry) + result

    return result


def subtract(number1, number2, base):
    """
    Function that gets two numbers written in a base base and perform their subtraction
    :param number1: the first operand in base base
    :param number2: the second operand in base base
    :param base: the base of the operands
    :return: the difference between number1 and number2, calculated in the given base
    """
    number1, number2 = prepare_numbers_for_addition(number1, number2)
    max_length = max(len(number1), len(number2))
    result = ""
    borrow = 0

    # Iterate through digits from right to left
    for i in range(max_length - 1, -1, -1):
        if is_hexa_digit(number1[i]) and is_hexa_digit(number2[i]):
            digit_sum = get_decimal_digits(number1[i]) - get_decimal_digits(number2[i]) + borrow

        elif is_hexa_digit(number1[i]):
            digit_sum = get_decimal_digits(number1[i]) - int(number2[i]) + borrow

        elif is_hexa_digit(number2[i]):
            digit_sum = int(number1[i]) - get_decimal_digits(number2[i]) + borrow

        else:
            digit_sum = int(number1[i]) - int(number2[i]) + borrow

        if digit_sum < 0:
            borrow = -1
            digit_sum = digit_sum + base
        else:
            borrow = 0

        if could_be_hexa_value(str(digit_sum % int(base))):
            result = get_hexa_values(str(digit_sum % int(base))) + result
        else:
            result = str(digit_sum % int(base)) + result

    return result


def divide(first_operand, second_operand, base):
    """
    Function that gets two numbers written in the base base and their base and performs division by one digit in
    the given base
    :param first_operand: the first operand of the division, written in base base
    :param second_operand: the second operand of the division, written in base base
    :param base: the base of the operands in which the division will be performed
    :return: the quotient and the reminder of the division
    """
    max_length = max(len(first_operand), len(second_operand))
    result = ""
    carry = 0

    if is_hexa_digit(second_operand):
        second_operand = get_decimal_digits(second_operand)

    for i in range(0, max_length, 1):
        if is_hexa_digit(str(carry)):
            carry = get_decimal_digits(str(carry))
        if is_hexa_digit(first_operand[i]):
            digit_sum = int(base) * carry + get_decimal_digits(first_operand[i])
        else:
            digit_sum = int(base) * carry + int(first_operand[i])

        if could_be_hexa_value(str(digit_sum % int(second_operand))):
            carry = get_hexa_values(str(digit_sum % int(second_operand)))
        else:
            carry = digit_sum % int(second_operand)

        if could_be_hexa_value(str(digit_sum // int(second_operand))):
            result = get_hexa_values(str(digit_sum // int(second_operand))) + result
        else:
            result = str(digit_sum // int(second_operand)) + result

    result = result[::-1]

    return result, carry


def multiply(first_operand, second_operand, base):
    """
    Function that gets two numbers written in the base base and their base and performs multiplication by one digit in
    the given base
    :param first_operand: the first operand of the multiplication, written in base base
    :param second_operand: the second operand of the multiplication, written in base base
    :param base: the base of the operands in which the multiplication will be performed
    :return: the result of the multiplication
    """
    result = ""
    carry = 0

    if is_hexa_digit(second_operand):
        second_operand = get_decimal_digits(second_operand)

    for i in range(len(first_operand) - 1, -1, -1):
        if is_hexa_digit(first_operand[i]):
            digit_sum = get_decimal_digits(first_operand[i]) * int(second_operand) + carry
        else:
            digit_sum = int(first_operand[i]) * int(second_operand) + carry

        carry = digit_sum // int(base)

        if could_be_hexa_value(str(digit_sum % int(base))):
            result = get_hexa_values(str(digit_sum % int(base))) + result
        else:
            result = str(digit_sum % int(base)) + result

    if carry:
        result = str(carry) + result

    return result


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> HEXA DIGITS CASE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def is_hexa_digit(digit_to_be_checked):
    """
    Function used to check if a digit, given as string, could be a numeric value or not
    :param digit_to_be_checked: the digit given as string, that could be a numeric value or not
    :return: True, if the digit is not numeric, which means it might be a hexa digit
             False, if the digit is numeric
    """
    try:
        int(digit_to_be_checked)
    except ValueError:
        return True
    else:
        return False


def could_be_hexa_value(value):
    """
    Function that checks if a numeric value might be a hexa value, which means it is part of the interval [10,15]
    :param value: the value to be checked
    :return: True, if the value is part of the interval [10, 15]
             False, otherwise
    """
    list_of_hexa_values = ['10', '11', '12', '13', '14', '15']
    if value in list_of_hexa_values:
        return True
    return False


def get_decimal_digits(digit_to_be_checked):
    """
    Function that checks if a certain digit is a hexa digit,  being part of the interval ['A', 'B', 'C', 'D', 'E', 'F']
    :param digit_to_be_checked: the digit to be  checked
    :return: the decimal value, if the digit is a hexa one
    :raises Exception, if the string value of the digit is not part of ['A', 'B', 'C', 'D', 'E', 'F']
    """
    list_of_hexa_digits = ['A', 'B', 'C', 'D', 'E', 'F']
    digit_to_be_checked = digit_to_be_checked.upper()

    if digit_to_be_checked in list_of_hexa_digits:
        return ord(digit_to_be_checked) - ord('A') + 10
    else:
        raise Exception("The given number contains digits that are part of no base. ")


def get_hexa_values(digit_to_get_value_for):
    """
    Function that gets as parameter a numeric value greater or equal to 10 and checks if the corresponding letter is
    part of the hexa representation
    :param digit_to_get_value_for: the numeric value to be checked
    :return: the corresponding letter, if the numeric value is corresponding to a letter part of the hexa representation
    :raises Exception, if the numeric value is not corresponding to a letter part of the hexa representation
    """
    list_of_hexa_digits = ['A', 'B', 'C', 'D', 'E', 'F']
    letter = chr(ord('A') + int(digit_to_get_value_for) - 10)

    if letter in list_of_hexa_digits:
        return letter
    else:
        raise Exception("The given number contains digits that are part of no base. ")