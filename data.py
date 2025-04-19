# Product stock at each center
centers = {
    "C1": ["A", "B", "C"],
    "C2": ["D", "E", "F"],
    "C3": ["G", "H", "I"]
}

# Distance between centers and L1
distances = {
    ("C1", "L1"): 10,
    ("C2", "L1"): 20,
    ("C3", "L1"): 30,
    ("C1", "C2"): 15,
    ("C2", "C3"): 25,
    ("C1", "C3"): 35
}

cost_per_km = 2
