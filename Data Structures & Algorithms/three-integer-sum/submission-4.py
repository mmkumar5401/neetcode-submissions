class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        n=len(nums)
        i=0
        result=set()
        while(i<n-2):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j=i+1
            k=n-1
            while(j<k):
                # print(i,j,k)
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    result.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif s<0:
                    j+=1
                else:
                    k-=1
            i+=1
        return(list(result))