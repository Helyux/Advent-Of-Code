__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "04.12.2021"
__email__ = "m@hler.eu"


def first_challenge(binary_list):
    gamma_rate = []
    epsilon_rate = []

    # Check every position individually
    for pos in range(0, len(binary_list[0])):
        zerobits = 0
        bits = 0

        # Check most common on position 'pos'
        for binary in binary_list:
            if binary[pos] == "0":
                zerobits += 1
            else:
                bits += 1

        if zerobits > bits:
            gamma_rate.append("0")
            epsilon_rate.append("1")
        else:
            gamma_rate.append("1")
            epsilon_rate.append("0")

    # Binary to decimal numbers
    gamma = int("".join(gamma_rate), 2)
    epsilon = int("".join(epsilon_rate), 2)

    answer = gamma * epsilon
    return answer


def second_challenge(binary_list):

    # Check until there is only the most common binary left
    oxygen_rating = binary_list
    while len(oxygen_rating) > 1:
        # Check every position individually
        for pos in range(0, len(binary_list[0])):
            zerobits = 0
            bits = 0

            # Check most common on position 'pos'
            for binary in oxygen_rating:
                if binary[pos] == "0":
                    zerobits += 1
                else:
                    bits += 1

            print(f"pos [{str(pos+1):>2}] | n0: [{str(zerobits):>4s}] | n1: [{str(bits):>4s}]", end=" -> ")

            if zerobits > bits:
                print("Keeping 0-bit entrys for this pos")
                oxygen_rating = [x for x in oxygen_rating if x[pos] != "1"]
            else:
                print("Keeping 1-bit entrys for this pos")
                oxygen_rating = [x for x in oxygen_rating if x[pos] != "0"]

    x = 0
    print(x)

    # Check until there is only the least common binary left
    scrubber_rating = binary_list
    while len(scrubber_rating) > 1:
        # Check every position individually
        for pos in range(0, len(binary_list[0])):
            zerobits = 0
            bits = 0

            # Check least common on position 'pos'
            for binary in scrubber_rating:
                if binary[pos] == "0":
                    zerobits += 1
                else:
                    bits += 1

            print(f"pos [{str(pos + 1):>2s}] | n0: [{str(zerobits):>4s}] | n1: [{str(bits):>4s}]", end=" -> ")

            if bits > zerobits:
                print("Keeping 0-bit entrys for this pos")
                scrubber_rating = [x for x in scrubber_rating if x[pos] != "1"]
            else:
                print("Keeping 1-bit entrys for this pos")
                scrubber_rating = [x for x in scrubber_rating if x[pos] != "0"]

    # Binary to decimal numbers
    oxygen = int("".join(oxygen_rating), 2)
    scrubber = int("".join(scrubber_rating), 2)

    answer = oxygen * scrubber
    return answer


def main():

    with open("inputs/03.txt", "r") as infile:
        binary_list = infile.read().splitlines()

        print(f"First challenge answer: {first_challenge(binary_list)}")
        print(f"Second challenge answer: {second_challenge(binary_list)}")


if __name__ == '__main__':
    main()
