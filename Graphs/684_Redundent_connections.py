"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi 
in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, 
return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

from typing import List
class Solution:
    def find(self, node, parent):
        if node != parent[node] :
            parent[node] = self.find(parent[node],parent) # Path Compression
        return parent[node]
    
    def union(self, rank, parent,pnode1,pnode2):
        if rank[pnode1] < rank[pnode2]:
            parent[pnode1] = pnode2
        else:
            if rank[pnode1] == rank[pnode2]:
                rank[pnode1]+=1 
            parent[pnode2] = pnode1
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # Solve using UnionFind by rank
        rank = [0]*(n+1)
        parent = [0]*(n+1)
        for i in range(n+1):
            parent[i]=i

        # Union
        # check if 2 parents are same. If not then, compare the ranks of both and attch the lower ranked tree to higher ranked tree.
        # if both parents are same => cycle and that edge has to be returned.
        for node1, node2 in edges:
            pnode1 = self.find(node1,parent)
            pnode2 = self.find(node2,parent)
            if pnode1 == pnode2 :
                return [node1,node2]
            else:
                self.union(rank,parent,pnode1,pnode2)

def main():
    solution = Solution()
    edges = [[1,2],[1,3],[2,3]]
    res=solution.findRedundantConnection(edges)
    print(res)

if __name__ == "__main__" :
    main()