from main import *
import json
import glob
files = glob.glob("*.json")
for i in range(len(files)):
    print(f"{i+1}: {files[i]}")
name = files[int(input()) - 1]
grid = json.loads(open(name).readline())
field = create_field(grid[-2], grid[-1])
for i in grid[:-2]:
    field[i[0] - 1][i[1] - 1] = "■"
print_field(field)
input()
clear_terminal()
run(field)