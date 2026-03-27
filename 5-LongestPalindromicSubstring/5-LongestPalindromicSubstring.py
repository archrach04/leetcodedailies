# Last updated: 3/28/2026, 12:55:52 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        word = ""
        maxlen = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxlen:
                    word = s[l:r+1]
                    maxlen = r - l + 1

                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxlen:
                    word = s[l:r+1]
                    maxlen = r - l +1
                l -= 1
                r += 1

        return word