class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        k=len(s)
        for i in range(k):
            new=list(s)
            left=0
            right=len(new)-1
            while left<right:
                new[left],new[right]=new[right],new[left]
                left+=1
                right-=1

            left=0
            right=i-1
            while left<right:
                new[left],new[right]=new[right],new[left]
                left+=1
                right-=1
            left=i
            right=len(new)-1
            while left<right:
                new[left],new[right]=new[right],new[left]
                left+=1
                right-=1
            if "".join(new)==goal:
                return True
        return False
                