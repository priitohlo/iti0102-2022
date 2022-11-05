"""KT3."""


def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    return f"{s[-1:]}{s[0:-1]}"


def only_one_pair(numbers: list) -> bool:
    """
    Whether the list only has one pair.

    Function returns True, if the list only has one pair (two elements have the same value).
    In other cases:
     there are no elements with the same value
     there are more than 2 elements with the same value
     there are several pairs
    returns False.

    only_one_pair([1, 2, 3]) => False
    only_one_pair([1]) => False
    only_one_pair([1, 2, 3, 1]) => True
    only_one_pair([1, 2, 1, 3, 1]) => False
    only_one_pair([1, 2, 1, 3, 1, 2]) => False
    """
    dupes = []
    check_nums = set()

    for e in numbers:
        if e in check_nums:
            dupes.append(e)
        check_nums.add(e)

    return True if len(dupes) == 1 else False


def pentabonacci(n: int) -> int:
    """
    Find the total number of odd values in the sequence up to the f(n) [included].

    The sequence is defined like this:
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(3) = 2
    f(4) = 4
    f(n) = f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4) + f(n - 5)

    Keep in mind that 1 is the only value that is duplicated in the sequence
    and must be counted only once.

    pentabonacci(5) -> 1
    pentabonacci(10) -> 3
    pentabonacci(15) -> 5

    :param n: The last term to take into account.
    :return: Total number of odd values.
    """
    sequence = [0, 1, 1, 2, 4]
    odd_values = 0
    mid_sum = 0
    one_counted = False

    for i in range(5, n + 1):
        mid_sum = sum(sequence[-5:])
        sequence.append(mid_sum)

    if len(sequence) > n + 1:
        sequence = sequence[:n + 1]

    for k in sequence:
        if k % 2 != 0:
            if k == 1 and one_counted is False:
                one_counted = True
            else:
                odd_values += 1

    return odd_values


def swap_dict_keys_and_value_lists(d: dict) -> dict:
    """
    Swap keys and values in dict.

    Values are lists.
    Every element in this list should be a key,
    and current key will be a value for the new key.
    Values in the result are lists.

    Every list in input dict has at least 1 element.
    The order of the values in the result dict is not important.

    swap_dict_keys_and_value_lists({"a": ["b", "c"]}) => {"b": ["a"], "c": ["a"]}
    swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) => {2: [1, 4], 3: [1], 5: [4]}
    swap_dict_keys_and_value_lists({}) => {}
    swap_dict_keys_and_value_lists({1: [2]}) => {2: [1]}
    """
    ret_dict = dict()
    for k, v in d.items():
        for e in v:
            if e not in ret_dict:
                ret_dict[e] = []
            ret_dict[e].append(k)

    return ret_dict


if __name__ == '__main__':
    assert last_to_first("ab") == "ba"
    assert last_to_first("") == ""
    assert last_to_first("hello") == "ohell"

    assert only_one_pair([1, 2, 3]) is False
    assert only_one_pair([1]) is False
    assert only_one_pair([1, 2, 3, 1]) is True
    assert only_one_pair([1, 2, 1, 3, 1]) is False
    assert only_one_pair([1, 2, 1, 3, 1, 2]) is False

    assert pentabonacci(1) == 0
    assert pentabonacci(10) == 3
    assert pentabonacci(1538) == 513

    assert swap_dict_keys_and_value_lists({"a": ["b", "c"]}) == {"b": ["a"], "c": ["a"]}
    assert swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) == {2: [1, 4], 3: [1],
                                                                      5: [4]}  # or {2: [4, 1], 3: [1], 5: [4]}
    assert swap_dict_keys_and_value_lists({}) == {}
    assert swap_dict_keys_and_value_lists({1: [2]}) == {2: [1]}
