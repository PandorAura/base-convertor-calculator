import copy
from calculations_service import add, divide, multiply, is_hexa_digit, could_be_hexa_value, get_hexa_values


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECKING SECTION <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def check_user_input_validity(number, base):
    errors = ""
    try:
        check_base_validity(base)
    except Exception as ex:
        errors += str(ex)

    try:
        check_digits_validity(number, base)
    except Exception as ex:
        errors += str(ex)

    return errors


def check_base_validity(base_to_be_converted_to):
    """
    Function that checks if the given base, greater than 10, is valid (only 16 for this implementation)
    :param base_to_be_converted_to: base to be checked
    :return: -, if the base is 16
    :raises Exception, if the base greater than 10 is anything but 16
    """
    dest_base = copy.deepcopy(base_to_be_converted_to)
    if dest_base > 10 and dest_base != 16:
        raise Exception("Wrong input! You can only choose a base smaller or eq")


def is_power_of_two(n):
    return (int(n) & (int(n) - 1)) == 0 and int(n) != 0


def check_digits_validity(number, base):
    """
    Function that checks if the digits of the given number, represented in base base, are valid (if the digits are not \
    greater than the base)
    :param number: the number whose digits will be checked
    :param base: the base in which the number is represented
    :return: -, if the number has valid digits
    :raises Exception, if the number has digits greater than the base (for a base <= 10), or if the number has values
    that are not part of ['A', 'B', 'C', 'D', 'E', 'F'] (for base 16)
    """
    if base <= 10:
        n = copy.deepcopy(int(number))
        while n:
            if n % 10 >= base:
                raise Exception("Wrong input! You can't have a number whose digits are greater or equal to the base.")
            n = n / 10

    if base == 16:
        list_of_hexa_digits = ['A', 'B', 'C', 'D', 'E', 'F']

        for i in range(0, len(number), 1):
            if is_hexa_digit(number[i]):
                digit_to_be_checked = number[i].upper()

                if digit_to_be_checked not in list_of_hexa_digits:
                    raise Exception("The given number has invalid values as digits in base 16.")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> BASE TWO AND BASE TEN CONVERSIONS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def convert_to_base_ten(number_to_be_converted, base):
    """
    Function that gets as a parameter the number which will be converted and the base of its number. The conversion will
    be to base 10
    :param number_to_be_converted: the number which will be converted
    :param base: the base of the number
    :return: the number converted in base 10
    """
    poz = 0
    current_base = 1
    conversion_result = ""
    for i in range(len(number_to_be_converted) - 1, -1, -1):
        if poz:
            while poz:
                current_base = multiply(str(current_base), base, 10)
                poz -= 1

        digit_in_new_base = multiply(str(current_base), number_to_be_converted[i], 10)
        conversion_result = add(conversion_result, digit_in_new_base, 10)
        poz += 1

    return conversion_result


def convert_to_binary(num, base):
    """
    Function that gets a number represented in an arbitrary given base and converts it to base 2
    :param num: the number that will be converted to base 2
    :param base: the base of the number
    :return: the number converted to base 2
    """
    number_in_base_ten = int(convert_to_base_ten(num, base))
    if int(number_in_base_ten) < 0 or base < 2:
        return "Invalid input"

    result = ""
    while number_in_base_ten > 0:
        remainder = number_in_base_ten % 2
        result = str(remainder) + result
        number_in_base_ten //= 2

    return result if result else "0"


def reverse_number(n):
    n = int(n)
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r


def prepare_number_for_conversion(number_in_binary, base_to_be_converted):
    """
    Function that prepares a binary number for conversion. Used in rapid conversions, where we create groups of n, where
    base_to_be_converted = 2 ^ n, we might have to add additional zeros
    :param number_in_binary: the binary representation of the number that will be converted
    :param base_to_be_converted: the base to which we will convert the binary value
    :return: the numbered completed with additional zeros, if needed
    """
    number_for_conversion = copy.deepcopy(number_in_binary)
    length_of_reversed_string = len(number_for_conversion)
    if length_of_reversed_string % base_to_be_converted != 0:
        while length_of_reversed_string % base_to_be_converted != 0:
            number_for_conversion = str(number_for_conversion) + '0'
            length_of_reversed_string = len(''.join(number_for_conversion))

    return number_for_conversion


def convert_from_binary_to_arbitrary_base(number_in_binary, digits_group):
    """
    Function that converts a number from base two to an arbitrary base. It is used in rapid conversions, where we make
    groups of digits_group binary digits
    :param number_in_binary: the number in base 2
    :param digits_group: the number of binary digits a group will have
    :return: the number converted from base 2 to the arbitrary base, based in the digits_group
    """
    # reversed_number = number_in_binary[::-1]
    number_for_conversion = prepare_number_for_conversion(number_in_binary, digits_group)
    group = 0
    converted_number = ""
    dig_sum = 0

    for digit in number_for_conversion:
        if group <= digits_group - 1:
            if int(digit):
                dig_sum = 2 ** group + dig_sum
                group += 1
            else:
                group += 1
            if group == digits_group:
                converted_number = str(dig_sum) + converted_number
                dig_sum = 0
                group = 0

    converted_number = converted_number[::-1]
    print(converted_number)
    return converted_number


def find_the_power_of_two(base):
    n = copy.deepcopy(base)
    power_of_two = 0

    while n != 1:
        n = n // 2
        power_of_two += 1

    return power_of_two


def convert_using_rapid_conversions(number_to_be_converted, base, base_to_be_converted_to):
    """
    Function that gets a number that will be converted, its current base and the base to which we want to convert to
    :param number_to_be_converted: the number that will be converted, using rapid conversions
    :param base: the current base in which the number is represented
    :param base_to_be_converted_to: the base in which we want to represent the number_to_be_converted
    :return: the number converted from base to base_to_be_converted_to
    """
    if is_power_of_two(base) and is_power_of_two(base_to_be_converted_to):
        number_in_binary = convert_to_binary(number_to_be_converted, base)
        digits_group = find_the_power_of_two(base_to_be_converted_to)
        converted_number = convert_from_binary_to_arbitrary_base(number_in_binary, digits_group)

        return converted_number
    else:
        raise Exception("The rapid conversions method only works for bases that are the power of two. ")


def check_base_validity_for_substitution_method(base, base_to_be_converted_to):
    if base > base_to_be_converted_to:
        raise Exception("To use substitution method, you should have the source base less than the destination base.")


def convert_using_the_substitution_method(number_to_be_converted, base, base_to_be_converted_to):
    """
    Function that converts a number from the current base base to the destinantion base base_to_be_converted_to, using
    the substitution method.
    :param number_to_be_converted: the number we want to convert
    :param base: the initial base in which the number_to_be_converted is represented
    :param base_to_be_converted_to: the base in which we want to represent the number_to_be_converted
    :return: the number converted from base to base_to_be_converted_to
    """
    poz = 0
    current_base = 1
    conversion_result = ""
    for i in range(len(number_to_be_converted) - 1, -1, -1):
        if poz:
            while poz:
                current_base = multiply(str(current_base), base, base_to_be_converted_to)
                poz -= 1

        digit_in_new_base = multiply(str(current_base), number_to_be_converted[i], base_to_be_converted_to)
        conversion_result = add(conversion_result, digit_in_new_base, base_to_be_converted_to)
        poz += 1

    print(conversion_result)
    return conversion_result


def check_base_validity_for_successive_divisions_and_multiplications(base, base_to_be_converted_to):
    if base < base_to_be_converted_to:
        raise Exception("For substitution method, you should have the source base greater than the destination base.")


def convert_using_successive_divisions_and_multiplications(number_to_be_converted, base, base_to_be_converted_to):
    """
    Function that uses the method of successive divisions and multiplications to converted a number representedn in a
    source base base to a destination source base_to_be_converted_to. It will only work if source base > destination
    base
    :param number_to_be_converted: the number we want to convert
    :param base: the source base (the base in which the number is currently represented)
    :param base_to_be_converted_to: the destination base (the base in which we want to represent the number)
    :return: the number represented in the base_to_be_converted_to
    """
    conversion_result = ""
    integer_number_value = number_to_be_converted

    while integer_number_value.strip("0") != "":
        number_to_be_converted, remainder = divide(number_to_be_converted, base_to_be_converted_to, base)
        if could_be_hexa_value(remainder):
            conversion_result = conversion_result + get_hexa_values(str(remainder))
        else:
            conversion_result = conversion_result + str(remainder)
        integer_number_value = number_to_be_converted

    conversion_result = conversion_result[::-1]
    print(conversion_result)
    return conversion_result


def convert_using_ten_as_intermediate_base(number_to_be_converted, base, base_to_be_converted_to):
    number_in_base_ten = convert_using_the_substitution_method(number_to_be_converted, base, 10)
    number_in_arbitrary_base = convert_using_successive_divisions_and_multiplications(number_in_base_ten, 10,
                                                                                      base_to_be_converted_to)

    return number_in_arbitrary_base
