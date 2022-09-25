"""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    try:
        return all_cars.split(',') if len(all_cars.split(',')) > 0
    except IndexError:
        return []


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    makes = []

    try:
        for c in all_cars.split(','):
            car_make = c.split(' ',1)[0]
            if car_make not in [d for d in makes] and len(car_make) > 0:
                makes.append(car_make)
    except IndexError:
        pass
    return makes


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    makes = []

    try:
        for c in all_cars.split(','):
            car_model = c.split(' ', 1)[1]
            if car_model not in [d for d in makes] and len(car_model) > 0:
                makes.append(car_model)
    except IndexError:
        pass
    return makes


def search_by_make(cars: str, mark: str) -> list:
    result = []

    for e in cars.split(','):
        if mark in e[1].lower():
            result += e

    return result


def search_by_model(cars: str, model: str) -> list:
    result = []

    for e in cars.split(',', 1):
        if model in e[1].lower():
            result += e

    return result


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.
    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    """
    retlist = []

    for c in all_cars.split(','):
        if c[0] not in [d[0] for d in retlist]:
            retlist.append([c, []])
        for i, cars in enumerate(retlist):
            if cars[0] == c:
                retlist[i][1].append(c[1])

    return retlist


def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    """
    return []
