# Last updated: 3/28/2026, 12:54:56 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        