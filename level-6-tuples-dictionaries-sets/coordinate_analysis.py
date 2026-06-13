"""
Problem 2: Coordinate Analysis
------------------------------
Concepts Practiced: Tuple traversal, Finding maximum values

This script stores a series of X, Y coordinate tuples and evaluates 
the collection to find the highest individual X and Y values.

"""



print(f"{'Coordinate Analysis':-^40}")

coordinates = [
    (10,20),
    (15, 25),
    (50, 10)
]

# # method 1: 
# def get_x_coordinate(coord):
#     return coord[0]

# def get_y_coordinate(coord):
#     return coord[1]

# x1 = get_x_coordinate(coordinates[0])
# x2 = get_x_coordinate(coordinates[1])
# x3 = get_x_coordinate(coordinates[2])

# y1 = get_y_coordinate(coordinates[0])
# y2 = get_y_coordinate(coordinates[1])
# y3 = get_y_coordinate(coordinates[2])

# highest_x = max(x1,x2,x3)
# highest_y = max(y1,y2,y3)


# # method 2:
# def get_x_coordinate(coord):
#     return coord[0]

# def get_y_coordinate(coord):
#     return coord[1]

# highest_x_tuple = max(coordinates, key=get_x_coordinate)
# highest_y_tuple = max(coordinates, key=get_y_coordinate)

# highest_x = highest_x_tuple[0]
# highest_y = highest_y_tuple[1]


# method 3: with lambda function
highest_x_tuple = max(coordinates, key=lambda coord: coord[0])
highest_y_tuple = max(coordinates, key=lambda coord: coord[1])

highest_x = highest_x_tuple[0]
highest_y = highest_y_tuple[1]

print("Stored Coordinate: ", coordinates)
print("Highest X coordinate: ", highest_x_tuple)
print("Highest Y coordinate: ", highest_y_tuple)
print("Highest X value: ", highest_x)
print("Highest Y value: ", highest_y)