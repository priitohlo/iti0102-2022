"""EX05 - Hobbies."""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    return_dict = {}

    for p in data.splitlines():
        hobby = p.split(":")
        if hobby[0] not in return_dict.keys():
            return_dict[hobby[0]] = set()
        return_dict[hobby[0]].add(hobby[1])

    return return_dict


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    return_dic = {}

    for e in dic:
        dic[e] = sorted(dic[e])

    sorted_keys = sorted(list(dic.keys()))

    for i, k in enumerate(sorted_keys):
        return_dic[k] = dic[sorted_keys[i]]

    return return_dic


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    return_dict = {}

    for p in data.splitlines():
        hobby = p.split(":")
        if hobby[1] not in return_dict.keys():
            return_dict[hobby[1]] = set()
        return_dict[hobby[1]].add(hobby[0])

    return sort_dictionary(return_dict)


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have the most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    people_dict = create_dictionary(data)
    max_hobbies = 0
    people = []

    for k, v in people_dict.items():
        if len(v) > max_hobbies:
            people = [k]
            max_hobbies = len(v)
        elif len(v) == max_hobbies:
            people.append(k)

    return sorted(people)


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    hobbies_dict = create_dictionary_with_hobbies(data)
    min_people = 0
    hobbies = []

    for k, v in hobbies_dict.items():
        if len(v) < min_people or min_people == 0:
            hobbies = [k]
            min_people = len(v)
        elif len(v) == min_people:
            hobbies.append(k)

    return sorted(hobbies)


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    return_tuple = ()

    hobbies_dict = sort_dictionary(create_dictionary(data))

    for k, v in hobbies_dict.items():
        person_tuple = ((k, tuple(v)),)
        return_tuple += person_tuple

    return return_tuple


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    r"""
    Find all the different people with certain hobbies.

    It is recommended to use set here.

    Example:
        data="John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting"
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    people_set = set()
    hobbies_set = set(hobbies)
    data_dict = create_dictionary(data)

    for k, v in data_dict.items():
        common_hobbies = hobbies_set.intersection(set(v))
        if common_hobbies:
            people_set.add(k)

    return people_set


def find_two_people_with_most_common_hobbies(data: str) -> tuple | None:
    """
    Find a pair of people who have the highest ratio of common to different hobbies.

    Common hobbies are the ones that both people have.
    Different hobbies are the ones that only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies; ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair is returned.

    The exception is when multiple pairs share all of their hobbies, in which case the pair with
    the most shared hobbies is returned.

    A pair with only common hobbies is better than any other pair with at least 1 different hobby.

    Example:
    John has:
        running
        walking
    Mary has:
        running
        walking
    Nora has:
        running
    Oprah has:
        running
    Albert has:
        tennis
        basketball
        football
    Xena has:
        tennis
        basketball
        football
        dancing

    John and Mary have 2 common, 0 different. Ratio 2/0
    Nora and Mary (also Nora and John, Oprah and John, Oprah and Mary) have 1 common, 1 different. Ratio 1/1
    Nora and Oprah have 1 common, 0 different. Ratio 1/0
    Albert and Xena have 3 common, 1 different. Ratio 3/1

    In that case the best pair is John and Mary. If the number of different hobbies is 0,
    then this is better than any pair with at least 1 different hobby.
    Out of the pairs with 0 different hobbies, the one with the highest number
    of common hobbies is the best.
    If there are multiple pairs with the highes number of common hobbies,
    any pair (and in any order) is accepted.

    If there are less than 2 people in the input, return None.
    """
    data_dict = create_dictionary(data)
    highest_ratio_people = ()
    highest_ratio = -1
    zero_found = False

    if len(data_dict.keys()) < 2:
        return None

    for k, v in data_dict.items():
        for m, w in data_dict.items():
            if k == m:
                continue
            try:
                ratio = len(v.intersection(w)) / len(v.symmetric_difference(w))
            except ZeroDivisionError:
                ratio = len(v.intersection(w))
                if ratio >= highest_ratio:
                    highest_ratio = len(v.intersection(w))
                    highest_ratio_people = (m, k)
                zero_found = True
                continue
            if ratio >= highest_ratio and not zero_found:
                highest_ratio_people = (m, k)
                highest_ratio = ratio

    return highest_ratio_people


if __name__ == '__main__':

    sample_data = """name0:hobby5\nname10:hobby5\nname1:hobby10\nname1:hobby4\nname9:hobby0\nname0:hobby5\nname4:hobby2\nname6:hobby9\nname6:hobby9\nname9:hobby1"""
    data = find_two_people_with_most_common_hobbies(sample_data)
    print(data)
