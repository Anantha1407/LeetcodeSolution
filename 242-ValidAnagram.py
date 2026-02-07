class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        wor={}
        for i in s:
            if i in wor:
                wor[i]+=1
            else:
                wor[i]=1
        for i in t:
            if i in wor:
                wor[i]-=1
            else:
                return False
        for i,val in wor.items():
            if val !=0:
                return False
        return True
