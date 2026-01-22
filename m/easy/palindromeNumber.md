# 9. Palindrome Number

- **Murakablik**: Easy
- **Tegishlik Mavzular**: Math, Two Pointers

## Masala

- Berilgan butun son [x] agar palindrome bo‘lsa [true] ni, aks holda [false] ni qaytaring.

- Palindrome — bu oldindan va orqadan o‘qilganda bir xil bo‘ladigan son yoki so‘z.

### Example 1:

- Input: x = 121

- Output: true

- Explanation: 121 chapdan o‘ngga ham, o‘ngdan chapga ham o‘qilganda 121 bo‘lib qoladi.

### Example 2:

- Input: x = -121

- Output: false

- Explanation: Chapdan o‘ngga o‘qilganda u −121 bo‘ladi. O‘ngdan chapga o‘qilganda esa 121− ga aylanadi. Shuning uchun u palindrome emas.

### Example 3:

- Input: x = 10

- Output: false

- Explanation: O‘ngdan chapga o‘qilganda u 01 bo‘ladi. Shuning uchun u palindrome emas.
## Javob-1 (Time: 3ms, 18 MB)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else: return False        
```

## Javob-2 (Time: 19 ms, 19.41 MB)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = 0
        r = len(x) - 1
        while l < r:
            if len(x) == 1:
                return True
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True      
```