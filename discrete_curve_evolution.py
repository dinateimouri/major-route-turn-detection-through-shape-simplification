import matplotlib.pyplot as plt
import networkx as nx
import pyproj


def calculate_dce_values(digraph, path):
    dce_values = []
    for i in range(1, len(path)-1):
        pointA = (digraph.nodes[path[i-1]]['lat'], digraph.nodes[path[i-1]]['lon'])
        pointDP = (digraph.nodes[path[i]]['lat'], digraph.nodes[path[i]]['lon'])
        pointB = (digraph.nodes[path[i+1]]['lat'], digraph.nodes[path[i+1]]['lon'])
        fwd_azimuth1, _, l1 = get_azimuth(pointA, pointDP)
        fwd_azimuth2, _, l2 = get_azimuth(pointDP, pointB)
        beta = abs(fwd_azimuth1 - fwd_azimuth2)
        k = (beta * l1 * l2) / (l1 + l2)
        dce_values.append(k)
    return dce_values


def dce_with_threshold_percentage(digraph, path, threshold):
    dce_values = calculate_dce_values(digraph, path)
    max_dce = max(dce_values)
    path_threshold = max_dce * threshold
    origin, destination = path[0], path[-1]
    path_dce_with_od = path.copy()
    level = 0
    plot_name = f'plots/{origin}_to_{destination}_dce_threshold_{threshold}_level_{level}.png'
    plot_current_shape(digraph, path, plot_name)
    while any(value < path_threshold for value in dce_values):
        level += 1
        min_dce_value = min(dce_values)
        min_dce_indexes = [i for i, x in enumerate(dce_values) if x == min_dce_value and i not in (0, len(path)-1)]
        path_dce_with_od = [path_dce_with_od[i] for i in range(len(path_dce_with_od)) if i not in min_dce_indexes]
        dce_values = calculate_dce_values(digraph, path_dce_with_od)
        plot_name = f'plots/{origin}_to_{destination}_dce_threshold_{threshold}_level_{level}.png'
        plot_current_shape(digraph, path_dce_with_od, plot_name)
    return path_dce_with_od


def get_azimuth(pointA, pointB):
    lon1, lat1, lon2, lat2 = pointA[1], pointA[0], pointB[1], pointB[0]
    geod = pyproj.Geod(ellps='WGS84')
    fwd_azimuth, back_azimuth, distance = geod.inv(lon1, lat1, lon2, lat2)

    return fwd_azimuth, back_azimuth, distance

