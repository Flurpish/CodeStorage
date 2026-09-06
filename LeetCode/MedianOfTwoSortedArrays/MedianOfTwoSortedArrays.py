class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = nums1 + nums2
        arr.sort()

        if len(arr) % 2 == 0:
            return float(arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2

        else:
            return float(arr[len(arr)//2])