# Last updated: 4/5/2026, 10:38:52 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m=len(matrix)
4        n=len(matrix[0])
5        l=0
6        r=m*n-1
7        i=(l+r)//2
8        rw=i//n
9        cm=i%n
10        while l<=r:
11            if target<matrix[rw][cm]:
12                r=i-1
13                i = (l + r) // 2
14                rw=i//n
15                cm=i%n
16            elif target>matrix[rw][cm]:
17                l=i+1
18                i = (l + r) // 2
19                rw=i//n
20                cm=i%n
21            else:
22                return True
23        return False
24
25        