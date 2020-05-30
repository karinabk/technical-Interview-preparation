class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        slist = list(s)
        perms = set()
        
        temp = slist[:k-1]

        for i in range(k-1,len(s)):
            temp.append(s[i])
            perms.add(tuple(temp))
            temp.pop(0)
        return len(perms) == 2**k
           
        
