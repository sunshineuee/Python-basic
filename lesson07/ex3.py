import os
import shutil

my_dir = 'task3'

root_ = r'my_project'
dir_ = 'templates'

for root, dirs, files in os.walk(root_):
    if dir_ in dirs and root != root_:
        for i in os.listdir(os.path.join(root, dir_)):
            try:
                shutil.copytree(os.path.join(root, dir_, i),
                                os.path.join(root_, dir_, i))
            except FileExistsError:
                print('Уже')
