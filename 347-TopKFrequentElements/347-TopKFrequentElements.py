# Last updated: 3/28/2026, 12:54:43 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])

        for j in count:
            bucket[count[j]].append(j)
        op=[]
        n=len(bucket)-1
        while len(op) < k:
            if bucket[n]:
                for x in bucket[n]:
                    op.append(x)
            n -= 1
        return op



            


        