# Last updated: 3/28/2026, 12:55:49 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L=0
        R=len(height)-1
        maxArea=0
        while L<R:
            area=min(height[L],height[R])*(R-L)
            maxArea=max(maxArea,area)
            if height[R]<height[L]:
                R-=1
            else:
                L+=1
       
        return maxArea

        