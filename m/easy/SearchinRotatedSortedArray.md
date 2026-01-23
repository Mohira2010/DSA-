# 33.Search in Rotated Sorted Array    

- **Murakablik**: Medium
- **Tegishlik Mavzular**: Array, Binary Search

## Masala

- Butun sonlardan iborat nums massivi berilgan, u o‘sish tartibida saralangan va takrorlanmaydigan qiymatlardan iborat.

- Funksiyaga uzatilishidan oldin, nums massivi noma’lum k indeksda (1 ≤ k < nums.length) chap tomonga aylantirilgan (left rotated) bo‘lishi mumkin.

- Natijada massiv quyidagi ko‘rinishga keladi:
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
 (0-indekslash asosida)
Masalan:
[0,1,2,4,5,6,7] massivi 3 indeksga aylantirilsa, u: [4,5,6,7,0,1,2]
ko‘rinishiga keladi.

- nums massivi (aylantirilgandan keyingi holati) va butun son target berilgan.

- 👉 Agar target massiv ichida bo‘lsa — uning indeksini qaytaring,
- 👉 agar bo‘lmasa — -1 qaytaring.

⚠️ Siz O(log n) vaqt murakkabligiga ega algoritm yozishingiz shart.

### Example 1:

- Input: nums = [4,5,6,7,0,1,2], target = 0

- Output: 4


### Example 2:

- Input: nums = [4,5,6,7,0,1,2], target = 3

- Output: -1

### Example 3:

- Input: nums = [1], target = 0

- Output: -1

## Javob-1 (Time: 0 ms, 18 MB)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1    
```

## Javob-2 (Time: 0 ms, 19.4 MB)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        # Binary search
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            return -1    
```