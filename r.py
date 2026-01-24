# task 1
#
#
# input_string = sorted(input("string"))
# exit_string = ""
# previous_element = input_string[0]
#
#
# for i in input_string:
#     if i != previous_element:
#         count = input_string.count(i)
#         exit_string += i * count
#         previous_element = i
#
# print(exit_string
# task 2

# number_list = []
# userinput = ""
# print("give me numbers and say \"u got enuff numbas little bro\" when ur done")
# while userinput != "u got enuff numbas little bro":
#     userinput = input("give me a numba: ")
#     if userinput.isdigit():
#         number_list.append(int(userinput))
#
# k = int(input("give me a number: "))
# r_list = number_list[k:] + number_list[:k]
# print(r_list)

# task 3

# class Cell:  # this is copy paste from homework lmao
#     def __init__(self, x, y, occupied=False):
#         self.x = x
#         self.y = y
#         self.occupied = occupied
#         # i know this is not necessary
#
#     def __str__(self):
#         return 'x' if self.occupied else '0'
#
# n = 5 #int(input("number of row"))
# m = 5 #int(input("number of columns"))
#
# c = int(input("x"))
# l = int(input("y"))
#
# matrix = []
# for i in range(n):
#     row = [Cell(i, j) for j in range(m)]
#     matrix.append(row)
#
# for row in matrix:
#     for cell in row:
#         if l > cell.x > l - 3 and c > cell.y > c - 3:
#             cell.occupied = True
#
#
# for row in matrix:
#     print(' '.join('x' if cell.occupied else '0' for cell in row))

# i love classes :heart_eyes: classes are so versatile :heart_eyes: I LOVE CLASSES

# task 4

# task 5

# number_list = []
# userinput = ""
# print("give me numbers and say \"u got enuff numbas little bro\" when ur done")
# while userinput != "u got enuff numbas little bro":
#     userinput = input("give me a numba: ")
#     if userinput.isdigit() and userinput not in number_list:
#          number_list.append(int(userinput))
#          number_list.append(int(userinput))
#
# userinput = input("give me a number you DIDN'T put")
# if userinput.isdigit() and userinput not in number_list:
#     number_list.append(int(userinput))
# else:
#     raise ValueError("restart the program :shrug")
# #i = 0
# # while i < len(number_list):
# #     if number_list.count(number_list[i]) >= 2:
# #         number_list.remove(number_list[i])
# #     i+=1
# #
# # print(number_list[0])
# # why use xor when snake already has everything you need lol imagine actually making your own code that would be dumb...
# r = 0
# for element in number_list:
#     r ^= element
#
# print(r)

# task 6

# k = int(input("Enter a number: "))
# number_list = []
# userinput = ""
# indexes = []
# yes = False
# print("give me numbers and say \"u got enuff numbas little bro\" when ur done")
# while userinput != "u got enuff numbas little bro":
#      userinput = input("give me a numba: ")
#      if userinput.isdigit() and userinput not in number_list:
#           number_list.append(int(userinput))
#
#
# def find(a):
#     global indexes
#     indexes = [i for i, x in enumerate(number_list) if x == a]
#
# i = 0
# while i < len(number_list) and not yes:
#     thing = number_list[i]
#     find(thing)
#     for j in indexes:
#         if j == abs(thing - k):
#             yes = True
#             break
#     i = i + 1
#
# print(yes)

# task 7

# start1 = int(input("Enter the first number: "))
# end1 = int(input("Enter the second number: "))
# start2 = int(input("Enter the first number: "))
# end2 = int(input("Enter the second number: "))
# if start1 > end1:
#     start1, end1 = end1, start1
#
# elif start2 > end2:
#     start2, end2 = end2, start2
#
# if start1 < end2 and end1 > start2:
#     print("yes")
# else:
#     print("no")


# # task 8
# num = int(input("Enter the number: "))
# sum = 0
# def do_things(n):
#     if n > 0:
#         global sum
#         sum += n % 10
#         n = n // 10
#         do_things(n)
#
# do_things(num)
# print(sum)
# print(sum)

# task 9

# im not writing a whole input system for a tup so this is going untested

data = [()]
scores = []
for name, score in data:
    found = False
    for i in range(len(scores)):
        if scores[i][0] == name:
            scores[i] = (name, scores[i][1] + score)
            found = True
            break
    if not found:
        scores.append((name, score))