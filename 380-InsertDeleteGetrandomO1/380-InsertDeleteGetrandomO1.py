# Last updated: 3/28/2026, 12:54:41 AM
import random
class RandomizedSet:

    def __init__(self):
        self.numMap={}
        self.numList=[]


    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        else:
            self.numList.append(val)
            self.numMap[val]=len(self.numList)-1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.numMap:
            if self.numList[-1]==val:
                self.numList.pop()
                del self.numMap[val]
            else:
                ind=self.numMap[val]
                self.numList[ind]=self.numList[len(self.numList)-1]
                self.numList[len(self.numList)-1]=val
                self.numMap[self.numList[ind]]=ind
                del self.numMap[val]
                self.numList.pop()
            return True
        else:
            return False

        

    def getRandom(self) -> int:
            return random.choice(self.numList)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()