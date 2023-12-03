__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "XX.12.2023"
__email__ = "m@hler.eu"


def get_clean_input():

    with open("inputs/XX.txt", "r") as f:
        inputs = [line.strip() for line in f]

    return inputs


def first_challenge(inputs):

    answer = None

    return answer


def second_challenge(inputs):

    answer = None

    return answer


def main():

    inputs = get_clean_input()
    print(f"First challenge answer: {first_challenge(inputs)}")
    print(f"Second challenge answer: {second_challenge(inputs)}")


if __name__ == '__main__':
    main()
