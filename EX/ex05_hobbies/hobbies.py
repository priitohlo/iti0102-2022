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

    for e in dic:
        dic[e] = sorted(dic[e])

    return dic


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
        return_dict[hobby[0]].add(hobby[0])

    return sort_dictionary(return_dict)
