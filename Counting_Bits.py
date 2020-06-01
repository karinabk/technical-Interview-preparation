class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        
        for i in range(num + 1):
            
            binstr = str(bin(i))
            binlist = list(binstr)
            
            sum_ = 0
            for j in range(2,len(binlist)):
                
                sum_ += int(binlist[j])
            result.append(sum_)
        return result
