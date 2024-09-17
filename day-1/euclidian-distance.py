import math

# Define the points
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")
