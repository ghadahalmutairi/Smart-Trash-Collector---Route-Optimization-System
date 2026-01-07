import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def nearest_neighbor_algorithm(points):
    start_point = (0, 0)
    unvisited = points[:]  
    route = [start_point]
    total_distance = 0
    current_point = start_point
    
    while unvisited:
     
        nearest_point = min(unvisited, key=lambda x: calculate_distance(current_point, x))
        route.append(nearest_point)
        total_distance += calculate_distance(current_point, nearest_point)
        current_point = nearest_point
        unvisited.remove(nearest_point)
    

    total_distance += calculate_distance(current_point, start_point)
    route.append(start_point)
    
    return route, total_distance

def main():
    n = int(input("Enter the number of points to visit (excluding the station): "))
    
    points = []
    for i in range(n):
        x, y = map(float, input(f"Enter coordinates for point {i + 1} (x y): ").split())
        points.append((x, y))

    route, total_distance = nearest_neighbor_algorithm(points)

    print("Optimal route:", route)
    print(f"Total distance: {total_distance}")

if __name__ == "__main__":
    main()