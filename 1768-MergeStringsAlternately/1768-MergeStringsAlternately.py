# Last updated: 5/9/2026, 4:14:17 PM
1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        visited=set()
4        stack=[0]
5        while stack:
6            room=stack.pop()
7            visited.add(room)
8            for key in rooms[room]:
9                if key not in visited:
10                    stack.append(key)
11        if len(visited)==len(rooms):
12             return True
13        else: 
14            return False
15                    