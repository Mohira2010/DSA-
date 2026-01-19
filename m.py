x = 'pwwkew'
window = ''
left = 0
max_len = 0

for r in range(len(x)):
    if x[r] not in window:
        window += x[r]
    else:
        while x[r] in window:
            window = window[1:] 
        window += x[r]
    max_len = max(max_len, len(window))
print(max_len) 