__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "04.12.2023"
__email__ = "m@hler.eu"


def get_clean_input():

    with open("inputs/03.txt", "r") as f:
        inputs = [line.strip() for line in f]

    return inputs


def get_symbol_map(inputs):
    symbol_map = {}

    for i, line in enumerate(inputs):

        chars = [char for char in line]
        symbols = [x for x in chars if x != "." and not x.isdigit()]

        idx = 0
        symbol_map[i] = []
        for symbol in symbols:
            idx = line.find(symbol, idx + 1)
            symbol_map[i].append(idx)

    return symbol_map


def get_gear_map(inputs):
    gear_map = {}

    for i, line in enumerate(inputs):

        chars = [char for char in line]
        gears = [x for x in chars if x == "*"]

        idx = 0
        gear_map[i] = []
        for gear in gears:
            idx = line.find(gear, idx + 1)
            gear_map[i].append(idx)

    return gear_map


def first_challenge(inputs):

    answer = 0

    symbol_map = get_symbol_map(inputs)

    for i, line in enumerate(inputs):

        print(line)

        chars = [char for char in line]

        # Get the numbers!
        numbers = []
        number = []
        for char in chars:
            if char.isdigit():
                number.append(char)
            elif number:
                numbers.append(''.join(number))
                number.clear()
        if number:
            numbers.append(''.join(number))
            number.clear()

        idx = 0
        for number in numbers:

            is_part_number = False
            num_len = len(str(number))
            idx_begin = line.find(number, idx)
            idx_end = idx_begin + (num_len-1)

            # Find the positions for the number
            front = idx_begin - 1
            back = idx_end + 1
            indexes = [front] + list(range(idx_begin, idx_end+1)) + [back]

            for index in indexes:

                # Check the line before
                if i != 0:
                    if index in symbol_map[i-1]:
                        is_part_number = True
                        break

                # Check same line
                if index in symbol_map[i]:
                    is_part_number = True
                    break

                # Check the next line
                if i + 1 < len(symbol_map):
                    if index in symbol_map[i+1]:
                        is_part_number = True
                        break

            print(f"{number} is {'a part number' if is_part_number else 'no part number'}")
            if is_part_number:
                answer += int(number)

            idx = idx_begin + num_len

    return answer


def second_challenge(inputs):

    answer = 0

    inputs = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    gear_map = get_gear_map(inputs)
    print(gear_map)

    # Using the gear index check if the * is connected to two digits in different locations
    for i, gear_indexes in gear_map.items():
        for gear_index in gear_indexes:

            # Same line
            if inputs[i][gear_index-1].isdigit():
                print("connected same line, before")

            if inputs[i][gear_index+len(str(gear_index))+1].isdigit():
                print("connected same line, after")

    return answer


def main():

    inputs = get_clean_input()

    print(f"\nFirst challenge answer: {first_challenge(inputs)}")
    print(f"Second challenge answer: {second_challenge(inputs)}")


if __name__ == '__main__':
    main()
