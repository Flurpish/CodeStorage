#interesting name
# This type of sort is pretty important to remember

class Solution(object):
    def threeSumClosest(self, nums, target):
        # Start by sorting

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        if len(nums) == 3:
            return closest

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(target - closest):
                    closest = total

                if total == target:
                    return total

                if total < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest
