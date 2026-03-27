# Last updated: 3/28/2026, 12:55:54 AM
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        x = []
        for i in range(len(nums1)):
            x.append(nums1[i])
        for j in range(len(nums2)):
            x.append(nums2[j])
        
        x.sort()  # Sorting the merged list

        if len(x) % 2 != 0:
            num = len(x) // 2
            save = x[num]
            return save
        else:
            num = len(x) // 2
            save = (x[num - 1] + x[num]) / 2
            return save
def main():
    nums1=[]
    nums2=[]
    m=int(input('enter size of array nums1: '))
    n=int(input('enter size of array nums2: '))
    for i in range (0,m):
         x=int(input('enter element: '))
         nums1.append(x)
    for i in range (0,n):
         x=int(input('enter element: '))
         nums2.append(x)
    print(Solution.findMedianSortedArrays(nums1, nums2))