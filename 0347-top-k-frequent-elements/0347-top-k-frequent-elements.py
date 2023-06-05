class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i],0)
        print(freq)
        freq = {k: v for k, v in sorted(freq.items(), reverse = True, key=lambda item: item[1])}
        print(freq)

        return list(freq.keys())[:k]