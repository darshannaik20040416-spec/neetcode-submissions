class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(numbers):
            current = target - num
            if current in seen:
                return [seen[current]+1,i+1]
            seen[num] = i