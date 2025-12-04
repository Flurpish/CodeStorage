class Solution(object): #This is my example
    def twoSum(self, nums, target):
        solution = []

        for idx, value in enumerate(nums):
            for i, x in enumerate(nums):
                if value + x == target and idx != i:
                    solution.append(idx)
                    solution.append(i)
                    return solution
        
        
class BestPractice(object): #This is one of the best ways to handle this in python
    def twoSum(self, nums, target):
        # Dictionary to store {value: index}
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num  # What number do we need?
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i  # Remember this number's index
        
        return []