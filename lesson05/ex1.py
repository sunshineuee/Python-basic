def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


n = 15
odd_to_n = odd_nums(n)
for i in range(n//2+1):
    print(next(odd_to_n))


