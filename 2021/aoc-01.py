__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "04.12.2021"
__email__ = "m@hler.eu"


def first_challenge(depth_list):
    increases = 0
    last_depth = 0

    for depth in depth_list[1:]:
        if depth > last_depth:
            # print(f"{depth} increased")
            increases += 1
        else:
            # print(f"{depth} not increased")
            pass

        last_depth = depth

    return increases


def second_challenge(depth_list):
    increases = 0
    last_measurement_window_sum = 0

    for n in range(1, len(depth_list)):

        measurement_window = depth_list[n:n+3]
        if len(measurement_window) < 3:
            break
        else:
            measurement_window_sum = sum(measurement_window)
            if measurement_window_sum > last_measurement_window_sum:
                # print(f"{measurement_window} = {str(measurement_window_sum)} increased")
                increases += 1
            else:
                # print(f"{measurement_window} = {str(measurement_window_sum)} not increased")
                pass

            last_measurement_window_sum = measurement_window_sum

    return increases


def main():

    with open("inputs/01.txt", "r") as infile:
        depth_list = [int(val) for val in infile.read().splitlines()]

        print(f"First challenge answer: {first_challenge(depth_list)}")
        print(f"Second challenge answer: {second_challenge(depth_list)}")


if __name__ == '__main__':
    main()
