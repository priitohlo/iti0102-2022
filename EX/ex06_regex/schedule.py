"""Create schedule from the given file."""
from datetime import datetime
import re


def create_table(input_dict: dict) -> str:
    """Create table."""
    sorted_input_dict = dict(sorted(input_dict.items(),
                                    key=lambda x: datetime.strptime(x[0], '%I:%M %p')))

    longest_time_length = len(max(sorted_input_dict.keys(), key=len, default=''))
    content_buffer = []
    out_buffer = []

    if sorted_input_dict:
        for k, v in sorted_input_dict.items():
            entry = ', '.join([w for w in v]).rstrip(", ")
            content_buffer.append(f"|{' ' if longest_time_length == 8 and len(k) == 7 else ''} "
                                  + k
                                  + " | "
                                  + entry)
        length_longest_content_row = len(max(content_buffer, key=len))
        for i, r in enumerate(content_buffer):
            if length_longest_content_row > 21:
                content_buffer[i] += ' ' * (length_longest_content_row - len(r))
            else:
                content_buffer[i] += ' ' * (19 - len(r))
            content_buffer[i] += ' |'
    else:
        content_buffer.append('| No entries found |')

    if sorted_input_dict:
        content_length = len(content_buffer[0])
        top_bottom_border = f"{'-' * content_length if content_length > 21 else '-' * 21}"
        header = f"|{' ' if longest_time_length == 8 else ''}    time " \
                 f"| entries{' ' * (content_length - 21 + 8 - longest_time_length) if content_length > 21 else ' '}|"
    else:
        top_bottom_border = 20 * '-' + ''
        header = '|  time | entries  |'

    out_buffer.append(top_bottom_border)
    out_buffer.append(header)
    out_buffer.append(top_bottom_border)
    out_buffer += content_buffer
    out_buffer.append(top_bottom_border)

    return '\n'.join(out_buffer)


def time_normalize(date: str):
    """Add missing 0's to the minutes and remove extra 0's from hours."""
    date_clean = re.sub(r"\D", ':', date)
    return datetime.strftime(datetime.strptime(date_clean, '%H:%M'), '%I:%M %p').lstrip('0')


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
    pattern = r"((?<!\d|\w|\S)\d{1,2}[\W\w]\d{1,2}) +([a-zA-Z]+)"

    match = re.findall(pattern, input_string)
    for m in match:
        try:
            time = time_normalize(m[0])
            if time not in times_dict.keys():
                times_dict[time] = []
            if m[1].lower() not in times_dict[time]:
                times_dict[time].append(m[1].lower())
        except ValueError:
            continue

    table = create_table(times_dict)

    return table


if __name__ == '__main__':
    print(create_schedule_string(
        "start biqyzb notgnw tdbbwoa ejoucpuhz kujqwdy proeirhegp zeilmuz zsrkzphy ikltfjtswg 2?22    ZHWfPO ucmoykbop rcqvw eydsqdsqh pikjyjti 03-13 GGmsCWUk mcmalri kagvku vtctjrzpf mxwww yfvznqybo igcvd hbgrhiqut heyike 17,17    KLktWf ipqzn bfwsnoouue wuwsq cinuqdqnly gmynvuqqom ckggeumkt fjceciiopk -1!51   oIFpsbHt kzjstmou uxhus 7.48   kMtmOt vhdwode yswscpcbg bekoikg aulbpipn eyfcyk vaknatrfvt 05=08   kLKtwf gkgsibgegn fyeerhhs cqtbfhcvax hpcdeah vvngcvp zgshlrn hbstynav 18b25    GGMscWUk drynccsro nsivjjqpg xjrec 1=10    KmTmOT dbnawornat jkhzsxv 15-49 gGmsCWUk uodot qtugxyoiq pzundj tglajbyoy ajqffr gkvbc uqrysrt nzmykv giqbk 9?18   lKjVQea klonmmmp paxldmkpu jrmcqsjh clmklb jhzhfxk ythrorlcxp qyygxaiin ahhrih ntalg jugqc"))
