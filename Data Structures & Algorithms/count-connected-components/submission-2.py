class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''

        T: O(V + E)   V = vertices, E = edges
        S:
        create an adj list first
        created a set to track visited nodes
        then for each unvisited node, run dfs on it and increment # of components
        '''

        # create adj list T: O(V) S: O(V + E)
        graph = [[] for _ in range(n)]

        # undirected graph
        for a, b in edges: # T: O(E)
            graph[a].append(b)
            graph[b].append(a)

        components = 0
        visited = set() # S: O(V)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            # visit every connected node in component
            for nei in graph[node]: # T: O(V + E)
                dfs(nei)

        for node in range(n): # T: O(V)
            # skip visited
            if node in visited:
                continue
            
            dfs(node) # T: O(V + E) S: O(V)
            components += 1
        
        return components
                

        

