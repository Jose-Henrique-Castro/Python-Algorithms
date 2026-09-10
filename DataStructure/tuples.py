
grid_points = []

for i in range(3):
    x = input("X coordination: ")
    y = input("Y coordination: ")

    grid_points.append((x,y))

    count = 1


for point in grid_points:
    x , y = point

    print(f"Coordenation[{count}]: {x},{y}")
    count += 1