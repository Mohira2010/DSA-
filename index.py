class Solution:
    """
    Two Sum masalasi:
    Berilgan nums listi va target, ikkita indexni topish kerak
    ular yig‘indisi target ga teng bo‘lsin.
    """

    # 1-usul
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # 2-usul: Two pointers (faqat sorted list bo‘lsa ishlaydi)
    def twoSum_two_pointers(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            x = nums[left] + nums[right]
            if x == target:
                return [left, right] 
            elif x < target:
                left += 1
            else:
                right -= 1
        return []
