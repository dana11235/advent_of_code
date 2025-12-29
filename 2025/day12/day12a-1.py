import copy

PRESENTS = {}
VARIANTS = {}
BOXES = []
present_id = None
present_content = []


def get_board(width, length):
    row = ["." for num in range(width)]
    return [row[:] for num in range(length)]


def get_flips(board):
    height = len(board)
    width = len(board[0])

    # flip horizontally
    horizontal = []
    vertical = []
    both = []
    for i in range(height):
        hor_row = []
        vert_row = []
        both_row = []
        for j in range(width):
            hor_row.append(board[i][width - j - 1])
            vert_row.append(board[height - i - 1][j])
            both_row.append(board[height - i - 1][width - j - 1])
        horizontal.append(hor_row)
        vertical.append(vert_row)
        both.append(both_row)

    return [board, horizontal, vertical, both]


def get_variants(present):
    variants = []
    variants.append(["".join(row) for row in copy.deepcopy(present)])
    # get rotations
    for _ in range(3):
        variant = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(variants[-1][2 - j][i])
            variant.append("".join(row))
        variants.append(variant)

    # get flips
    for orig in range(4):
        mirror = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(variants[orig][i][2 - j])
            mirror.append("".join(row))
        variants.append(mirror)

    deduped_variants = [
        ded_var.split("|")
        for ded_var in list(set(["|".join(variant) for variant in variants]))
    ]

    return deduped_variants


with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            PRESENTS[present_id] = present_content
            present_id = None
        elif ":" in line and "x" not in line:
            present_id = int(line.split(":")[0])
            present_content = []
        elif ":" in line and "x" in line:
            size, contents = [item.strip() for item in line.split(":")]
            width, length = [int(dim) for dim in size.split("x")]
            print(contents)
            BOXES.append(
                {
                    "length": length,
                    "width": width,
                    "contents": [int(content) for content in contents.split(" ")],
                }
            )
        else:
            present_content.append(list(line))

# print(PRESENTS)
# print(BOXES)


def display(item):
    for line in item:
        print("".join(line))


USED_BOARDS = None


# Adds the variant to a copy of the board, unless there is a conflict
def add_to_board(board, variant, start_y, start_x):
    new_board = copy.deepcopy(board)
    for y in range(3):
        for x in range(3):
            if variant[y][x] == "#" and board[start_y + y][start_x + x] == "#":
                return None
            elif variant[y][x] == "#":
                new_board[start_y + y][start_x + x] = "#"

    for flip in get_flips(new_board):
        if str(flip) in USED_BOARDS:
            return None
    USED_BOARDS[str(new_board)] = True

    return new_board


def is_match(board, contents):
    if sum(contents) == 0:
        print("matched")
        display(board)
        print("--------")
        return True
    for index, val in enumerate(contents):
        if val > 0:
            new_contents = copy.deepcopy(contents)
            new_contents[index] = val - 1
            for start_y in range(len(board) - 2):
                for start_x in range(len(board[0]) - 2):
                    for variant in VARIANTS[index]:
                        new_board = add_to_board(board, variant, start_y, start_x)
                        if new_board:
                            if is_match(new_board, new_contents):
                                return True
    return False


# Generate all of the variants for each present
for index, present in PRESENTS.items():
    VARIANTS[index] = get_variants(present)

fit = 0
for box in BOXES:
    USED_BOARDS = {}
    board = get_board(box["width"], box["length"])
    if is_match(board, box["contents"]):
        fit += 1
    else:
        print("no match")

print("fit", fit)
