def right_shift(n, d):
    return (n >> d)|(n << (32 - d)) & 0xFFFFFFFF
n = 60
d = 2
print(right_shift(n, d))
