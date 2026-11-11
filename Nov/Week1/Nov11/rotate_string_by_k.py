class Solution(object):
    def rotate(self, s, k):
        s=list(s)
        k=k%len(s)
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        left=0
        right=k-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        left=k
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return "".join(s)
                