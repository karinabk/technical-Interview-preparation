from random import randrange
class Solution:

    def __init__(self, w: List[int]):
        self.nums = []
        self.l = 0
        for i in range(len(w)):
            self.l += w[i]
            self.nums.append(self.l)
                        
    def pickIndex(self) -> int:
       
        rnum = randrange(self.l)
        for el in range(len(self.nums)):
            if rnum < self.nums[el]:
                return el
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
