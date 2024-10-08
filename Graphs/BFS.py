"""
Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
Note: One can move from node u to node v only if there's an edge from u to v. Find the BFS traversal of the graph 
starting from the 0th vertex, from left to right according to the input graph. Also, you should only take nodes directly 
or indirectly connected from Node 0 in consideration.

Example 1:
Input:
V = 5, E = 4
adj = {{1,2,3},{},{4},{},{}}
Output: 
0 1 2 3 4
Explanation: 
0 is connected to 1 , 2 , 3.
2 is connected to 4.
so starting from 0, it will go to 1 then 2
then 3. After this 2 to 4, thus bfs will be
0 1 2 3 4.


Example 2:
Input:
V = 3, E = 2
adj = {{1,2},{},{}}
Output: 
0 1 2
Explanation:
0 is connected to 1 , 2.
so starting from 0, it will go to 1 then 2,
thus bfs will be 0 1 2. 

Your task:
You dont need to read input or print anything. 
Your task is to complete the function bfsOfGraph() which takes the integer V denoting the number of vertices and 
adjacency list as input parameters and returns  a list containing the BFS traversal of the graph starting from 
the 0th vertex from left to right.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ V, E ≤ 104
"""

from typing import List
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [0]*V
        queue = deque()
        queue.append(0)
        res = []
        while len(queue) > 0:
            pop_ele = queue.popleft()
            res.append(pop_ele)
            visited[pop_ele] = 1
            for neighbour in adj[pop_ele] :
                if visited[neighbour] == 0 and neighbour not in queue:
                    queue.append(neighbour)
        return res