def floyd_warshall(graph) -> list:
    '''
    Performs the Floyd-Warshall algorithm on the graph.
    '''
    nodes = len(list(graph.nodes()))
    edges = list(graph.edges(data=True))
    matrix = []
    for i in range(nodes):
        matrix.extend([['inf'] * nodes])
    for u in range(nodes):
        matrix[u][u] = 0
    for e in edges:
        matrix[e[0]][e[1]] = (e[2])['weight']
    for j in range(nodes):
        for l in range(nodes):
            for h in range(nodes):
                if matrix[l][h] == 'inf' and matrix[l][j] != 'inf' and matrix[j][h] != 'inf':
                    matrix[l][h] = matrix[l][j] + matrix[j][h]
                if matrix[l][j] == 'inf' or matrix[j][h] == 'inf':
                    matrix[l][h] = matrix[l][h]
                else:
                    matrix[l][h] = min(matrix[l][h], matrix[l][j] + matrix[j][h])
    return matrix
