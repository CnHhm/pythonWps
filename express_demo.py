# 0. 删除原output文件夹,创建新output文件夹
# 1. 复制 public\template的文件到output文件夹下
# 2. 遍历文件夹下所有docx文件，替换关键字
# 3. 打包 output文件夹

import os
import shutil

# 0.删除output 文件夹
filepath = r"D:\project\pythonWps\public\output"
if os.path.exists(filepath):
    shutil.rmtree(filepath,True)
    print("dir "+ str(filepath)+ " removed!")
else:
    print("dir "+ str(filepath) + " not exist.")

# 0.创建output 文件夹
os.mkdir(filepath)
print("dir "+ str(filepath) + " create.")

# 1.复制 public\template的文件到output文件夹下
src = r"D:\project\pythonWps\public\template"
dst = r"D:\project\pythonWps\public\output"

def get_filelist(dir):
    Filelist = []
    DirList = []
    for home, dirs, files in os.walk(dir):
        # DirList.append(home)
        for filename in files:
            # 文件名列表，包含完整路径
            if os.path.isfile(os.path.join(home, filename)):
                DirList.append(os.path.join(home, filename))
                print(os.path.join(home, filename))
            # 文件名列表，只包含文件名
            Filelist.append( filename)
    return Filelist,DirList

Result = get_filelist(src)
# print(DirList)
# for filename,Dir in Filelist:
#     print('1')
#     shutil.copyfile(Dir,s.path.join(dst,filename))