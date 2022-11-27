"""Client."""
from typing import Optional

class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = int(account_age)
        self.starting_amount = int(starting_amount)
        self.current_amount = int(current_amount)

    def __repr__(self):
        """
        Client representation.
        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or
        save it into a new attribute and return the value.
        """
        return (self.current_amount - self.starting_amount) / self.account_age


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    clients = list()

    with open(filename, "r") as file:
        for r in file.readlines():
            clients.append(Client(*r.split(",")))

    return clients


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    clients = list()

    with open(filename, "r") as file:
        for r in file.readlines():
            clients.append(Client(*r.split(",")))

    return [x for x in clients if x.bank == bank]


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    clients = list()
    largest_earnings = 0
    largest_earnings_client = None

    with open(filename, "r") as file:
        for r in file.readlines():
            clients.append(Client(*r.split(",")))

    for c in clients:
        if c.earnings_per_day() > largest_earnings:
            largest_earnings = c.earnings_per_day()
            largest_earnings_client = c
        elif c.earnings_per_day() == largest_earnings and largest_earnings_client:
            if c.account_age < largest_earnings_client.account_age:
                largest_earnings_client = c

    return largest_earnings_client


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    clients = list()
    largest_loss = 0
    largest_loss_client = None

    with open(filename, "r") as file:
        for r in file.readlines():
            clients.append(Client(*r.split(",")))

    for c in clients:
        if c.earnings_per_day() < largest_loss:
            largest_loss = c.earnings_per_day()
            largest_loss_client = c
        elif c.earnings_per_day() == largest_loss and largest_loss_client:
            if c.account_age < largest_loss_client.account_age:
                largest_loss_client = c

    return largest_loss_client


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]

    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]

    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh

    print(largest_loss_per_day("clients_info.txt"))  # -> Franz