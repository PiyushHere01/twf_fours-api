
from data import centers, distances, cost_per_km
from itertools import permutations

def get_product_centers():
    prod_map = {}
    for center, products in centers.items():
        for p in products:
            prod_map.setdefault(p, []).append(center)
    return prod_map

def calculate_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        pair = (path[i], path[i+1])
        if pair not in distances:
            pair = (path[i+1], path[i])  # reverse
        total_distance += distances.get(pair, 0)
    return total_distance

def calculate_minimum_cost(order):
    prod_map = get_product_centers()
    
    # Get all required products and which centers can fulfill them
    required_centers = set()
    for product in order:
        if order[product] > 0 and product in prod_map:
            required_centers.update(prod_map[product])

    min_cost = float('inf')

    # Try all starting points (C1, C2, C3)
    for start_center in centers:
        if start_center not in required_centers:
            continue
        # All permutations of pickup and delivery
        for path in permutations(required_centers):
            if path[0] != start_center:
                continue
            full_path = list(path) + ["L1"]
            total_distance = calculate_distance(full_path)
            total_cost = total_distance * cost_per_km
            min_cost = min(min_cost, total_cost)

    return min_cost if min_cost != float('inf') else 0
