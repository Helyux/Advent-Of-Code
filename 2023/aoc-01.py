__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "03.12.2023"
__email__ = "m@hler.eu"


def get_clean_input():

    with open("inputs/01.txt", "r") as f:
        inputs = [line.strip() for line in f]

    return inputs


def first_challenge(inputs):

    answer = 0

    for calibration_line in inputs:
        digits = []

        for char in calibration_line:
            if char.isdigit():
                digits.append(char)

        answer += int(f"{digits[0]}{digits[-1]}")

    return answer


def second_challenge(inputs):

    num_list = [
        "one", "two", "three",
        "four", "five", "six",
        "seven", "eight", "nine"
    ]

    answer = 0

    for calibration_line in inputs:

        digits = []
        for idx, char in enumerate(calibration_line):
            if char.isdigit():
                digits.append(char)

            for char_val, char_key in enumerate(num_list):
                if calibration_line[idx:].startswith(char_key):
                    digits.append(str(char_val+1))

        answer += int(f"{digits[0]}{digits[-1]}")

    return answer


def main():

    inputs = get_clean_input()
    print(f"First challenge answer: {first_challenge(inputs)}")
    print(f"Second challenge answer: {second_challenge(inputs)}")


if __name__ == '__main__':
    main()
