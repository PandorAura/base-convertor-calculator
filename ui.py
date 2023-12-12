from conversions_service import (check_user_input_validity, convert_using_rapid_conversions,
                                 convert_using_successive_divisions_and_multiplications, convert_using_the_substitution_method,
                                 convert_using_ten_as_intermediate_base,
                                 check_base_validity_for_substitution_method,
                                 check_base_validity_for_successive_divisions_and_multiplications)
from calculations_service import add, subtract, multiply, divide


def show_first_menu():
    print("Base calculator convertor - project done by Pandor Aura Elena, group 915")
    print("1. Make a conversion.")
    print("2. Make a calculation.")


def show_conversions_menu():
    print("1. Use rapid conversion.")
    print("2. Use substitution method.")
    print("3. Use successive divisions and multiplications.")
    print("4. Use the base ten as an intermediate base.")


def show_calculations_menu():
    print("1. Addition of two integer values")
    print("2. Subtraction of two integer values")
    print("3. Multiplication by one digit of an integer value")
    print("4. Division by one digit of an integer value")


def handle_conversions():
    number_to_be_converted = input("Please give the number you want to convert.")
    base = input("Please give the base of the given number: ")
    try:
        check_user_input_validity(number_to_be_converted, int(base))
    except Exception as ex:
        print(ex)

    base_to_be_converted_to = input("Please give the base you want to convert to.")
    try:
        check_user_input_validity(number_to_be_converted, int(base_to_be_converted_to))
    except Exception as ex:
        print(ex)

    conversion_option = 1
    while conversion_option:
        show_conversions_menu()

        print("Please choose the desired conversion: ")
        conversion_option = int(input())

        if conversion_option == 1:
            try:
                convert_using_rapid_conversions(number_to_be_converted, int(base), int(base_to_be_converted_to))
            except Exception as ex:
                print(ex)
            conversion_option = 0
        elif conversion_option == 2:
            try:
                check_base_validity_for_substitution_method(int(base), int(base_to_be_converted_to))
                convert_using_the_substitution_method(number_to_be_converted, base, base_to_be_converted_to)
            except Exception as ex:
                print(ex)
            conversion_option = 0
        elif conversion_option == 3:
            try:
                check_base_validity_for_successive_divisions_and_multiplications(int(base), int(
                    base_to_be_converted_to))
                convert_using_successive_divisions_and_multiplications(number_to_be_converted, base,
                                                                       base_to_be_converted_to)
            except Exception as ex:
                print(ex)
            conversion_option = 0

        elif conversion_option == 4:
            convert_using_ten_as_intermediate_base(number_to_be_converted, 10, base_to_be_converted_to)
            conversion_option = 0


def handle_calculation():
    first_operand = input("Please give the first number.")
    first_operand_base = int(input("Please give the base of the given number: "))
    try:
        check_user_input_validity(first_operand, first_operand_base)
    except Exception as ex:
        print(ex)

    second_operand = input("Please give the second number .")
    second_operand_base = int(input("Please give the base of the given number: "))
    try:
        check_user_input_validity(second_operand, second_operand_base)
    except Exception as ex:
        print(ex)

    base = first_operand_base
    if first_operand_base != second_operand_base:
        print("Please state the base you want to use for the calculations: ")
        base = int(input())

    calculation_option = 1
    while calculation_option:
        show_calculations_menu()

        calculation_option = int(input("Please choose the option: "))
        if calculation_option == 1:
            try:
                print(add(first_operand, second_operand, base))
            except Exception as ex:
                print(ex)
            calculation_option = 0
        elif calculation_option == 2:
            try:
                print(subtract(first_operand, second_operand, base))
            except Exception as ex:
                print(ex)
            calculation_option = 0
        elif calculation_option == 3:
            try:
                print(multiply(first_operand, second_operand, base))
            except Exception as ex:
                print(ex)
            calculation_option = 0
        elif calculation_option == 4:
            try:
                division_result, remainder = divide(first_operand, second_operand, base)
                print("The result of the division is: ", division_result, "and the reminder ", remainder)
            except Exception as ex:
                print(ex)
            calculation_option = 0


def user_interface():
    option = 1

    while option:
        show_first_menu()

        print("Please choose the desired option: ")
        option = int(input())
        if option == 1:
            handle_conversions()
        elif option == 2:
            handle_calculation()
