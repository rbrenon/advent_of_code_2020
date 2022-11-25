from pprint import pprint


def main():
    with open("input.txt") as file:
        instructions: list[str] = file.read().splitlines()

    print(f"Part one answer is: {part_one(instructions)}")

    starting_waypoint = {
        'x': 10,
        'y': 1
    }
    print(f"Part two answer is: {part_two(instructions, starting_waypoint)}")


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
    ferry_coord = {
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
            # increase y axis of ferry
            ferry_coord['y'] += int(action[1:])
        elif action[0] == 'E' or (action[0] == 'F' and direction == 'E'):
            # increase x axis of ferry
            ferry_coord['x'] += int(action[1:])
        elif action[0] == 'S' or (action[0] == 'F' and direction == 'S'):
            # decrease y axis of ferry
            ferry_coord['y'] -= int(action[1:])
        elif action[0] == 'W' or (action[0] == 'F' and direction == 'W'):
            # decrease x axis of ferry
            ferry_coord['x'] -= int(action[1:])

    # calculate distance to 0,0
    manhattan_distance: int = abs(ferry_coord['x']) + abs(ferry_coord['y'])     # 364

    return manhattan_distance


def part_two(instructions: list[str], waypoint: dict[str:int], starting_direction: str = 'E') -> int:
    """
    Almost all the actions indicate how to move a waypoint which is relative to the ship's position:

        Action N means to move the waypoint north by the given value.
        Action S means to move the waypoint south by the given value.
        Action E means to move the waypoint east by the given value.
        Action W means to move the waypoint west by the given value.
        Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
        Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
        Action F means to move forward to the waypoint a number of times equal to the given value.
        The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship;
        if the ship moves, the waypoint moves with it.

    :param starting_direction:
    :param instructions:
    :param waypoint:
    :return:
    """
    direction: str = starting_direction
    ferry_coord = {
        'x': 0,
        'y': 0
    }

    for action in instructions:
        if action[0] == 'F':
            # move to the waypoint x times
            ferry_coord['x'] += (waypoint['x'] * int(action[1:]))
            ferry_coord['y'] += (waypoint['y'] * int(action[1:]))

        elif action[0] == 'R':
            # waypoint (2,1) rotated 90 = (1,-2)
            # x,y = -y,x for each 90 clockwise rotation
            rotations = int(action[1:]) // 90
            for rotation in range(rotations):   # apply 1x 90-degree clockwise rotation
                waypoint['x'], waypoint['y'] = waypoint['y'] , (waypoint['x'] * -1)
        elif action[0] == 'L':
            # x,y = y,-x for each 90 counter-clockwise rotation
            rotations = int(action[1:]) // 90
            for rotation in range(rotations):   # apply 1x 90-degree counter-clockwise rotation
                waypoint['x'], waypoint['y'] = (waypoint['y'] * -1), waypoint['x']
        elif action[0] == 'N':
            # increase y axis value of waypoint
            waypoint['y'] += int(action[1:])
        elif action[0] == 'E':
            # increase x axis value of waypoint
            waypoint['x'] += int(action[1:])
        elif action[0] == 'S':
            # decrease y axis value of waypoint
            waypoint['y'] -= int(action[1:])
        elif action[0] == 'W':
            # decrease x axis value of waypoint
            waypoint['x'] -= int(action[1:])

    manhattan_distance: int = abs(ferry_coord['x']) + abs(ferry_coord['y'])  # 39518, too low: 1991, 37792

    return manhattan_distance


if __name__ == "__main__":
    main()
