# Last updated: 8/6/2026, 10:19:54 PM
1from collections import defaultdict
2class Solution:
3    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
4        subarr=nums[:k]
5        freq=defaultdict(int)
6        maxm=0
7        ans=0
8        l=0
9        for r in range(k):
10            freq[nums[r]]+=1
11            maxm+=nums[r]
12        if len(freq)==k:
13            ans=max(ans,maxm)
14        r=k
15        while r<len(nums):
16            if freq[nums[l]]==1:
17                del freq[nums[l]]
18            else:
19                freq[nums[l]]-=1
20            maxm-=nums[l]
21            l+=1
22            freq[nums[r]]+=1
23            maxm+=nums[r]
24            r+=1
25            if len(freq)==k:
26                ans=max(ans,maxm)
27        return ans
28
29
30                
31        