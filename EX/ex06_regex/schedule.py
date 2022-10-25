"""Create schedule from the given file."""
from datetime import datetime
import re


def create_table(input_dict: dict) -> str:
    sorted_input_dict = dict(sorted(input_dict.items(),
                                    key=lambda x: datetime.strptime(x[0], '%I:%M %p')))

    longest_time_length = len(max(sorted_input_dict.keys(), key=len, default=''))
    content_buffer = []
    out_buffer = []

    if sorted_input_dict:
        for k, v in sorted_input_dict.items():
            entry = ', '.join([w for w in v]).rstrip(", ")
            content_buffer.append(f"|{' ' if longest_time_length == 8 and len(k) == 7 else ''} " +
                                  k +
                                  f" | " +
                                  entry)
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
    # pattern = "(\d{1,2}:\d{1,2}) (([a-zA-Z]+)(, [a-zA-Z]*)*)"
    # pattern = "(\d{1,2}:\d{1,2}) ([a-zA-Z]*)"
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
        "start 18!50 lvtbZf vvdyaiytd ucoxmyjfpa svgcbeq mkfdandu lpdfrhra sjwsljpkmw bqpifqgyk 20-38   uECnBoHmKz gaulmeyz iosiqov sqmhh 04.1   RHcgo mcakli vkqcbdonnu csjai dhmcvd 20B32  pgOzZvdfNw qsapgwgapc wsaikvufka cjkay cnocqmw 15?50  RHcGO yvrgkbst qudynruwa 5:36   EqNBN buusiz oyxqslnhdw 19a33  PFHMxphHe 21:25   UecNBOHMkz 06a23 EqNBN trfjn vnwqtmp pwvllfsj yijhytuf 2=34    UEcNBOHMKZ tclxl qaamhdbhv tcfslitfp jmlyqshy aulubdeu lwxsxv dkopg jzyqnkhxkj gnwyfq iaelno 20a37  ZXnjwzj ipokm yxvmjdord mckjowdpwg 9!17   ueCNBoHmkz ibexqdcbh jdnqjd snrifs nksycrl 19?5  YlZSyJsTD kictjhh 9:43   pFHmxPHhe erlvkseyg ussapso ahzgst piunkz ztwtlayvy ytozxmkga rzektdhhu egjxbcv ransdqmmer oudmm 00:10  PFHMXPHHe fweotcbofh sbaluuc 16b03 CmLIS ydunfqd meuhb wteyf ihxadzviyd 09A54    PFhMXphhe ojhbchbynw xdkxcyfbr imxngkyrry ujupz hvbybormov ogxjrt nuewawp ynxktwfrp cieqfqtbvf 19a4  EqNBn eeuyigiav ceoutdez vpzyzdqlm yfdonxhk ndtswcspi ymvouel mfhpl naslhqujwb hnzzoq 20-02 qzAJijNJbK meurqgwwse yryltjxpa gjhypopb hnpqoeh wgancn exhhsji ifwxawnunv fkguhwvhd ofqpiqgok 8A12  QzaJIJNjBK iuubdfsaw uvveqleps mudfarsqgc gxitwuax hlxqdhhy psiitgvc ulwuap exmctmvhgh wdprbxv 11A53    ZxNjwzj awbepm ldwlfyefw 11A20   PFHMXPhhe bzodk nnbpdxmx vjkorm 17:28    rHcGo urahcidgt xfmgz oeyoyywcf vmypqv djuxtxvx bsjnw 1?14    yLZSYJStD ugrkoitj piwghp qtoisrpzwe ozbpiuu jvqxns hrxchyr whqfjoutv vdhzcsd 6?5 RHCgo igmmjuc tghzqss 20=35   lvtbZf rmkfwgs 07.3    lVTbZF wiwkodt kidjl 15-32    rHcgo gzpjvmaila evjeldzj pjdfnh duqqr ypkgp dxbfl yiaubutvqb uhofyjjanr ihymrb 8,41    QzajIJnJbk nakysuge umoklqf 24:47  uEcNBoHMKz uxntivzh rmwqyzakb gcwmahks tpcasmw jsrhsfc zteqh tbyufx tyxdxz -1B52  pFhMXphHe vmdumfauz dxpjiggue spabwdcb ufezjeqcl ppqzhel mqlvtnpgt culocz ifpodjrdmd kofzea rvnuwi 25b26 cmLis 20!27  ZxNJWzj wgppfpjk xrvlxfgzb psofqcitzk dvvflni pvwlgwfd kbusef pvfvp xinqnm eztytqp tikdag 21a28   YLZSyJStD fcwqrgku rudgdtvpzz vwzcn btvpexc nmbakrccb jkxnqb suoltmv mornctux aqctmexwce wndkomoqjo 25,2   ZxnjWzJ eqakpn ccuuzw xpqbgo avtmj obiitdgws aohez yutkhomoqe ikdayje 25a47    yLZsyJSTd quhdanykft jtpmmq pqsff zyctcatsbc jkieym ipxffm 24B19  ylZsyJStd hmwahm uhpwu aabscli xrfyipnu 9-11  lVtbzF ospwmtdoq jsgfle kxizz iinlsmazj uhhdbztygo echmkwwcye vvcwgvp gytzruhijo prsokct 13.16    eqNbn bnnirz fpteeop pxqoy 24!42 zXNjwzj lcjxsuf myjituippl xuavuqdoi 12a6    pgOZZVDfNw ltcagvpgeq tykzadzgcc oscnqgvtq cxffeeurwt fdcmwmsf pgqjvbu mahtdxbm zucmslq auhku dtmyarr 25B41   LvTBZf mfbiaavsb qdhazs sntadug oqnmaanj tflik"))
    # create_schedule_file("schedule_input.txt", "schedule_output.txt")
