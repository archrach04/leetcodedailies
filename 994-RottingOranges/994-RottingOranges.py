# Last updated: 4/8/2026, 11:43:07 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        q=deque()
4        time,fresh=0,0
5        r,c=len(grid),len(grid[0])
6        for row in range(r):
7            for col in range(c):
8                if grid[row][col]==1:
9                    fresh+=1
10                if grid[row][col]==2:
11                    q.append([row,col])
12        
13        dir=[[0,1],[0,-1],[1,0],[-1,0]]
14        while q and fresh>0:
15            for i in range(len(q)):
16                row,col=q.popleft()
17                for dr, dc in dir:
18                    nr, nc=dr+row, dc+col
19                    if (nr<0 or nr==len(grid)) or (nc<0 or nc==len(grid[0])) or grid[nr][nc]!=1:
20                        continue
21                    grid[nr][nc]=2
22                    q.append([nr,nc])
23                    fresh-=1
24            time+=1
25      
26        return time if fresh==0 else -1
27            
28