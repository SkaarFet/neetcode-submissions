from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        [0, 2], [3, 0]
        '''
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        # add the treasure into q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    continue
                
                q.append((r, c))

        #         up       down    left     right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # run bfs on the treasures to find shortest path
        while q:
            curr = q.popleft()
            # current distance
            r, c = curr[0], curr[1]

            # check adjacent neighbors
            for dir in dirs:
                dr = r + dir[0]
                dc = c + dir[1]
                # skip if:
                # - out of bounds
                # - is water
                # - already has a distance
                if (dr < 0 or dr >= ROWS or
                    dc < 0 or dc >= COLS or
                    grid[dr][dc] == -1 or 
                    grid[dr][dc] != 2147483647
                ):
                    continue

                # add the neighbor to q
                q.append((dr, dc))
                # mark as visited (add curr distance + 1)
                grid[dr][dc] = grid[r][c] + 1

                