# Last updated: 3/28/2026, 12:55:28 AM
class Solution:
    def plusOne(self, digits: List[int]):

       for i in range(len(digits) - 1, -1, -1):
          if digits[i] == 9:
             digits[i] = 0
          elif digits[i] < 9:
              digits[i] = digits[i] + 1
              return digits

# if all digits were 9
       return [1] + digits