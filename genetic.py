import random
import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def route_distance(route):
    return sum(calculate_distance(route[i], route[i+1]) for i in range(len(route)-1)) + calculate_distance(route[-1], route[0])

def crossover(parent1, parent2):
    child = [-1] * len(parent1)
    if len(parent1) <= 3: 
        return parent1[:]

    start = random.randint(1, len(parent1) - 3)
    end = random.randint(start + 1, len(parent1) - 2)
    child[start:end+1] = parent1[start:end+1]

    p2_candidates = [gene for gene in parent2 if gene not in child]
    p2_idx = 0
    for i in range(len(child)):
        if child[i] == -1:
            child[i] = p2_candidates[p2_idx]
            p2_idx += 1
    return child

def mutate(route, mutation_rate):
    for i in range(1, len(route)-1):
        if random.random() < mutation_rate:
            swap_idx = random.randint(1, len(route)-2)
            route[i], route[swap_idx] = route[swap_idx], route[i]
    return route

def genetic_algorithm(points, pop_size=100, generations=1000, mutation_rate=0.01):
    points = [(0,0)] + points
    population = [random.sample(points[1:], len(points)-1) for _ in range(pop_size)]
    population = [[(0,0)] + route + [(0,0)] for route in population]

    for gen in range(generations):
        population = sorted(population, key=lambda x: route_distance(x))
        new_population = population[:pop_size//2] 

        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(new_population[:50], 2)
            child = crossover(parent1, parent2)
            new_population.append(child)

        population = [mutate(route, mutation_rate) for route in new_population]

    best_route = population[0]
    return best_route, route_distance(best_route)

def main():
    n = int(input("Enter number of points to visit (excluding station): "))
    points = [tuple(map(float, input(f"Enter coordinates for point {i+1} (x y): ").split())) for i in range(n)]
    route, total_distance = genetic_algorithm(points)
    print("Optimal route:", route)
    print(f"Total distance: {total_distance}")

if __name__ == "main":
    main()