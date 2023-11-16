import copy
from time import sleep
from os import system

TPS = 10
width, height = int(input()), int(input())


def create_field(width, height):
    field = [["□" for j in range(width)] for i in range(height)]
    return field


def print_field(field):
    for i in field:
        print("  ".join((i)))


def check_cell(field, i, j):
    if field[i][j] == "■":
        return True
    return False


def count_neighbors(field, i, j):
    neighbors = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == dj == 0:
                continue
            try:
                if field[i + di][j + dj] == "■":
                    neighbors += 1
            except:
                pass
    return neighbors


def tick(field):
    next_field = copy.deepcopy(field)
    global TPS
    for i in range(len(field) - 1):
        for j in range(len(field) - 1):
            alive = check_cell(field, i, j)
            neigbors = count_neighbors(field, i, j)
            if not alive:
                if neigbors == 3:
                    next_field[i][j] = "■"
            elif neigbors < 2 or neigbors > 3:
                next_field[i][j] = "□"
    return next_field


field = create_field(10, 10)
field[1] = ["□", "□", "□", "□", "□", "□", "□", "■", "□", "□", ]
field[2] = ["□", "□", "□", "□", "□", "□", "■", "□", "□", "□", ]
field[3] = ["□", "□", "□", "□", "□", "□", "■", "■", "■", "□", ]
while True:
    print_field(field)
    sleep(1)
    system("cls")
    field = tick(field)

