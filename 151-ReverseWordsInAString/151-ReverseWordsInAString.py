# Last updated: 3/28/2026, 12:55:10 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        char=[]
        for i in s:
            if i!=" ":
                char.append(i)
            elif char and char[-1]!=" ":
                char.append(" ")
        if char and char[-1]==" ":
            char.pop()

        left,right=0,len(char)-1 
        while left<right:
            char[left],char[right]=char[right],char[left]
            left+=1
            right-=1
        
        start=0
        for i in range(len(char)+1):
            if i==len(char) or char[i]==" ":
                left,right=start,i-1
                while left<right:
                    char[left],char[right]=char[right],char[left]
                    left+=1
                    right-=1
                start=i+1
        return "".join(char)

                
        