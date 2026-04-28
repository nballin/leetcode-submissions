class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      #Output: arr of product (multiply everything bit nums[i])
      #1. set output arr 
      #2. set prefix = 1
      #iterate through nums
      #3. res[i] = prefix;
      #4. prefix updates with the next [i] in nums (multiply both)
      #5. prefix *= nums[i]

      #6. set postfix = 1
      #7. same thing with postfix as prefix

      res = [1] * len(nums);
      prefix = 1;
      for i in range(len(nums)):
        res[i] = prefix;
        prefix *= nums[i];

      postfix = 1;
      for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix;
        postfix *= nums[i];

      return res;
