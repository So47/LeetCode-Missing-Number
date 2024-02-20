class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        ## O(n×m) looking up in a list is depending on m numbers 
        # for i in range(n+1):
        #    if i not in nums:
        #       return i

        
        # # Sets in Python are implemented as hash tables, which generally provide O(1) average time complexity for membership checks.
        # numSet = set(nums)  # Convert list to set for O(1) average lookup time
        # for i in range(n+1):
        #     if i not in numSet:
        #         return i

        # # This is O(n) + O(n) + O(n)+ O(1) = O(n) but space complexity is also O(n) for storing the whole list
        # default_list = list(range(n+1))
        # return sum(default_list) - sum(nums)

        '''
        Space Efficiency: This approach does not require additional data structures,
        making it very space-efficient.
        Time Complexity: The time complexity is 
        O(n) primarily due to the single pass required to calculate the actual_sum.
        The calculation of expected_sum is O(1).
        '''
        expected_sum = n * (n+1)//2
        return expected_sum - sum(nums)
