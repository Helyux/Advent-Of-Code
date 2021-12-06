__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "06.12.2021"
__email__ = "m@hler.eu"

from collections import defaultdict


def find_overlaps(x1, y1, x2, y2, mode="hv"):

    print(f"\n{x1}x{y1} / {x2}x{y2}")

    if x1 == x2:
        # Horizontal
        for i in range(0, len(range(min(y1, y2), max(y1, y2) + 1))):
            # print((i, y1))
            if y2 > y1:
                hv_overlaps[(x1, y1+i)] += 1
                if mode == "hvd":
                    hvd_overlaps[(x1, y1+i)] += 1
                print(f"H: {(x1, y1+i)}")
            else:
                hv_overlaps[(x1, y1-i)] += 1
                if mode == "hvd":
                    hvd_overlaps[(x1, y1-i)] += 1
                print(f"H: {(x1, y1-i)}")

    if y1 == y2:
        # Vertical
        for i in range(0, len(range(min(x1, x2), max(x1, x2) + 1))):
            # print((i, y1))
            if x2 > x1:
                hv_overlaps[(x1 + i, y1)] += 1
                if mode == "hvd":
                    hvd_overlaps[(x1 + i, y1)] += 1
                print(f"V: {(x1 + i, y1)}")
            else:
                hv_overlaps[(x1 - i, y1)] += 1
                if mode == "hvd":
                    hvd_overlaps[(x1 - i, y1)] += 1
                print(f"V: {(x1 - i, y1)}")

    if not (x1 == x2 or y1 == y2):
        if mode == "hvd":
            for i in range(0, len(range(min(x1, x2), max(x1, x2) + 1))):
                if x2 > x1:
                    hvd_overlaps[((x1 + i), abs(y1 - i))] += 1
                    print(f"D: {(x1 + i), abs(y1 - i)}")
                else:
                    hvd_overlaps[(abs(x1 - i), abs(y1 - i))] += 1
                    print(f"D:  {abs(x1 - i), abs(y1 - i)}")


def get_clean_input():
    with open("inputs/05.txt", "r") as infile:
        line_list = [[[int(num) for num in pair.split(",")] for pair in val.split(" -> ")]
                     for val in infile.read().splitlines()]

    return line_list


def first_challenge(line_list):
    """ Horizontal and vertical overlaps """

    global hv_overlaps
    hv_overlaps = defaultdict(int)

    for pair in line_list:
        find_overlaps(pair[0][0], pair[0][1], pair[1][0], pair[1][1], mode="hv")

    answer = sum(overlap > 1 for overlap in hv_overlaps.values())

    return answer


def second_challenge(line_list):
    """ Horizontal, vertical and diagonal overlaps """

    global hvd_overlaps
    hvd_overlaps = defaultdict(int)

    for pair in line_list:
        find_overlaps(pair[0][0], pair[0][1], pair[1][0], pair[1][1], mode="hvd")

    answer = sum(overlap > 1 for overlap in hvd_overlaps.values())

    return answer


def main():

    line_list = get_clean_input()
    print(f"First challenge answer: {first_challenge(line_list)}")
    print(f"Second challenge answer: {second_challenge(line_list)}")


if __name__ == '__main__':
    main()
