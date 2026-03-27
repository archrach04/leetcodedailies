# Last updated: 3/28/2026, 12:54:26 AM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for op in operations:
            if op=="+":
                stk.append(stk[-1]+stk[-2])
            elif op=="C":
                stk.pop()
            elif op=="D":
                stk.append(stk[-1]*2)
            else:
                stk.append(int(op))
        s=0
        for i in stk:
            s+=i
        return s

            