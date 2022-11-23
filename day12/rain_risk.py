from pprint import pprint


def main():
    with open("input.txt") as file:
        instructions: list[str] = file.read().splitlines()

    print(f"Part one answer is: {part_one(instructions)}")


def part_one(instructions: list[str], starting_direction: str = 'E') -> int:
    """
    move the ferry according to the instructions

        Action N means to move north by the given value.
        Action S means to move south by the given value.
        Action E means to move east by the given value.
        Action W means to move west by the given value.
        Action L means to turn left the given number of degrees.
        Action R means to turn right the given number of degrees.
        Action F means to move forward by the given value in the direction the ship is currently facing.

    :param starting_direction:
    :param instructions: input in the form of Action (N,S,E,W,L,R,F) and distance or degree
    :return: sum of absolute value from 0,0 to the last ferry location
    """
    direction: str = starting_direction
    fleet_coord = {
        'x': 0,
        'y': 0
    }
    compass = {
        'N': 0,
        'E': 90,
        'S': 180,
        'W': 270
    }

    for action in instructions:
        if action[0] == 'R':
            # turn the ferry right by the number of degrees indicated - eg: R90 steers right 90 degrees
            new_direction = (compass[direction] + int(action[1:])) % 360
            direction = [k for k in compass if compass[k] == new_direction][0]
        elif action[0] == 'L':
            # turn the ferry left by the number of degrees indicated - eg: L90 steers left 90 degrees
            new_direction = (compass[direction] - int(action[1:])) % 360
            direction = [k for k in compass if compass[k] == new_direction][0]

        elif action[0] == 'N' or (action[0] == 'F' and direction == 'N'):
            # increase value of y axis
            fleet_coord['y'] += int(action[1:])
        elif action[0] == 'E' or (action[0] == 'F' and direction == 'E'):
            # increase value of x axis
            fleet_coord['x'] += int(action[1:])
        elif action[0] == 'S' or (action[0] == 'F' and direction == 'S'):
            # decrease value of y axis
            fleet_coord['y'] -= int(action[1:])
        elif action[0] == 'W' or (action[0] == 'F' and direction == 'W'):
            # decrease value of x axis
            fleet_coord['x'] -= int(action[1:])

    manhattan_distance: int = abs(fleet_coord['x']) + abs(fleet_coord['y'])     # 364

    return manhattan_distance


if __name__ == "__main__":
    main()
