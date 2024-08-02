#Remove duplicates
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        k=1
        for i in range(1,l):
            if nums[i]==nums[i-1]:
                pass
            else:
                nums[k]=nums[i]
                k+=1
        return k
