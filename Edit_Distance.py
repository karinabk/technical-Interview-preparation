class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()
        
        def editDist(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) not in memo:
                if word1[i] == word2[j]:
                    return editDist(i+1,j+1)
                else:
                    insert = 1+ editDist(i, j + 1)
                    delete =1+ editDist(i + 1,j)
                    replace =1+ editDist(i+1,j+1)
                    ans = min(insert, replace, delete)
                memo[(i, j)] = ans
            return memo[(i,j)]
        return editDist(0, 0)
