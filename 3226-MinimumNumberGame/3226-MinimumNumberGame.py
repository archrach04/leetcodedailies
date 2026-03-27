# Last updated: 3/28/2026, 12:53:46 AM
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        for i in range(0,len(nums),2):
            arr.append(nums[i+1])
            arr.append(nums[i])
        return arr
        