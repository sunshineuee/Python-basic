def odd_nums(n):
    return (i for i in range(n + 1) if i % 2 != 0)


n = 15
odd_to_n = odd_nums(n)
for i in range(n//2+1):
    print(next(odd_to_n))