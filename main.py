import os
import time
import shutil
import zipfile


start_time = time.time()


root_path = r'\\192.168.1.40\All\Сотниченко А.Д\programs'
objects = root_path + r'\extract_files\list.txt'
dir_fom = root_path + r'\extract_files\from'
dir_to = root_path + r'\extract_files\to'
ext = '.zip'


d_file_path = {'_'.join(file.split(':')): dir_fom + os.sep + file for file in os.listdir(dir_fom)}
with open(objects) as inf:
    li_files = list(map(lambda x: '_'.join(x.split(':')) + ext, inf.read().split('\n')))
shutil.rmtree(dir_to)
for file in li_files:
    if d_file_path.get(file):
        zip_object = zipfile.ZipFile(d_file_path[file])
        zip_object.extractall(dir_to)


print("--- %s seconds ---" % (time.time() - start_time))