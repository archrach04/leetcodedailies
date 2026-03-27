# Last updated: 3/28/2026, 12:54:50 AM
class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            sum=0
            while num>0:
                temp=num%10
                num=num//10
                sum+=temp
            num=sum
        return num
        