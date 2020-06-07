class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1)//2]
        arr.sort(key=lambda el: (abs(el - m),el),reverse=True)
        answer = [arr[i] for i in range(k)]
        return answer
