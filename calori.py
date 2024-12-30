from geopy.distance import geodesic

# Fungsi untuk menghitung kalori terbakar
def calculate_calories(distance, weight):
    return distance * 0.063 * weight  # Rumus kalori terbakar

# Fungsi untuk menghitung jarak dengan GPS
def calculate_distance(loc1, loc2):
    return geodesic(loc1, loc2).km
