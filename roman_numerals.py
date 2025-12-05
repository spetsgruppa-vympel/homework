number = input('give roman numba GIVE UPPERCASE')
number_list = list(str(number))
total_sum = 0

class numerals:
    def __init__(self, arab, roman):
        self.arab = arab
        self.roman = roman

numerals_list = [  # sorted like this intentionally
    numerals(40, "XL"),
    numerals(9, "IX"),
    numerals(4, "IV"),
    numerals(90, "XC"),
    numerals(900, "CM"),
    numerals(400, "CD"),
    numerals(1, "I"),
    numerals(5, "V"),
    numerals(10, "X"),
    numerals(50, "L"),
    numerals(100, "C"),
    numerals(500, "D"),
    numerals(1000, "M")
]

i = 0

while i < len(number):
    matched = False
    for numeral in numerals_list:
        length = len(numeral.roman)
        # check if the next substring matches the Roman numeral
        if number[i:i+length] == numeral.roman:
            total_sum += numeral.arab
            i += length  # move forward by the length of the matched numeral
            matched = True
            break  # break the inner loop=
    if not matched:
        # Invalid numeral detected
        print("Deleting system32. . .")
        raise ValueError

print("total value:", total_sum)

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
# i main japan aviation in war thunder