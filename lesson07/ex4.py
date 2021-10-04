import os
from collections import defaultdict

files_ = defaultdict(int)
for root, dirs, files in os.walk('./'):
    for f in files:
        size = 10 ** len(str(os.stat(os.path.join(root, f)).st_size))
        files_[size] += 1

for s, n in sorted(files_.items())[:15]:
    print(f'{s}: {n}')
