# Last updated: 4/1/2026, 11:35:51 PM
1class Solution:
2    def multiply(self, num1: str, num2: str) -> str:
3        if num1 == "0" or num2 == "0":
4            return "0"
5        
6        n, m = len(num1), len(num2)
7        res = [0] * (n + m)
8        
9        # Multiply digits
10        for i in range(n - 1, -1, -1):
11            for j in range(m - 1, -1, -1):
12                mul = int(num1[i]) * int(num2[j])
13                
14                p1 = i + j
15                p2 = i + j + 1
16                
17                total = mul + res[p2]
18                
19                res[p2] = total % 10
20                res[p1] += total // 10
21        
22        # Convert to string (skip leading zeros)
23        result = []
24        for num in res:
25            if not (len(result) == 0 and num == 0):
26                result.append(str(num))
27        
28        return "".join(result)