class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make count hash (key and value -> number and count)
        #make a list of empty lists (freq) the same length of input arr

        #count each numbers occurence (ACOUNT FOR POSSIBLE NON EXISTENCE)

        #get each num and count from hashmap, and update the freq list 
        #bucket sort the numbers per count

        #make result arr
        #decrement from end of freq(most occurence) and add to result until result is at k len

        count = {}
        freq = [[]for i in range(len(nums)+1)]

        for n in nums:
          count[n] = 1 + count.get(n,0) #default case

        for n, c in count.items():
          freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1):
          for n in freq[i]: #for the numbers at count index (should be the highest)
            res.append(n)
            if len(res) == k: 
              return res