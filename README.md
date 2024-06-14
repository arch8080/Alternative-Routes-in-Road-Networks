# Alternative-Routes-in-Road-Networks
The code is a Python implementation of a traffic simulation system using graph theory and Dijkstra's algorithm. 

The code uses the networkx and osmnx libraries to create a graph representation of a road network in Mumbai, India. It then adds random travel times to the edges of the graph to simulate traffic conditions.

The dijkstra function implements Dijkstra's algorithm to find the shortest path between two nodes in the graph, taking into account the current traffic conditions.

The avoid_collisions function simulates dynamic speed adjustments to avoid collisions between vehicles by inserting None values into the paths at conflicting nodes.

The main function downloads and plots the street network of Mumbai, adds random traffic to the edges, finds the shortest path between two nodes, plots the shortest path, and simulates multiple vehicles and avoids collisions.
