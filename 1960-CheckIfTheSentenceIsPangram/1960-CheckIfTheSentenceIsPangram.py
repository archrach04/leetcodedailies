# Last updated: 3/28/2026, 12:54:00 AM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set(sentence)
        if len(s)==26:
            return True
        else:
            return False