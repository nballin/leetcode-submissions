#bucket sort
#output: retrurn list
#make emtpy count list -> make empty freq list for length on nums
#iterate through all n in nums ->update the value count at [n]
#for each c in c in count count.items (gets key and value)
#then for each c in freq, append the n.
#for i in the range len of freq, start and end and append n to the res until k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      count = {};
      freq = [[]for i in range(len(nums)+1)]

      for n in nums:
        count[n] = 1 + count.get(n, 0)
      
      for n, c in count.items():
        freq[c].append(n)

      res = []

      for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
          res.append(n)
          if len(res) == k:
            return res

        