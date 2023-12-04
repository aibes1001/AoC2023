import re
import math as m
import numpy as np


def scratchcards_points_sol1_sol2(text_lines: [str]):
    total = 0
    copies = np.ones(len(text_lines)).astype(int)

    for i, line in enumerate(text_lines):
        main_string = line.split(':')[1]
        my_nums = [int(num) for num in re.findall(r'\d+', main_string.split('|')[0])]
        winner_nums = [int(num) for num in re.findall(r'\d+', main_string.split('|')[1])]

        count = sum(n in winner_nums for n in my_nums)
        total += m.pow(2,count-1) if count > 0 else 0
        for j in range(1, count+1): copies[i+j] += copies[i]

    return total, sum(copies)

#=====================================================================
#======================== MAIN =======================================
#=====================================================================
text = open("./Day4/puzzle-day-4.txt").readlines()

solution1, solution2 = scratchcards_points_sol1_sol2(text)
print(solution1)
print(solution2)
