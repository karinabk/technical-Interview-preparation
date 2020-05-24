from collections import Counter
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        maxlet = 0
        count = 0
        
        for i in range(k-1):
            
            if s[i] in vowels:
                count += 1
        for j in range(k -1,len(s)):
           
            if s[j] in vowels:
                count += 1
            maxlet = max(count, maxlet)
            
            if s[j-k+1] in vowels:
                count -= 1
        return maxlet
        
