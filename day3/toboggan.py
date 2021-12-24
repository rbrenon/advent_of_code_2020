
def main():
    with open("input.txt") as f:
        slopes = f.read().split('\n')

    total_trees = 1
    for right in [1, 3, 5, 7]:
        tree = 0
        for index, row in enumerate(slopes):
            space = row[(index * right) % len(row)]
            if space == '#':
                tree += 1
        total_trees *= tree
        print(index, row, space, (index * 3) % len(row), tree, total_trees)

    tree = 0
    for index, row in enumerate(slopes):
        if index > 0 and index % 2 == 0:
            element = (index//2) % len(row)
            space = row[element]
            if space == '#':
                tree += 1

    total_trees *= tree
    print(index, row, space, index % len(row), tree, total_trees)


if __name__ == "__main__":
    main()

# 2632611840 - too low
# 3510149120