# Last updated: 3/28/2026, 12:55:39 AM
class Solution:
    def trap(self, height: List[int]) -> int:

        left_max=float('-inf')
        n=len(height)
        if n<3:
            return 0
        tot=0
        right_max=[0]*n
        right_max[-1]=height[-1]
        for i in range(n-2,-1,-1):
            right_max[i]=max(height[i],right_max[i+1])

        for i in range(1,n-1):
            left_max=max(left_max,height[i-1])
            if (min(right_max[i+1],left_max)-height[i])>0:
                tot+=min(right_max[i+1],left_max)-height[i]
            
        
        return tot
            
            
        