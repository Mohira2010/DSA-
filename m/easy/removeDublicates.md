# 26. Remove Duplicates from Sorted Array

- **Murakablik**: Easy
- **Tegishlik Mavzular**: Array, Two Pointers

## Masala

- Butun sonlardan iborat [nums] massivi berilgan.
U kamaymaydigan tartibda (sorted) joylashtirilgan.

- Sizning vazifangiz —
takroriy elementlarni joyida (in-place) olib tashlash, shunda har bir noyob son faqat bir marta qoladi.
Elementlarning ketma-ketligi o‘zgarmasligi kerak.

- [nums] ichidagi noyob (unique) elementlar sonini [k] deb hisoblang.
Takroriylar olib tashlangandan so‘ng, [k] ni qaytaring.

- nums massivining birinchi [k] ta elementi faqat noyob sonlardan iborat bo‘lishi kerak va tartiblangan holatda qoladi

- k - 1 indeksidan keyingi elementlar hisobga olinmaydi (e’tiborga olinmaydi).

### Example 1:

Input: nums = [1,1,2]

Output: 2, nums = [1,2,_]

Explanation: Sizning funksiyangiz k = 2 ni qaytarishi kerak,
va [nums] massividagi birinchi ikki element mos ravishda 1 va 2 bo‘lishi kerak.

Qaytarilgan k dan keyingi elementlar muhim emas (shuning uchun ular _ bilan ifodalanadi).

### Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]

Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation: Sizning funksiyangiz k = 5 ni qaytarishi kerak,
va nums massividagi birinchi besh element mos ravishda 0, 1, 2, 3 va 4 bo‘lishi kerak.

## Javob-1 (Time: 29 ms, 8.1 MB)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[m]:
                m += 1
                nums[m] = nums[i]
        return m + 1  
```
