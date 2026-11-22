class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        T:
        S:
        create an adj list first
        created a set to track visited nodes
        then for each unvisited node, run dfs on it and increment # of components
        '''

        # create adj list
        graph = [[] for _ in range(n)]

        # undirected graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        components = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            # visit every connected node in component
            for nei in graph[node]:
                dfs(nei)

        for node in range(n):
            # skip visited
            if node in visited:
                continue
            
            dfs(node)
            components += 1
        
        return components
                

        

