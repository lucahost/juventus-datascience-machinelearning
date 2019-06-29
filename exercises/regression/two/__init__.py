def generate_complete_graph(num_nodes):
    if num_nodes > 0:
        graph = {}
        nodes = [n for n in range(num_nodes)]
        for node in range(num_nodes):
            graph[node] = set()
            for edge in nodes:
                if edge != node:
                    graph[node].add(edge)
        return graph
    else:
        return {}
