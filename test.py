# # import zipfile
# import shutil


# target = r"D:\project\pythonWps\public\output"
# output_filename = r"D:\project\pythonWps\public"
# shutil.make_archive（output_filename，“zip”，target）

import shutil
# 将path_1处的文件归档到path_2处
path_1 = r"D:\project\pythonWps\public\output"
path_2 = r"D:\project\pythonWps\public\download"
new_path = shutil.make_archive(path_2, 'zip', path_1)
print(new_path)