"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 2^31 - 1.
"""
from typing import List
from collections import deque

class Solution:
    INF = 2**31 - 1

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)

    def bfs(self, rooms: List[List[int]], i: int, j: int) -> None:
        m = len(rooms)
        n = len(rooms[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(i, j)])

        distance = 1

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for direction in directions:
                    next_x = x + direction[0]
                    next_y = y + direction[1]

                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        continue
                    if rooms[next_x][next_y] == self.INF or rooms[next_x][next_y] > distance:
                        rooms[next_x][next_y] = distance
                        queue.append((next_x, next_y))
            distance += 1



    def run(self):
        rooms1 = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
        print("aaa")
        self.wallsAndGates(rooms1)
        print(rooms1)

        rooms2 = [[-1]]
        self.wallsAndGates(rooms2)
        print(rooms2)
        


if __name__ == "__main__":
    Solution().run()