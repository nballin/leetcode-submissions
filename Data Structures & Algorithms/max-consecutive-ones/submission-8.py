class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      max_count = 0;
      current = 0;

      for n in nums:
          if n == 1:
            current += 1;
            max_count = max(max_count,current);
          else:
            current = 0;
      return max_count;









#output: max_count = 0
#current = 0

#1. Iterate through n in nums (For)
#2. Update current if n = 1
#3. actively update max count using max(max_count, current)
#4. is the else (if n = 0), then return current = 0 (streak over)
#return finale max_count
