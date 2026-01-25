81. Search in Rotated Sorted Array II

- **Murakablik**: Medium
- **Tegishlik Mavzular**: Array, Binary Search

## Masala

- nums — butun sonlardan iborat massiv, u kamaymaydigan tartibda (o‘sish tartibida, lekin qiymatlar bir xil bo‘lishi ham mumkin) saralangan.

- Funksiyaga uzatilishidan oldin, nums noma’lum k indeksida aylantirilgan (rotated)
(0 ≤ k < nums.length), natijada massiv quyidagi ko‘rinishga keladi:
-- [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indeksdan boshlab).

- Masalan: [0,1,2,4,4,4,5,6,6,7]
massivi k = 5 indeksida aylantirilsa, u quyidagicha bo‘ladi:
[4,5,6,6,7,0,1,2,4,4]

- Aylantirilgandan keyingi nums massivi va target butun soni beriladi.

👉 Agar target nums ichida mavjud bo‘lsa, true qaytaring,
👉 aks holda — false.

📌 Umumiy bajariladigan amallar sonini imkon qadar kamaytirish talab qilinadi.

### Example 1:

- Input: nums = [2,5,6,0,0,1,2], target = 0

- Output: true

### Example 2:

- Input: nums = [2,5,6,0,0,1,2], target = 3

- Output: false

## Javob-1 (Time: 0 ms, 19.54 MB)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
```

## Javob-2 (Time: 0 ms, 18.27 MB)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in nums:
            return True
        else:
            return False
```

## Javob-3 (Time: 0 ms, 19.74 MB)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
```
