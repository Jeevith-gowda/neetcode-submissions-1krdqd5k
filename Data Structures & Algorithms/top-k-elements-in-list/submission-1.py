class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1 - count frequency
        count = {}
        for i in nums:
            if i in count:
                count[i] = count[i] + 1
            else:
                count[i] = 1

        # Step 2 - sort by frequency
        sorted_keys = sorted(count, key=count.get)

        # Step 3 - return top k
        return sorted_keys[-k:]