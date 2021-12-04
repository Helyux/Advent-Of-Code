__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "04.12.2021"
__email__ = "m@hler.eu"


def first_challenge(move_list):
    depth = 0
    horizontal = 0

    for move in move_list:
        action = move[0]
        step = move[1]

        if action == "forward":
            horizontal += step
        elif action == "down":
            depth += step
        elif action == "up":
            depth -= step

    answer = horizontal * depth
    return answer


def second_challenge(move_list):
    depth = 0
    horizontal = 0
    aim = 0

    for move in move_list:
        action = move[0]
        step = move[1]

        if action == "forward":
            horizontal += step
            depth += (aim * step)
        elif action == "down":
            aim += step
        elif action == "up":
            aim -= step

    answer = horizontal * depth
    return answer


def main():

    with open("inputs/02.txt", "r") as infile:
        lines = infile.read().splitlines()
        move_list = [[move[0], int(move[1])] for move in (line.split(" ") for line in lines)]

        print(f"First challenge answer: {first_challenge(move_list)}")
        print(f"Second challenge answer: {second_challenge(move_list)}")


if __name__ == '__main__':
    main()
