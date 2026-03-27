# Last updated: 3/28/2026, 12:54:42 AM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        hmap={}
        for i in nums1:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1
        for j in nums2:
            if j in hmap and hmap[j]>0:
                res.append(j)
                hmap[j]-=1
        return res
        