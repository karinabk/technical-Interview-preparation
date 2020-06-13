from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        freq = Counter(s)
        for el in  freq.most_common(len(freq)+1):
            for i in range(freq[el[0]]):
                result += el[0]
        return result
