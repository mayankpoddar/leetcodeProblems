class Solution:
    
    def combinationSumHelper(self, candidates, target, n):
        results = []
        if n == 1:
            if target >= candidates[0] and (target % candidates[0] == 0):
                divisor = target // candidates[0]
                results.append([candidates[0]]*divisor)
        elif n > 1:
            firstElement = candidates[0]
            results = []
            if target == firstElement:
                results.append([firstElement])
            elif target > firstElement:
                for possible in self.combinationSumHelper(candidates, target-firstElement, n):
                    new_possible = [firstElement] + possible
                    results.append(new_possible)
                results.extend(self.combinationSumHelper(candidates[1:], target, n-1))
        return results
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        return self.combinationSumHelper(candidates, target, n)
        
        
        