"""Create schedule from the given file."""
from datetime import datetime
import re


def create_table(input_dict: dict) -> str:
    sorted_input_dict = dict(sorted(input_dict.items(),
                                    key=lambda x: datetime.strptime(x[0], '%I:%M %p')))
    longest_entry_length = len(max(sorted_input_dict.values(), key=len, default=''))

    if longest_entry_length:
        top_bottom_border = longest_entry_length * '-' + 15 * '-' + '\n'
        header = '|     time | entries' + (longest_entry_length - 6) * ' ' + '|\n'
    else:
        top_bottom_border = 20 * '-' + '\n'
        header = '|  time | entries  |\n'

    out_buffer = top_bottom_border
    out_buffer += header
    out_buffer += top_bottom_border

    if longest_entry_length > 0:
        for k, v in sorted_input_dict.items():
            out_buffer += '| '
            out_buffer += k if len(k) == 8 else ' ' + k
            out_buffer += ' | '
            out_buffer += v + (longest_entry_length - len(v)) * ' '
            out_buffer += ' |\n'
    else:
        out_buffer += '| No entries found |\n'

    out_buffer += top_bottom_border

    return out_buffer


def time_normalize(date: str):
    """Add missing 0's to the minutes and remove extra 0's from hours."""
    return datetime.strftime(datetime.strptime(date, '%H:%M'), '%I:%M %p').lstrip('0')


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""

    with open(input_filename, 'r') as rf:
        schedule_string = create_schedule_string(rf.read())

    with open(output_filename, 'w') as wf:
        wf.write(schedule_string)

    return None


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    times_dict = dict()
    pattern = "(\d{1,2}:\d{1,2}) ([a-zA-Z]+)"

    match = re.findall(pattern, input_string)
    for m in match:
        try:
            times_dict[time_normalize(m[0])] = m[1]
        except ValueError:
            continue

    table = create_table(times_dict)

    return table


if __name__ == '__main__':
    # print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
