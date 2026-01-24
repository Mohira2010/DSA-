# 66. Plus One

- **Murakablik**: Easy
- **Tegishlik Mavzular**: Array, Math   

## Masala

- Sizga katta butun son berilgan, u butun sonlar ro‘yxati (digits) sifatida ifodalangan. Bu yerda digits[i] — sonning i-chi raqami. Raqamlar eng yuqori tartibdan eng past tartibgacha, chapdan o‘ngga qarab joylashgan. Katta butun son oldida hech qanday 0 yo‘q.

- Sizning vazifangiz: ushbu katta butun sonni 1 ga oshiring va natijani raqamlar ro‘yxati (digits) sifatida qaytaring.


### Example 1:

- Input: digits = [1,2,3]

- Output: [1,2,4]

- Explanation: Massiv 123 butun sonini ifodalaydi.
1 ga oshirish 123 + 1 = 124 ga teng bo‘ladi.
Shuning uchun natija [1,2,4] bo‘lishi kerak.


### Example 2:

- Input: digits = [4,3,2,1]

- Output: [4,3,2,2]

- Explanation: Massiv 4321 butun sonini ifodalaydi.
1 ga oshirish 4321 + 1 = 4322 ga teng bo‘ladi.
Shuning uchun natija [4,3,2,2] bo‘lishi kerak.

### Example 3:

- Input: digits = [9]

- Output: [1,0]

- Explanation: Massiv 9 butun sonini ifodalaydi.
1 ga oshirish 9 + 1 = 10 ga teng bo‘ladi.
Shuning uchun natija [1,0] bo‘lishi kerak.

## Javob-1 (Time: 0 ms, 17.62 MB)

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m = len(digits)
        for i in range(m - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
```

## Javob-2 (Time: 0 ms, 19.3 MB)

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m = ''.join(map(str, digits))
        d = [int(d) for d in str(int(m) + 1)]
        return d
```