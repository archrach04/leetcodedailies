# Last updated: 3/28/2026, 12:55:03 AM
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            
            res = res << 1
            bit = n%2
            res += bit
            n = n >> 1

        return res
