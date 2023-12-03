__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "03.12.2023"
__email__ = "m@hler.eu"


def get_clean_input():

    with open("inputs/02.txt", "r") as f:
        inputs = [line.strip() for line in f]

    return inputs


def first_challenge(inputs):

    answer = 0
    static_max = {"red": 12, "green": 13, "blue": 14}

    for i, game_line in enumerate(inputs):

        maxes = {"red": 0, "green": 0, "blue": 0}

        game_id = i+1
        game_line = game_line.replace(f"Game {game_id}: ", "")
        subsets = [subset.strip() for subset in game_line.split(";")]
        for subset in subsets:
            cubes = subset.split(",")
            for cube in cubes:
                cube_n, cube_color = cube.split()
                if int(cube_n) > maxes[cube_color]:
                    maxes[cube_color] = int(cube_n)

        # Check if inbound
        valid = True
        for k, v in maxes.items():
            if static_max[k] < v:
                valid = False

        if valid:
            answer += game_id

    return answer


def second_challenge(inputs):

    answer = 0

    for i, game_line in enumerate(inputs):

        maxes = {"red": 0, "green": 0, "blue": 0}

        game_id = i+1
        game_line = game_line.replace(f"Game {game_id}: ", "")
        subsets = [subset.strip() for subset in game_line.split(";")]
        for subset in subsets:
            cubes = subset.split(",")
            for cube in cubes:
                cube_n, cube_color = cube.split()
                if int(cube_n) > maxes[cube_color]:
                    maxes[cube_color] = int(cube_n)

        # Build power of maxes
        power = maxes['red'] * maxes['green'] * maxes['blue']
        answer += power

    return answer


def main():

    inputs = get_clean_input()
    print(f"First challenge answer: {first_challenge(inputs)}")
    print(f"Second challenge answer: {second_challenge(inputs)}")


if __name__ == '__main__':
    main()
