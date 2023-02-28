def kruskala(graph):
    '''
    Performs the Kruskal's algorithm on the graph.
    '''
    result = []
    all_nodes = list(graph.nodes())
    edges = list(graph.edges(data=True))
    sorted_edges = sorted(edges, key=lambda elem: (elem[2])['weight'])
    parent = {node: node for node in all_nodes}
    rank = {node: 0 for node in all_nodes}

    def find(node):
        '''
        Finds the parent of the node (it may be the node itself).
        '''
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        '''
        Finds if two nodes have union (this is done to prevent adding cycles to minimum spanning tree).
        '''
        root1 = find(node1)
        root2 = find(node2)
        if root1 == root2:
            return None
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1
    for edge in sorted_edges:
        node1, node2, data = edge
        if find(node1) != find(node2):
            result.append(edge)
            union(node1, node2)
    return result
  
def prim(graph):
    '''
    Performs Prim`s algorithm on the graph.
    '''
    result = []
    visited_nodes = {0}
    all_nodes = list(graph.nodes())
    edges = list(graph.edges(data=True))
    sorted_edges = sorted(edges, key=lambda elem: (elem[2])['weight'])
    while len(visited_nodes) != len(all_nodes):
        for edge in sorted_edges:
            if edge[0] in visited_nodes and edge[1] not in visited_nodes:
                result.append(edge)
                visited_nodes.add(edge[1])
                break
            elif edge[1] in visited_nodes and edge[0] not in visited_nodes:
                result.append(edge)
                visited_nodes.add(edge[0])
                break     
    return result
