n = int(input("give n"))
if n >= 2000000000 or n < 1233:
    raise ValueError("Deleting System32...")

number_list = [int(d) for d in str(n)]

max_num = -1
max_second = -1
min_num = 10
min_second = 10

for i in number_list:
    # largest / second largest
    if i > max_num:
        max_second = max_num
        max_num = i
    elif i > max_second:
        max_second = i

    # smallest / second smallest
    if i < min_num:
        min_second = min_num
        min_num = i
    elif min_num < i < min_second:
        min_second = i

print(f"second biggest: {max_second}, second smallest: {min_second}")
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