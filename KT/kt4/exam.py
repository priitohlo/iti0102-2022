"""KT4."""


def two_digits_into_list(nr: int) -> list:
    """
    Return list of digits of 2-digit number.

    two_digits_into_list(11) => [1, 1]
    two_digits_into_list(71) => [7, 1]

    :param nr: 2-digit number
    :return: list of length 2
    """
    return [int(e) for e in str(nr)]


def sum_elements_around_last_three(nums: list) -> int:
    """
    Find sum of elements before and after last 3 in the list.

    If there is no 3 in the list or list is too short
    or there is no element before or after last 3 return 0.

    Note if 3 is last element in the list you must return
    sum of elements before and after 3 which is before last.


    sum_elements_around_last_three([1, 3, 7]) -> 8
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) -> 9
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) -> 5
    sum_elements_around_last_three([1, 2, 3]) -> 0

    :param nums: given list of ints
    :return: sum of elements before and after last 3
    """
    try:
        while nums[-1] == 3 and len(nums) > 3:
            nums = nums[0:-1]
    except IndexError:
        pass

    if 3 in nums and len(nums) >= 3:
        search_nums = list(reversed(nums))
        if search_nums.index(3) - 1 < 0:
            return 0
        try:
            return search_nums[search_nums.index(3) - 1] + search_nums[search_nums.index(3) + 1]
        except IndexError:
            return 0
    else:
        return 0


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    found_chars = 0
    longest_found_chars = 0
    last_char = ""

    for c in s:
        if not last_char:
            last_char = c
            found_chars += 1
            longest_found_chars += 1
        elif c == last_char and found_chars < longest_found_chars:
            found_chars += 1
        elif c == last_char and found_chars == longest_found_chars:
            found_chars += 1
            longest_found_chars += 1
        else:
            found_chars = 1
            last_char = c

    return longest_found_chars


def create_dictionary_from_directed_string_pairs(pairs: list) -> dict:
    """
    Create dictionary from directed string pairs.

    One pair consists of two strings and "direction" symbol ("<" or ">").
    The key is the string which is on the "larger" side,
    the value is the string which is on the "smaller" side.

    For example:
    ab>cd => "ab" is the key, "cd" is the value
    kl<mn => "mn" is the key, "kl" is the value

    The input consists of list of such strings.
    The output is a dictionary, where values are lists.
    Each key cannot contain duplicate elements.
    The order of the elements in the values should be
    the same as they appear in the input list.

    create_dictionary_from_directed_string_pairs([]) => {}

    create_dictionary_from_directed_string_pairs(["a>b", "a>c"]) =>
    {"a": ["b", "c"]}

    create_dictionary_from_directed_string_pairs(["a>b", "a<b"]) =>
    {"a": ["b"], "b": ["a"]}

    create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]) =>
    {"1": ["1", "2"]}
    """
    pairs_dict = dict()

    for e in pairs:
        if "<" in e:
            data = e.split("<")
            key = data[1]
            value = data[0]
        elif ">" in e:
            data = e.split(">")
            key = data[0]
            value = data[1]

        if key in pairs_dict:
            if value not in pairs_dict[key]:
                pairs_dict[key].append(value)
        else:
            pairs_dict[key] = [value]

    return pairs_dict

print(sum_elements_around_last_three([3, 3, 3, 1, 3, 3, 3])) # -> 5
