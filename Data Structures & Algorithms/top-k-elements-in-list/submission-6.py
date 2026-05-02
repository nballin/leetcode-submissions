#return list res
#bucket sort -> so index is count -> value is numbers under that count
#make count empty list 
#then make freq emptyt list as long as length of nums

#iterate n in nums -> update count ->count[n] = 1 + count.get(n,0)
#iterate for n, c in count.items(get key and value)
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = {}
      freq = [[] for i in range(len(nums)+ 1)]

      for n in nums:
        count[n] = 1 + count.get(n, 0);

      for n, c in count.items():
        freq[c].append(n)

      res = []

      for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
          res.append(n);
          if len(res) == k:
            return res