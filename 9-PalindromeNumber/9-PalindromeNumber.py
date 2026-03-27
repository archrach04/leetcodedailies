# Last updated: 3/28/2026, 12:55:50 AM
class Solution:
    def isPalindrome(self, x):
        x=str(x)
        if x[::]==x[::-1]:
            return True
        else:
            False


def main():
    x=input("enter a number: ")
    print(Solution.isPalindrome(x))
        