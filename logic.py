from data import centers, distances, cost_per_km
from itertools import permutations, product
import math

def get_product_centers():
    product_sources = {}
    for center, items in centers.items():
        for item in items:
            product_sources.setdefault(item, []).append(center)
    return product_sources

def get_distance(a, b):
    return distances.get((a, b)) or distances.get((b, a)) or 0

def generate_plans(order, product_sources):
    options = []
    for item, qty in order.items():
        if qty == 0 or item not in product_sources:
            continue
        sources = product_sources[item]
        options.append([(item, source) for source in sources])
    return list(product(*options))

def route_cost(start_center, plan):
    steps = []
    visited = set()
    inventory = {}
    for item, center in plan:
        inventory.setdefault(center, []).append(item)
        visited.add(center)
    visited.add("L1")
    best_cost = math.inf
    for mid_route in permutations(visited):
        if mid_route[0] != start_center:
            continue
        if "L1" not in mid_route:
            continue
        total = 0
        for i in range(len(mid_route) - 1):
            total += get_distance(mid_route[i], mid_route[i + 1])
        best_cost = min(best_cost, total)
    return best_cost * cost_per_km

def calculate_minimum_cost(order):
    product_sources = get_product_centers()
    all_plans = generate_plans(order, product_sources)
    best = math.inf
    for plan in all_plans:
        centers_in_plan = set(center for _, center in plan)
        for start in centers_in_plan:
            cost = route_cost(start, plan)
            best = min(best, cost)
    return best if best != math.inf else 0
