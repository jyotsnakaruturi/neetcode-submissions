class Solution:
    def findMin(self, nums: List[int]) -> int:
        last=nums[-1]
        l=0
        res=nums[0]
        r=len(nums)-1
        while l <= r:
            mid=(l+r)//2
            if nums[mid]>last:
                l=mid+1
            else:
                res=nums[mid]
                r=mid-1
        return res
         

#in this we will do sorted part comparision
#if mid > last element then that is in rotated sorted part so u whave to move towords r=mid-1  else it is in sorte part then u whave to move l=mid+1 
#we will do comparison with static varible that is last element u can use first element
        