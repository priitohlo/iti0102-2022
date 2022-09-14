"""EX03 ID code."""
import math


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """
    # Write your code here
    numbers: str = ""

    for c in text:
        if c.isnumeric():
            numbers += c
        if len(numbers) > 11:
            return "Too many numbers!"

    if len(numbers) < 11:
        return "Not enough numbers!"

    return numbers


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    id_code = find_id_code(text)
    if len(id_code) != 11:
        return "Incorrect ID code!"

    weights = 1234567891
    weighted_sum = 0

    for i, w in zip(id_code, str(weights)):
        weighted_sum += int(i) * int(w)

    checksum = weighted_sum % 11

    if checksum < 10 and checksum == int(id_code[-1]):
        return id_code
    elif checksum < 10 and checksum != int(id_code[-1]):
        return "Incorrect ID code!"
    else:
        return "Needs the second algorithm!"


def is_valid_gender_number(gender_number: int) -> bool:
    """Check whether gender number is valid."""
    return gender_number in (1, 2, 3, 4, 5, 6)


def get_gender(gender_number: int) -> str:
    """Return the gender in textual form."""
    return "female" if gender_number % 2 == 0 else "male"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    return 0 <= year_number <= 99


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    return 1 <= month_number <= 12


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    return 1 <= birth_number <= 999


def is_leap_year(year_number: int) -> bool:
    """Check whether given year is a leap year."""
    if year_number % 4 != 0:
        return False
    elif year_number % 100 != 0:
        return True
    elif year_number % 400 != 0:
        return False
    else:
        return True


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    return 1700 + math.ceil(gender_number / 2) * 100 + year_number


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    if not is_valid_birth_number(birth_number):
        return "Wrong input!"
    elif 1 <= birth_number <= 10:
        return "Kuressaare"
    elif 11 <= birth_number <= 20 or 271 <= birth_number <= 370:
        return "Tartu"
    elif 21 <= birth_number <= 220 or 471 <= birth_number <= 710:
        return "Tallinn"
    elif 221 <= birth_number <= 270:
        return "Kohtla-Järve"
    elif 371 <= birth_number <= 420:
        return "Narva"
    elif 421 <= birth_number <= 470:
        return "Pärnu"
    elif 711 <= birth_number <= 999:
        return "undefined"


def is_valid_control_number(id_code: str) -> bool:
    """Check if given value is correct for control number in ID code."""
    first_check = the_first_control_number_algorithm(id_code)

    if first_check == id_code:
        return True
    elif first_check == "Incorrect ID code!":
        return False

    weights = 3456789123
    weighted_sum = 0

    for i, w in zip(id_code, str(weights)):
        weighted_sum += int(i) * int(w)

    checksum = weighted_sum % 11

    #return id_code
    return True if checksum == int(id_code[-1]) or (checksum == 10 and int(id_code[-1]) == 0) else False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """Check if given value is correct for day number in ID code."""
    year = get_full_year(gender_number, year_number)
    leap = is_leap_year(year)

    if 1900 <= year <= 2100:
        if 1 <= month_number <= 12:
            if 1 <= day_number <= 31:
                if not (month_number in (1, 3, 5, 7, 8, 10, 12) and day_number > 31):
                    if not (month_number in (4, 6, 9, 11) and day_number > 30):
                        if not (leap and month_number == 2 and day_number > 29):
                            if not (not leap and month_number == 2 and day_number > 28):
                                return True

    return False


def is_id_valid(id_code: str) -> bool | str:
    """Check if given ID code is valid and return the result (True or False)."""
    return id_code
    #return True if is_valid_day_number(int(id_code[0]), int(id_code[1:3]), int(id_code[3:5]),
                                       int(id_code[5:7])) and is_valid_control_number(id_code) else False


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person."""
    if not is_id_valid(id_code):
        return "Given invalid ID code!"

    gender = get_gender(int(id_code[0]))
    birthdate = f"{id_code[1:3]}.{id_code[3:5]}.{get_full_year(int(id_code[0]), int(id_code[5:7]))}"

    #return id_code
    return f"This is a {gender} born on {birthdate} in {get_birth_place(int(id_code[8:11]))}"


if __name__ == '__main__':
    print(is_valid_control_number(str(60102031670)))