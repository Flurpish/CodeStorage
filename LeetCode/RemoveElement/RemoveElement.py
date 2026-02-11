class Solution(object):
    def removeElement(self, nums, val):
        nums[:] = [x for x in nums if x != val]
        return len(nums)
    
    #This works because nums[:] is creating a slice
    #of the original array. Basically an empty array
    #that changes the original based on what you put in it.

    #x for x in nums if x != val:
    #this means that insert x into nums based on the loop
    #   for x in nums
    #       and insert if x != val