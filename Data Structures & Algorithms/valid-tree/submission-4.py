class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        build an adjacency list

        visited set - tracks visited nodes

        --> track parent node b/c graph is undirected and we don't want to revisit the parent
        --> but if we reach a node that isn't the parent but we already visited, that means theres a cycle in the list
        in dfs(node, parent):
        - Base:
            - alr in visited set, return False

        
        - mark each node as visited
        - go through the current node neighbors using the adj list and run dfs on each neighbor

        run dfs on the root node (0)
        '''

        # adj list
        graph = [[] for _ in range(n)]

        # populate it
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)

        visited = set()

        def dfs(node, parent) -> bool:
            if node in visited: 
                return False

            visited.add(node)
            # visit neighbors
            for nei in graph[node]:
                # skip parent
                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False

            return True
        
        if not dfs(0, 0): 
            return False

        # disconnected graph
        if len(visited) != n:
            return False

        return True

        
