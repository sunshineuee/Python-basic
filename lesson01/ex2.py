inputlist = [(2 * i - 1) ** 3 for i in range(1, 501)]
# print(inputlist)
result = []
for i in inputlist:
    clist = [i % (10 ** j) // (10 ** (j - 1)) for j in range(1, 11)]
    if sum(clist) % 7 == 0:
        result.append(i)
# print(result)
print(sum(result))

inputlist = [i + 17 for i in inputlist]
# print(inputlist)
result = []
for i in inputlist:
    clist = [i % (10 ** j) // (10 ** (j - 1)) for j in range(1, 11)]
    if sum(clist) % 7 == 0:
        result.append(i)
# print(result)
print(sum(result))
