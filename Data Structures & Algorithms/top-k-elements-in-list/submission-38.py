class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #where key is the nubmer and i is the count (which is index in freq list)

        freq = [[]for i in range(len(nums)+1)]

        for n in nums:
          count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
          freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1):
          for n in freq[i]:
            res.append(n)

            if len(res) == k:
              return res