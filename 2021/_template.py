__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "XX.12.2021"
__email__ = "m@hler.eu"


def get_clean_input():
    with open("inputs/XX.txt", "r") as infile:
        x_list = [int(val) for val in infile.read().splitlines()]

    return x_list


def first_challenge(x_list):


    return answer


def second_challenge(x_list):


    return answer


def main():

    x_list = get_clean_input()
    print(f"First challenge answer: {first_challenge(x_list)}")
    print(f"Second challenge answer: {second_challenge(x_list)}")


if __name__ == '__main__':
    main()
