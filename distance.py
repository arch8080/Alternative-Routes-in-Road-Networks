import networkx as nx
import osmnx as ox
from osmnx import distance
import random
import matplotlib.pyplot as plt


# Function to add random travel times to the edges
def add_random_traffic(G):
    for u, v, data in G.edges(data=True):
        data['travel_time'] = random.randint(1, 10)
    return G


# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(G, source, target):
    return nx.shortest_path(G, source, target, weight='travel_time')


# Function to avoid collisions by dynamically adjusting vehicle paths
def avoid_collisions(paths):
    vehicle_positions = {}
    for path in paths:
        for i, node in enumerate(path):
            if node in vehicle_positions:
                vehicle_positions[node].append((i, path))
            else:
                vehicle_positions[node] = [(i, path)]

    for position, times in vehicle_positions.items():
        if len(times) > 1:
            for i in range(1, len(times)):
                times[i][1].insert(times[i][0], None)

    return paths


# Main function
def main():
    # Download and plot the street network of Mumbai
    place = "Mumbai, India"
    G = ox.graph_from_place(place, network_type='drive')
    G = G.to_undirected()

    # Add random traffic to the edges
    G = add_random_traffic(G)

    # Define source and destination places
    orig_place = "Thane West,Mumbai"
    dest_place = "Chhatrapati Shivaji Maharaj International Airport,Mumbai"

    try:
        # Geocode the places to get the coordinates
        orig_point = ox.geocode(orig_place)
        dest_point = ox.geocode(dest_place)
    except Exception as e:
        print(f"Error geocoding place: {e}")
        return

    # Find the nearest nodes to the geocoded coordinates
    orig_node = distance.nearest_nodes(G, X=orig_point[1], Y=orig_point[0])
    dest_node = distance.nearest_nodes(G, X=dest_point[1], Y=dest_point[0])

    # Find the shortest path
    shortest_route = dijkstra(G, orig_node, dest_node)
    print("Shortest route nodes:", shortest_route)

    # Plot the shortest path
    fig, ax = ox.plot_graph_route(G, shortest_route)
    plt.show()

    # Simulate multiple vehicles and avoid collisions
    paths = [shortest_route]
    paths = avoid_collisions(paths)
    print("Paths after avoiding collisions:", paths)


if __name__ == "__main__":
    main()
