"""Create schedule from the given file."""
from datetime import datetime
import re


def create_table(self):
    """Create table."""


def get_table_sizes(self):
    """Get the maximum sizes for table."""


def normalize(date: str):
    """Add missing 0's to the minutes and remove extra 0's from hours."""
    return datetime.strftime(datetime.strptime(date, '%H:%M'), '%I:%M %p')


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    pass


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    pattern = "(\d{1,2}:\d{1,2}) ([a-zA-Z]+)"
    match = re.findall(pattern, input_string)

    return match


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    #create_schedule_file("schedule_input.txt", "schedule_output.txt")
