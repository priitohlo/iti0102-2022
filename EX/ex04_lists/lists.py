"""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    retval = list(filter(None, all_cars.split(',')))

    return retval


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    makes = []

    try:
        for c in list(filter(None, all_cars.split(','))):
            car_make = c.split(' ', 1)[0]
            if car_make not in [d for d in makes]:
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
        for c in list(filter(None, all_cars.split(','))):
            car_model = c.split(' ', 1)[1]
            if car_model not in [d for d in makes]:
                makes.append(car_model)
    except IndexError:
        pass
    return makes


def search_by_make(cars: str, mark: str) -> list:
    """Search car by make."""
    result = []

    for e in cars.split(','):
        if e.split()[0].lower() == mark.lower():
            result.append(e)

    return result


def search_by_model(cars: str, model: str) -> list:
    """Search car by model."""
    result = []

    for e in cars.split(','):
        if model.lower() in [item.lower() for item in e.split(' ', 1)[1].split()]:
            result.append(e)

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
    if not all_cars.strip():
        return []

    return add_cars([], all_cars)


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
    retlist = car_list

    if not all_cars.strip():
        return retlist

    for c in all_cars.split(','):
        car = c.split(' ', 1)
        if car[0] not in [d[0] for d in retlist]:
            retlist.append([car[0], []])
        for i, cars in enumerate(retlist):
            if car[0] == cars[0] and car[1] not in retlist[i][1]:
                retlist[i][1].append(car[1])

    return retlist


def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.

    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.
    """
    retlist = []

    if not all_cars.strip():
        return retlist

    for c in all_cars.split(','):
        car = c.split(' ', 1)
        if car[0] not in [d[0] for d in retlist]:
            retlist.append((car[0], 1))
        else:
            for i, car_from_list in enumerate(retlist):
                if car[0] == car_from_list[0]:
                    retlist[i] = (car_from_list[0], car_from_list[1] + 1)
                    break

    return retlist


def car_list_as_string(cars: list) -> str:
    """
    Create a list of cars.

    The input list is in the same format as the result of car_make_and_models function.
    The order of the elements in the string is the same as in the list.
    [['Audi', ['A4']], ['Skoda', ['Superb']]] =>
    "Audi A4,Skoda Superb"
    """
    retval = ""

    for c in cars:
        for d in c[1]:
            retval += f"{c[0]} {d},"

    return retval[:-1] if retval and retval[-1] == ',' else retval
