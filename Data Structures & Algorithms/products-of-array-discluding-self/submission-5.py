class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #make a result arr with default 1s for the length of nums 
        #prefix default 1
        #for i in range of the len nums
        #make the res at index = prefix 
        #update prefix to multiply and = num[i]

        #postfix = 1
        #for i in range len numbers from last
        #res[i] which is the prefix arr *= postfix
        #postfic *= the nums[s]
        #return res


      res = [1] * (len(nums))

      prefix = 1

      for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

      postfix = 1
      for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]
      return res

