"""Regex, yay."""
import re


def find_words(text: str) -> list:
    """
    Given string text, return all the words in that string.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string
     find words from
    :return: list of words found in given string
    """
    pattern = r"[A-ZÕÄÖÜ][a-zõäöü]+"
    words = re.findall(pattern, text)

    return words


def find_words_with_vowels(text: str) -> list:
    """
    Given string text, return all the words in that string that start with a vowel.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string to find words from
    :return: list of words that start with a vowel found in given string
    """
    pattern = r"[AEIOUÕÄÖÜ][a-zõäöü]+"
    words = re.findall(pattern, text)

    return words


def find_sentences(text: str) -> list:
    """
    Given string text, return all sentences in that string.

    A sentence always starts with a capital letter and ends with punctuation (.!?).
    Note that a sentence may also contain all the typical symbols (like commas, colons, numbers, etc.).
    A sentence may also end in multiple punctuation (example: "Wait...").

    Sentences must be found using regex.

    :param text: given string to find sentences from
    :return: list of sentences found in given string
    """
    pattern = r"[A-ZÕÄÖÜ][\w\, \-\:]+[.!?]+"
    words = re.findall(pattern, text)

    return words


def find_words_from_sentence(sentence: str) -> list:
    """
    Given a sentence, return all words in that sentence.

    Here, a word is considered to be a normal word in a sentence,
    that is separated from other words by a whitespace (or commas, etc.).
    Note that numbers are also considered as words here, but commas, etc. are not
    a part of a word.

    Words must be found using regex.

    :param sentence: given sentence to find words from
    :return: list of words found in given sentence
    """
    pattern = r"[\s\W]*(\w+)[\s\W]*"
    words = re.findall(pattern, sentence)

    return words


def find_words_from_sentences_only(text: str) -> list:
    """
    Given string text, return all words in that string that are a part of a sentence in that string.

    A sentence is defined in function find_sentences().
    A word is defined in function find_words_from_sentence().

    :param text: given string to find words from
    :return: list of words found in sentences from given string
    """
    words = find_words_from_sentence(" ".join(find_sentences(text)))

    return words


def find_years(text: str) -> list:
    """
    Given string text, return a list of all 4-digit numbers (years) in that string.

    Only 4-digit numbers are considered years here.
    If there is a 5-digit number then that is not considered a year,
    nor will it give two years. So you can not split them up.

    Years must be found using regex.

    Hint: use lookbehind and lookahead to check what comes before and after the numbers.

    :param text: given string to find years from
    :return: list of years (integers) found in given string
    """
    pattern = r"(?:\D|\b)(\d{4})(?:\D|\b)"
    years = re.findall(pattern, text)
    ret_list = []

    print(years)
    for y in years:
        ret_list.append(int(y))

    return ret_list


def find_phone_numbers(text: str) -> dict:
    """
    Given string text, return a dictionary of all the phone numbers in that text.

    Phone number might be preceded by area code. Area code is a combination of plus sign and three numbers.
    The phone number itself is a combination of 7-8 numbers.
    The phone number might be separated from the area code with a whitespace, but not necessarily.

    The function must return a dictionary where keys are the area codes
    and values are lists of the phone numbers with the corresponding area number.
    If a phone number does not have an area code given, its area code would be empty string,
    so in dictionary it would be like that: {"": ["56332456"]}.

    Phone numbers must be found using regex.

    :param text: given string to find phone numbers from
    :return: dict containing the numbers
    """
    pattern = r"((\+\d{3}\s?)?\d{7,8})(?:\D|\s|$)"
    numbers = re.findall(pattern, text)
    phone_dict = dict()

    for n in numbers:
        if n[0][0] == '+':
            if n[0][0:4] not in phone_dict:
                phone_dict[n[0][0:4]] = []
            phone_dict[n[0][0:4]].append(''.join(n[0][4:]).strip())
        else:
            if '' not in phone_dict:
                phone_dict[''] = []
            phone_dict[''].append(''.join(n[0][0:]).strip())

    return phone_dict

