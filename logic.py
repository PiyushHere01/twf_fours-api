from data import centers, distances, cost_per_km
from itertools import permutations
import math

def get_product_centers():
    product_sources = {}
    for center, items in centers.items():
        for item in items:
            product_sources.setdefault(item, []).append(center)
    return product_sources

def get_distance(a, b):
    return distances.get((a, b)) or distances.get((b, a)) or 0

def calculate_minimum_cost(order):
    product_sources = get_product_centers()

    product_to_center = {}
    involved_centers = set()

    for product, qty in order.items():
        if qty == 0:
            continue
        if product not in product_sources:
            return -1
        assigned_center = product_sources[product][0]
        product_to_center.setdefault(assigned_center, []).append(product)
        involved_centers.add(assigned_center)

    involved_centers = list(involved_centers)

    best_cost = math.inf

    for start_center in involved_centers:
        route = [start_center]
        visited = set()
        inventory = set()
        total_distance = 0
        remaining_centers = set(involved_centers)

        current = start_center

        if start_center in product_to_center:
            inventory.update(product_to_center[start_center])
        total_distance += get_distance(current, "L1")
        current = "L1"
        total_distance += get_distance(current, start_center)
        current = start_center
        remaining_centers.remove(start_center)

        for center in remaining_centers:
            total_distance += get_distance(current, center)
            current = center
            total_distance += get_distance(current, "L1")
            current = "L1"

        total_cost = total_distance * cost_per_km
        best_cost = min(best_cost, total_cost)

    return best_cost
