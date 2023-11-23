from main import *
import json
name = input()
grid = json.loads(open(name + ".json").readline())
field = create_field(grid[-2], grid[-1])
for i in grid[:-2]:
    field[i[0] - 1][i[1] - 1] = "■"
print_field(field)
input()
clear_terminal()
run(field)