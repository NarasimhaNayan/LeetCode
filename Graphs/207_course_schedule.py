"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

# Better to do with BFS
from typing import List
from collections import deque
class Solution:

    def topological_sort(self,node,visited,stack,adj):
        visited[node] = 1
        # if there are no dependency on the courses
        if len(adj[node]) == 0 :
            return
        
        temp_list = adj[node]
        for i in temp_list:
            if visited[i] == 0 :
                self.topological_sort(i,visited,stack,adj)
                temp_list.remove(i)
                stack.append(i)

    def dfs(self,course,visited_courses,adj):
        # If course is already visited  
        if course in visited_courses:
            return False
        # If courses do not have any dependency
        if len(adj[course]) == 0 :
            return True 
        visited_courses.add(course)
        for prereq in adj[course]:
            if not self.dfs(prereq,visited_courses,adj): return False
        # The main reason we remove the course from visited_courses set is because we are doing DFS from a particular node 
        # and we want to detect cycle from that node
        # This step acts as a backtracking step 
        visited_courses.remove(course)
        # We are assigning empty list for that particular course who completed the DFS without cycle to avoid repetation
        adj[course] = []
        return True

    def bfs(self, queue, adj, indegree):
        while len(queue)>0:
            ele = queue.popleft()

            for adj_node in adj[ele] :
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # pre_req has the edge a1-> b1
        # Draw graph based on the edgesand create adj list.
        adj = {}
        indegree = [0]*numCourses
        for i in range(numCourses):
            adj[i] = []
        for i,j in prerequisites :
            if i in adj:
                adj[j].append(i)
                indegree[i] += 1

        # Apply topological sorting on this adj list
        # Initialization
        # visited_courses = set()

        # Apply DFS
        # for course in range(numCourses) :
        #     # if visited[i] == 0 :
        #     if not self.dfs(course,visited_courses,adj):
        #         return False    
        # return True
    
        # BFS implementation:
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        for i in range(numCourses):
            self.bfs(queue,adj,indegree)

        for i in range(len(indegree)):
            if indegree[i] != 0 :
                return False
        return True

def main() :
    solution = Solution()
    prereq = [[0,1],[0,2],[1,3],[1,4],[3,4]]
    numCourses = 5
    sol = solution.canFinish(numCourses, prereq)
    print(sol)

if __name__ == "__main__" :
    main()