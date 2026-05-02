#reutn list of integers 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = {} #empty list to store each numbers frequency 
      freq = [[] for i in range(len(nums) + 1)] #index is going to be the count of an element

      for n in nums:
        count[n] = 1 + count.get(n, 0);
      
      for n, c in count.items():
        freq[c].append(n) #this value n occurs c number of times

      res = []
      for i in range(len(freq) -1, 0, -1): #last index, up until 0, in decending order
        for n in freq[i]:
          res.append(n)
          if len(res) == k:
            return res