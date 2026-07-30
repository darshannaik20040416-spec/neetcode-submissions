class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        maxStorage = 0
        for i in range(l):
            for j in range(i+1, l):
                length = j - i
                minheight = min(heights[i],heights[j])
                storage = minheight * length
                maxStorage = max(maxStorage, storage)
        return maxStorage
                
        