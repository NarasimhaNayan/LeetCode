"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""

from typing import List
from collections import deque
class Solution:
    def bfs(self,queue, adj,indegree):
        while len(queue) > 0 :
            node = queue.popleft()
            for neighbour in adj[node] :
                if indegree[neighbour] == 0:
                    continue
                indegree[neighbour] -= 1
                if indegree[neighbour] == 1 :
                    queue.append(neighbour)

    def bfs_finding_components(self,queue, adj, visited):
        while len(queue) > 0 :
            node = queue.popleft()
            visited[node] = 1
            for neighbour in adj[node] :
                if neighbour not in queue and visited[neighbour] == 0:
                    queue.append(neighbour)
                # if indegree[neighbour] == 0:
                #     continue
                # indegree[neighbour] -= 1
                # if indegree[neighbour] == 1 :
                #     queue.append(neighbour)

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        indegree = [0]*n
        queue = deque()
        visited= [0]*n
        num_of_components = 0

        for i in range(n):
            adj[i] = []

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
            indegree[i] += 1
            indegree[j] += 1
        
        # 2 conditions for a valid tree
        # 1. Should have only 1 connected-component
        for i in range(n):
            if num_of_components > 1 :
                return False
            if visited[i] == 0:
                num_of_components+=1
                queue.append(i)
                self.bfs_finding_components(queue, adj,visited)

        # 2. Must be acyclic
        for i in range(len(indegree)) :
            if indegree[i] == 1 :
                queue.append(i)
                indegree[i] -= 1

        for i in range(n):
            self.bfs(queue,adj,indegree)
        

        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False
        return True
        

def main():
    solution = Solution()
    n=5
    edges=[[0,1],[2,3]]
    res = solution.validTree(n,edges)
    print(res)

if __name__ == "__main__":
    main()       