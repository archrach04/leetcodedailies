# Last updated: 3/28/2026, 12:55:00 AM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso = {}
        ress = ""

        for i in range(len(s)):
            if s[i] in iso:
                ress += iso[s[i]]
            else:
                iso[s[i]] = t[i]
                ress += t[i]

        if ress != t:
            return False

        isot = {}
        rest = ""

        for i in range(len(t)):
            if t[i] in isot:
                rest += isot[t[i]]
            else:
                isot[t[i]] = s[i]
                rest += s[i]

        if rest == s:
            return True
        else:
            return False