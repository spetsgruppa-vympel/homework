import random


class Cell:
    def __init__(self, x, y, value, occupied=False):
        self.value = value
        self.x = x
        self.y = y
        self.occupied = occupied
        # i know this is not necessary

    def __str__(self):
        return 'x' if self.occupied else '0'

n = int(input("number of row"))
m = int(input("number of columns"))

# posture check

l = int(input("rows of whatever it is you are storing wahtthe heck is a \"drezina\" bro speak romanian/english plz help im being held at gunpoint by chinese pump&dumpersBigPhish Pha Ze Khan BigPhish ART OF CHOKE BigPhish J Kovv BigPhish Tu Vistzz BigPhish Brao Kih BigPhish Ki Riy Gaon BigPhish Frao Zin BigPhish NEO BigPhish "))
c = int(input("columnsz of whatever it is you are storing wahtthe heck is a \"drezina\" bro speak romanian/english plz help im being held at gunpoint by chinese pump&dumpersBigPhish Pha Ze Khan BigPhish ART OF CHOKE BigPhish J Kovv BigPhish Tu Vistzz BigPhish Brao Kih BigPhish Ki Riy Gaon BigPhish Frao Zin BigPhish NEO BigPhish "))

# create matrix
matrix = []
for i in range(n):
    row = [Cell(i, j, random.randint(0, 9)) for j in range(m)]
    matrix.append(row)

for row in matrix:
    print(' '.join(str(cell) for cell in row))
try:
    sum = 0
    for row in matrix:
        for cell in row:
            if cell.x < l and cell.y < c:
                cell.occupied = True
                sum += cell.value
except IndexError:
    print("no")
else:
    print(sum)

for row in matrix:
    print(' '.join('x' if cell.occupied else '0' for cell in row))


# they even pumped the ak safari mesh...
# someone needs to stop them
# the cs2 market will crash
# we will lose all of our investments
# NOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# MY RUBY WENT DOWN 20%
# i can only buy 54 houses instead of 67 with it now!
# (=^･ω･^=)(=^･ω･^=)(=^･ω･^=)(=^･ω･^=)(=^･ω･^=)
# ⣟⢿⣟⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣒⣒⣂⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀
# ⠻⣄⠹⣯⡀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⢀⡦
# ⠀⠘⢦⡈⠻⢶⡶⠶⠶⠶⠶⠶⣦⡄⠀⠀⢰⡶⠶⠶⠶⠶⠤⠤⠶⠋⢀⡴⠏⠀
# ⠀⠀⠀⠙⢦⡘⢿⣟⠛⠛⠛⠛⠛⠁⠀⠀⢸⡇⣶⣶⣶⣶⣶⣶⣶⡚⠁⠀⠀⠀
# ⠀⠀⠀⠀⠀⠹⣆⠻⣷⣄⣀⣀⣀⠀⠀⠀⢸⡇⠘⠻⠟⠗⠒⠒⠲⠶⠶⠶⣷⠆
# ⠀⠀⠀⠀⠀⠀⠈⠳⣌⣉⣉⣉⣻⡇⠀⠀⠈⢻⠏⠉⠉⠉⠉⣹⣿⠟⣠⡾⠋⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡟⢹⡇⠀⠀⠀⠀⢀⣀⣀⣠⣾⠟⣡⡶⠋⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⣠⠞⠋⣭⣭⣭⣥⠞⠋⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⣇⣤⠞⢁⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠼⠏⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣴⠟⠁⠀⠀⠀⠀⠀
# ⠀⠀⠀
# BigPhish Pha Ze Khan BigPhish ART OF CHOKE BigPhish J Kovv BigPhish Tu Vistzz
# BigPhish Brao Kih BigPhish  Ki Riy Gaon BigPhish Frao Zin BigPhish NEO BigPhish