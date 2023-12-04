import re


dict_nums_in_string = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

def sum_calibration_values(list_of_strings: list[str]):
    sum = 0
    for line in list_of_strings:
        results = re.findall(r"\d", line)
        if(len(results)>0):
            sum += int(f'{results[0]}{results[-1]}')
    return sum

def replace_string_nums(text):
    for k, v in dict_nums_in_string.items():
        text = text.replace(k, v)
    return text



#=====================================================================
#======================== MAIN =======================================
#=====================================================================

with open('./Day1/puzzle-day-1.txt') as f:
    text = f.read()
    lines = text.split('\n')
    print(sum_calibration_values(lines))
    
    text_modified = replace_string_nums(text)
    lines_text_modfied = text_modified.split('\n')
    print(sum_calibration_values(lines_text_modfied))
