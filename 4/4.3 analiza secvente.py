import math

number_list = []
helper_list = []
list_list = []
last_element = -math.inf
userinput = ""
maximum_difference = 0

print("give me numbers and say \"u got enuff numbas little bro\" when ur done")
while userinput != "u got enuff numbas little bro":
    userinput = input("give me a numba: ")
    if userinput.isdigit():  # only add real numbers
        number_list.append(int(userinput))

for i in number_list:
    if i > last_element:
        helper_list.append(i)
        last_element = i
    else:
        if helper_list:  # avoid appending empty lists
            list_list.append(helper_list)
        helper_list = [i]  # start new subsequence with current number
        last_element = i


if helper_list:
    list_list.append(helper_list.copy())

last_element = [-math.inf, []] # turn into a list to be able to store last list as well because im too lazy to turn ts into a class
for rlist in list_list:
    # repurpose last_element
    if len(rlist) > last_element[0]:
        last_element = [len(rlist), rlist]

maximum_difference = last_element[1][-1] - last_element[1][0]

print(maximum_difference)
print(last_element[1])

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