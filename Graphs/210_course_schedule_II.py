"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

from typing import List
class Solution:
    # Core logic:
    # 1. Check if the graph has any cycles
    # 2. If there are no cycles => topological sort can be performed.
    # 3. If there is any cycle => topological sort cannot be performed => students cannot take all the courses
    def dfs(self, course, cycle_set, stack, adj):
        if len(adj[course]) == 0 :
            # If there are no adj elements we will append them to the stack. But, we cannot just append here 
            # because we would make adj list empty later =>  we will keep adding the same course
            if course not in stack:
                stack.append(course)
            return True
        if course in cycle_set:
            return False
        
        cycle_set.add(course)
        for dep_course in adj[course]: 
                if not self.dfs(dep_course, cycle_set, stack, adj):
                    return False
                
        cycle_set.remove(course)
        stack.append(course)
        adj[course] = []
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Creating adjacency list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        print(adj)

        # Initialization
        # Have a visited set to detect cycle
        cycle_set = set() 
        # Visited_arr to mark the visited nodes
        # visited_arr = [0]*numCourses
        # Stack to keep the track of nodes visited
        stack = []
        # To store the result
        result = []

        # DFS on all the non-visited nodes
        for course in range(numCourses):
                # Check for cycles. If cycle exists return empty list
                if not self.dfs(course,cycle_set,stack,adj):
                    return []

        while len(stack) > 0:
            result.append(stack.pop())
        return result
        

def main() :
    solution = Solution()
    prereq = [[0,1],[0,2],[1,3],[1,4],[3,4]]
    numCourses = 5
    sol = solution.findOrder(numCourses, prereq)
    print(sol)

if __name__ == "__main__" :
    main()     
