class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxStorage = 0
        while l < r:
            length = r - l
            minheight = min(heights[l],heights[r])
            storage = minheight * length
            maxStorage = max(maxStorage, storage)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxStorage
            

        