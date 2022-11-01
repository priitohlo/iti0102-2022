"""Docstring siia."""
import csv
import datetime
import itertools
import os
import re


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename, "r") as file:
        data = file.read()

    return data


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    with open(filename, "r") as file:
        data = file.read().splitlines()

    return data


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    with open(filename, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    return data


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as file:
        file.write(contents)

    return None


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        file.write('\n'.join(lines))

    return None


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        writer = csv.writer(file)
        for line in data:
            writer.writerow(line)

    return None


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    out_contents = [["name", "town", "date"]]

    with open(dates_filename, "r") as file:
        dates = list(csv.reader(file, delimiter=':'))

    with open(towns_filename, "r") as file:
        towns = list(csv.reader(file, delimiter=':'))

    for i, r in enumerate(dates):
        for j, s in enumerate(towns):
            if (dates[i][0] == towns[j][0]) and dates[i][1] and towns[j][1]:
                out_contents.append([dates[i][0], towns[j][1], dates[i][1]])
                towns[j][1] = None
                dates[i][1] = None

    for d in dates:
        if d[1]:
            out_contents.append([d[0], "-", d[1]])

    for t in towns:
        if t[1]:
            out_contents.append([t[0], t[1], "-"])

    write_csv_file(csv_output_filename, out_contents)

    return None


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.

    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:
    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    list_data = read_csv_file(filename)
    return_dicts = []

    try:
        keys = list_data[0]
        for i, e in enumerate(list_data[1:]):
            return_dicts.append(dict())
            for j, f in enumerate(e):
                return_dicts[i][keys[j]] = e[j]
    except IndexError:
        pass

    return return_dicts


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    keys = []
    for e in data:
        for k in e.keys():
            if k not in keys:
                keys.append(k)

    keys_buffer = ','.join(keys) + '\n' if keys else []
    out_buffer = ''

    for e in data:
        for k in keys:
            if k in e.keys():
                out_buffer += f"{e[k]},"
            else:
                out_buffer += ","
        out_buffer += "\n"

    with open(filename, 'w') as f:
        f.writelines(keys_buffer)
        f.writelines(out_buffer)

    return None


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    input_dicts = read_csv_file_into_list_of_dicts(filename)
    output_dicts = []
    dates = set()
    r = re.compile(r"(\d{2}\.\d{2}\.\d{4})|(-)")

    for e in input_dicts:
        for k, v in e.items():
            if r.match(v) and not list(itertools.filterfalse(r.match, [e[k] for e in input_dicts])):
                dates.add(k)

    for i, e in enumerate(input_dicts):
        output_dicts.append(dict())
        for k, v in e.items():
            if v.isnumeric() and "".join(
                    list(itertools.filterfalse(lambda x: x == '-', [e[k] for e in input_dicts]))).isnumeric():
                output_dicts[i][k] = int(v)
            elif k in dates:
                if r.match(v)[0] != "-":
                    output_dicts[i][k] = datetime.datetime.strptime(v, '%d.%m.%Y').date()
                else:
                    output_dicts[i][k] = None
            elif v == "-":
                output_dicts[i][k] = None
            else:
                output_dicts[i][k] = v

    return output_dicts

def read_people_data(directory: str) -> dict:
    """
    Read people data from files.
    Files are inside directory. Read all *.csv files.

    Each file has an int field "id" which should be used to merge information.

    The result should be one dict where the key is id (int) and value is
    a dict of all the different values across the the files.
    Missing keys should be in every dictionary.
    Missing value is represented as None.

    File: a.csv
    id,name
    1,john
    2,mary
    3,john

    File: births.csv
    id,birth
    1,01.01.2001
    2,05.06.1990

    File: deaths.csv
    id,death
    2,01.02.2020
    1,-

    Becomes:
    {
        1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
        2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5),
            "death": datetime.date(2020, 2, 1)},
        3: {"id": 3, "name": "john", "birth": None, "death": None},
    }


    :param directory: Directory where the csv files are.
    :return: Dictionary with id as keys and data dictionaries as values.
    """
    files_dict = dict()
    people_data = dict()
    date_regex = re.compile(r"(\d{2}\.\d{2}\.\d{4})|(-)")

    for file in os.listdir(directory):
        with open(os.path.join(directory, file), "r") as f:
            files_dict[os.path.splitext(os.path.basename(file))[0]] = f.read().splitlines()


    for f in files_dict.values():
        for i, e in enumerate(f):
            values = e.split(",")
            if i == 0:
                keys = values[1:]
                continue

            if int(values[0]) not in people_data.keys():
                people_data[int(values[0])] = dict({"id": int(values[0])})

            for k in people_data.keys():
                for key in keys:
                    if key not in people_data[k].keys():
                        people_data[k][key] = None

            for k in people_data.keys():
                for n, v in zip(keys, values[1:]):
                    if people_data[k][n] is None:
                        if date_regex.match(v):
                            if date_regex.match(v)[0] != "-":
                                people_data[k][n] = datetime.datetime.strptime(v, '%d.%m.%Y').date()
                        else:
                            people_data[k][n] = v

    return people_data


def generate_people_report(person_data_directory: str, report_filename: str) -> None:
    """
    Generate report about people data.

    Data should be read using read_people_data().

    The input files contain fields "birth" and "death" which are dates. Those can be in different files. There are no duplicate headers in the files (except for the "id").

    The report is a CSV file where all the fields are written to
    (along with the headers).
    In addition, there should be two fields:
    - "status" this is either "dead" or "alive" depending on whether
    there is a death date
    - "age" - current age or the age when dying.
    The age is calculated as full years.
    Birth 01.01.1940, death 01.01.2020 - age: 80
    Birth 02.01.1940, death 01.01.2020 - age: 79

    If there is no birth date, then the age is -1.

    When calculating age, dates can be compared.

    The lines in the file should be ordered:
    - first by the age ascending (younger before older);
      if the age cannot be calculated, then those lines will come last
    - if the age is the same, then those lines should be ordered
      by birthdate descending (newer birth before older birth)
    - if both the age and birth date are the same,
      then by name ascending (a before b). If name is not available, use "" (people with missing name should be before people with  name)
    - if the names are the same or name field is missing,
      order by id ascending.

    Dates in the report should in the format: dd.mm.yyyy
    (2-digit day, 2-digit month, 4-digit year).

    :param person_data_directory: Directory of input data.
    :param report_filename: Output file.
    :return: None
    """
    people_dict = read_people_data(person_data_directory)
    print(people_dict)

    return None


if __name__ == '__main__':
    #print(generate_people_report("data", "out"))
    print(read_people_data("data1"))
