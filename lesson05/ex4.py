src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([n for i,n in enumerate(src) if i > 0 and n > src[i-1]])