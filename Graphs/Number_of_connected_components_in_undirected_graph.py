"""
Count Connected Components
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""

from typing import List
# from collections import deque
class Solution:

    def bfs(self, queue, adj, visited):
        while len(queue) > 0:
            ele = queue.popleft()
            visited[ele] = 1
            for neighbour in adj[ele]:
                if neighbour not in queue and visited[neighbour] == 0: 
                    queue.append(neighbour)

    def dfs(self, node, adj, visited):
        if visited[node] == 1 :
            return
        visited[node] = 1
        for neighbour in adj[node]:
            if visited[neighbour] == 0 :
                self.dfs(neighbour,adj,visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency matrix
        adj = {}
        for i in range(n):
            adj[i] = []
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = [0]*n
        # queue = deque()
        no_of_connected_components = 0
        
        # Perform BFS on all the nodes
        for i in range(n):
            if visited[i] == 0 :
                # queue.append(i)
                no_of_connected_components += 1
                # self.bfs(queue,adj,visited)
                self.dfs(i,adj,visited)

        return no_of_connected_components
    

def main():
    solution = Solution()
    n = 6
    edges = [[0,1], [1,2], [2,3], [4,5]]
    res = solution.countComponents(n,edges)
    print(res)

if __name__ == "__main__":
    main()