class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''

        '''

        adj = [[] for i in range(n)]
        visited = set()

        # populate the adj list
        # undirected, append both ways
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # track parent node
        def dfs(node, parent) -> bool:
            # mark as visited
            visited.add(node)

            # go through neighbors
            for nei in adj[node]:
                # skip if neighbor is the direct parent
                if nei == parent:
                    continue

                # not valid graph if the neighbor is already visited and is not the parent
                if nei in visited:
                    return False # found cycle

                dfs(nei, node)

            return True

        # just call dfs on the node 0
        if not dfs(0, 0):
            return False

        # check for unconnected nodes
        if len(visited) != n:
            return False
        
        return True
