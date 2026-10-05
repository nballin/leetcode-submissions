class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      # count of each number 
      # bucket sort by adding a list of numbers per that count
      #go from end of res, add res up to k values

      count = {}
      freq = [[]for i in range(len(nums)+1)]

      for n in nums:
        count[n] = 1 + count.get(n,0)

      for n, c in count.items():
        freq[c].append(n)

      res = []
      for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
          res.append(n)

          if len(res) == k: 

            return res
        