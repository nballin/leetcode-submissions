class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #get count of all numbers using hashmap
        #using count, we are bucket sorting numbers into a list where the key is how many times they appeared
        #and the going from end to start for k values

        #make empty frequency list as long as nums

        #for all n in nums -> update count (and default 0)

        #for all n,c in count (use .items for key and value)
        #freq at count c -> append n 

        #make result []
        # go backwards from the end until res len == k then return result

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
          count[n] = 1+ count.get(n,0)

        for n,c in count.items():
          freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1):
          for n in freq[i]:
            res.append(n)
            if len(res) == k:
              return res