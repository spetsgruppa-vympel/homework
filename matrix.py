import noise

scale = 0.1  # scale for perlin noise (smaller = smoother clusters)
threshold = 0.4  # base threshold for perlin noise
lines = int(input("how amny lines"))
columns = int(input("how amny colunms"))

if columns < 1 or columns > 100 or lines < 1 or lines > 100:
    raise IndexError("Deleting System32. . .")

photo = [[0 for _ in range(columns)] for _ in range(lines)]  # generate photo matrix

# pick center cell
center_row = lines // 2
center_col = columns // 2

for row in range(lines):
    for col in range(columns):
        # distance from the original cell
        distance_row = row - center_row
        distance_col = col - center_col

        # generate noise at scaled distance
        n = noise.pnoise2(distance_row * scale, distance_col * scale)

        # reduce likelihood further from center
        rel_distance = (abs(distance_row)/lines + abs(distance_col)/columns)
        distance_factor = rel_distance * 1.1
        cell_threshold = threshold - distance_factor  # threshold per cell

        # Assign 1 or 0
        if n > cell_threshold:
            photo[row][col] = 0
        else:
            photo[row][col] = 1

photo = [row for row in photo if sum(row) > 0]
photo = list(zip(*photo)) # transpose
photo = [col for col in photo if sum(col) > 0]  # remove empty columns
photo = [list(row) for row in zip(*photo)]  # transpose back and convert to lists

# print final matrix
for row in photo:
    print(row)

# i want to make this into a class so bad but im too lazy to make this into a class
# i want to make this into a class so bad but im too lazy to make this into a class
# i want to make this into a class so bad but im too lazy to make this into a class
# i want to make this into a class so bad but im too lazy to make this into a class
# i want to make this into a class so bad but im too lazy to make this into a class
# i want to make this into a class so bad but im too lazy to make this into a class
# i want to make this into a class so bad but im too lazy to make this into a class
# i want to make this into a class so bad but im too lazy to make this into a class
# i want to make this into a class so bad but im too lazy to make this into a class
# i want to make this into a class so bad but im too lazy to make this into a class