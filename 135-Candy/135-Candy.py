# Last updated: 3/28/2026, 12:55:14 AM
class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                arr[i]=arr[i-1]+1
        for j in range(len(ratings)-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                arr[j]=max(arr[j],arr[j+1]+1)
        sum=0
        for k in arr:
            sum+=k
        
        return sum
        
        