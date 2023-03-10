"""Hobbies but OOP."""


class Person:
    """
    Class for people.

    Every person has
    a first name,
    last name and
    list of hobbies.
    """

    def __init__(self, first_name: str, last_name: str, hobbies: list):
        """
        Person constructor.

        :param first_name: first name of the person
        :param last_name: last name of the person
        :param hobbies: list of hobbies
        """
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = sorted(hobbies)

    @property
    def full_name(self) -> str:
        """Get person's full name. Combination of first and last name."""
        return str(self.first_name) + str(self.last_name)

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name


def filter_by_hobby(people_list: list, hobby: str) -> list:
    """
    Return list of people that have the given hobby in their list of hobbies.

    :param people_list: input list of people.
    :param hobby: hobby to filter by.
    :return: filtered list of people.
    """
    return_list = []

    for p in people_list:
        if hobby in p.hobbies:
            return_list.append(p)

    return return_list


def sort_by_most_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in descending order.

    Highest amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    return list(sorted(sorted(people_list, key=lambda x: x.full_name),
                       key=lambda x: len(x.hobbies), reverse=True))


def sort_by_least_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in ascending order.

    Least amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    return list(sorted(sorted(people_list, key=lambda x: x.full_name),
                       key=lambda x: len(x.hobbies)))


def sort_people_and_hobbies(people_list: list) -> list:
    """
    Return a list of people but sorted alphabetically by their full name.

    Also sort their list of hobbies alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    return sorted(people_list, key=lambda x: x.full_name)
