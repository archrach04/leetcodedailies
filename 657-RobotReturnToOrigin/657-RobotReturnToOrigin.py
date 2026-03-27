# Last updated: 3/28/2026, 12:54:27 AM
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos=(0,0)
        pos=list(pos)
        for i in moves:
            if i=="U":
                pos[1]+=1
            elif i=="D":
                pos[1]-=1
            elif i=="R":
                pos[0]+=1
            else:
                pos[0]-=1
        if pos==[0,0]:
            return True
        return False
            
        