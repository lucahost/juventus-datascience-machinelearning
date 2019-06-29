from three import compute_in_degrees


def in_degree_distribution(digraph):
    indegree = compute_in_degrees(digraph)
    distribution = {}
    for count in indegree.values():
        if count not in distribution.keys():
            distribution[count] = 0
        distribution[count] += 1
    return distribution
