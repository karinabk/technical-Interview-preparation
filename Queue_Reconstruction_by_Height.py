class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        
        people.sort(key=lambda p: (-p[0],p[1]))
        answer = []
        for p in people:
        
            answer.insert(p[1],p)          
        return answer
        
                
            
