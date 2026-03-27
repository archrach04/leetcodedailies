# Last updated: 3/28/2026, 12:55:42 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        for l in range(len(haystack)-len(needle)+1):
            if haystack[l]==needle[0]:
                temp=1
                for r in range(l+1,l+len(needle)):
                    if needle[temp]==haystack[r]:
                        temp+=1
                    else:
                        break
                if temp==len(needle):
                    return l
        return -1

                