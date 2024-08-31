from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):
        # Initialize BFS
        m, n = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set((entrance[0], entrance[1]))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        
        while queue:
            r, c, steps = queue.popleft()
            
            # Check if this is an exit (and not the entrance)
            if (r != entrance[0] or c != entrance[1]) and (r == 0 or r == m-1 or c == 0 or c == n-1):
                return steps
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and maze[nr][nc] == '.':
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))
        
        return -1  # If no exit is found

# Example usage:
maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]

# Create an instance of the Solution class
solution = Solution()
# Call the nearestExit method
print(solution.nearestExit(maze, entrance))  # Output: 1
