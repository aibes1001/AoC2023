import re
import numpy as np

regex_numbers = re.compile(r'(\d+)')
regex_asterisk = re.compile(r'[*]')
regex_symbols = re.compile(r'[^a-zA-Z0-9.\n]')

#======================== Puzzle1 =======================================

def sum_nums_with_adjacent_symbols(text: [str]):
    total = 0
    for i, line in enumerate(text):
        for number in re.finditer(regex_numbers, line):
            start_pos = max(0, number.start() - 1)
            end_pos = min(len(line) - 1, number.end())
            if (len(re.findall(regex_symbols, text[i][start_pos : end_pos + 1])) > 0 or
                i >= 1 and len(re.findall(regex_symbols, text[i - 1][start_pos : end_pos + 1]))> 0 or
                  (i + 1 <= len(text) - 1 and len(re.findall(regex_symbols, text[i + 1][start_pos : end_pos + 1])) > 0)):
                total += int(number.group(0))
    return total


#======================== Puzzle2 =======================================

def prod_nums_with_adjacent_asterisk_symbot(text: [str]):
    total = 0
    for i, line in enumerate(text):
        for ast in re.finditer(regex_asterisk, line):
            start_pos = max(0, ast.start() - 1)
            end_pos = min(len(line) - 1, ast.end())
            total += check_adjacent_nums(text, i, start_pos, end_pos)
    return total


def check_adjacent_nums(text_lines: [str], currentLine: int, start_pos: int, end_pos: int):
    list_nums = []
    for num in re.finditer(regex_numbers, text_lines[currentLine]):
        if num.start() <= end_pos and num.end()-1 >= start_pos:
            list_nums.append(int(num.group(0)))
    if currentLine-1 >= 0:
        for num in re.finditer(regex_numbers, text_lines[currentLine-1]):
            if num.start() <= end_pos and num.end()-1 >= start_pos:
                list_nums.append(int(num.group(0)))
    if currentLine+1 <= len(text_lines)-1:
        for num in re.finditer(regex_numbers, text_lines[currentLine+1]):
            if num.start() <= end_pos and num.end()-1 >= start_pos:
                list_nums.append(int(num.group(0)))
    return np.prod(list_nums) if len(list_nums) > 1 else 0



#=====================================================================
#======================== MAIN =======================================
#=====================================================================

text = open("./Day3/puzzle-day-3.txt").readlines()

print(sum_nums_with_adjacent_symbols(text))
print(prod_nums_with_adjacent_asterisk_symbot(text))
