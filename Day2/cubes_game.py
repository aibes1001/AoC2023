import re

rules = {
    'red': 12,
    'green': 13,
    'blue': 14
}


#======================== Puzzle1 =======================================
def solution_1(text: str):
    return sum(
        int(re.findall(r'\d+', line.split(':')[0])[0])
        for line in text.split('\n')
        if check_if_is_valid_game('green', line.split(':')[1], rules['green'])
        and check_if_is_valid_game('red', line.split(':')[1], rules['red'])
        and check_if_is_valid_game('blue', line.split(':')[1], rules['blue'])
    )

def check_if_is_valid_game(color: str, txt: str, max_value: int):
    return all(int(match) <= max_value for match in re.findall(r'(\d+) '+color, txt))


#======================== Puzzle2 =======================================

def solution_2(text: str):
    return sum(
        fewest_number_cubes_by_color('red', line)
        * fewest_number_cubes_by_color('green', line)
        * fewest_number_cubes_by_color('blue', line)
        for line in text.split('\n')
    )

def fewest_number_cubes_by_color(color: str, txt: str):
    return max(int(match) for match in re.findall(r'(\d+) '+color, txt))


#=====================================================================
#======================== MAIN =======================================
#=====================================================================

text = open("./Day2/puzzle-day-2.txt").read()

print(solution_1(text))
print(solution_2(text))

