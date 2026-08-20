class Solution:
    def findMin(self, nums: List[int]) -> int:
        minval = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[r] and nums[mid]<= minval:
                minval = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
                
        return minval

        