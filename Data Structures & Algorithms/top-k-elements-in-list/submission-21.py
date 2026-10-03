class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      #count occurence of each number (use hash for key and val)
      #make list of empty lists the size of input arr
      
      #count each n in nums (ALWAYS take account for default 0)

      #for each num in count get key and value (.items because its hashmeep key val not index pos and value)
      
      #in freq at count [c], append the n of that count

      #make res arr
      #decrement from last (most count) in freq
      #res.append(n)
      #if res len is == k then return result 

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
        