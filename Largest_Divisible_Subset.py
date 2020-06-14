class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        nums.sort()
        dp = [1] * len(nums)
        maxind = 1
        maxval = 0
        for i in range(1,len(nums)):
            
            for j in range(i-1,-1,-1):
            
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i] >= maxval:
                        maxval = dp[i]
                        maxind = i
       
        current = dp[maxind]
        temp = nums[maxind]
        result = set()
        for n in range(maxind,-1,-1):
            
            if temp % nums[n] == 0 and dp[n] == current:
                result.add(nums[n])
                temp = nums[n]
                current -= 1
        return result
        
