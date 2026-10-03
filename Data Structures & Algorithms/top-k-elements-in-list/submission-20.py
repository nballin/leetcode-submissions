class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      #make count hashmap (k: number, v: count)
      #make a list of empty lists (i: count, v: numbers of that count)
      #count occurence of each number, put it in count (always .get for def 0)
      #lets bucket sort
      #for key and val in count (.items) (returns key and val)
      #freq[c] -> append (n)
      #res = []
      #for i in range (decrement -1,0,-1) (len(freq)):
      #for n in freq at [i] -> res.append(n)
      
      #if len(res) == k then return res

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