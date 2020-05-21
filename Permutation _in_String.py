#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
#In other words, one of the first string's permutations is the substring of the second string.

 

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window
        s1cnt = Counter(s1)
        s2cnt = Counter(s2[:len(s1)-1])
        for i in range(len(s1)-1,len(s2)):
            s2cnt[s2[i]] += 1
            if s1cnt == s2cnt:
                return True
            s2cnt[s2[i-len(s1)+1]] -=1
            if s2cnt[s2[i-len(s1)+1]] == 0:
                del s2cnt[s2[i-len(s1)+1]]
        return False
             
