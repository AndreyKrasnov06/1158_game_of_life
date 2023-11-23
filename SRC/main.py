import sys
import copy
from time import sleep
import os

TPS = 20


def clear_terminal():
    if sys.platform.startswith('win'):
        os.system("cls")
    elif sys.platform.startswith('linux'):
        os.system("clear")
    elif sys.platform.startswith('darwin'):
        os.system("clear")
    else:
        print("Вася чё за аппарат?!\n\r")


def create_field(width, height):
    field = [["□" for j in range(width)] for i in range(height)]
    return field


def print_field(field):
    for i in field:
        print(" ".join((i)))


def fill_field(field):
    clear_terminal()
    print_field(field)
    while (coords := input()) != "0":
        j, i = map(lambda x: int(x) - 1, coords.split(" "))
        if field[i][j] == "■":
            field[i][j] = "□"
        else:
            field[i][j] = "■"
        clear_terminal()
        print_field(field)
    return field


def check_cell(field, i, j):
    if field[i][j] == "■":
        return True
    return False


def count_neighbors(field, i, j):
    neighbors = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == dj == 0 or not (-1 < i + di < len(field) and -1 < j + dj < len(field[0])):
                continue
            if field[i + di][j + dj] == "■":
                neighbors += 1
    return neighbors


def tick(field):
    next_field = copy.deepcopy(field)
    global TPS
    for i in range(len(field)):
        for j in range(len(field[0])):
            alive = check_cell(field, i, j)
            neigbors = count_neighbors(field, i, j)
            if not alive:
                if neigbors == 3:
                    next_field[i][j] = "■"
            elif neigbors < 2 or neigbors > 3:
                next_field[i][j] = "□"
    return next_field


def run(field):
    clear_terminal()
    while True:
        print_field(field)
        sleep(1 / TPS)
        next_field = tick(field)
        if field == next_field:
            break
        clear_terminal()
        field = next_field
    input()
