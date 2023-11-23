from main import *

sizex, sizey = map(int, input().split(" "))
field = create_field(sizex, sizey)
fill_field(field)
run(field)
