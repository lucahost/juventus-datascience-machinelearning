def compute_in_degrees(digraph):
    res = {}
    for node in digraph.keys():
        res[node] = 0
    for indegrees in digraph.values():
        for indegree in indegrees:
            if indegree not in res.keys():
                res[indegree] = 1
            res[indegree] += 1
    return res
