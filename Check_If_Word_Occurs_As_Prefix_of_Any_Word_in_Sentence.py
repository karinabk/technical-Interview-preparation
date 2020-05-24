class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        
        
        for j in range(len(words)):
            if len(words[j]) < len(searchWord):
                continue
            i = 0
            while i < len(searchWord):
                if words[j][i] != searchWord[i]:
                    break
                i+= 1
            else:
                return j + 1
        return -1
            
