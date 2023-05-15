import networkx as nx
from digraph import osm_digraph, find_random_origin_destination_pairs, path_finder
from discrete_curve_evolution import dce_with_threshold_percentage


# load OpenStreetMap digraph
osm = 'extracted_hamburg.osm'
dg = osm_digraph(osm)

# find a random origin and destination
od_list = find_random_origin_destination_pairs(dg, 1)
origin, destination = od_list[0]

# find the shortest path between the origin and destination
path = path_finder(dg, origin, destination)

# define the threshold values for discrete curve evolution
thresholds = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

# iterate over the threshold values and compute the DCE path for each one
for threshold in thresholds:
    route_defining_threshold = 1 - threshold
    path_dce_with_od = dce_with_threshold_percentage(dg, path, route_defining_threshold)
