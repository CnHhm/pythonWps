from mmap import mmap,ACCESS_READ
from xlrd import open_workbook 

# print(open_workbook('simple2.xls')

print("test")
with open("simple2.xls",'rb') as file:
    data = file.read()

# with open('simple2.xls','rb') as f:
# 	print(open_workbook(file_contents = mmap(f.fileno(),0,access=ACCESS_READ)))

# aString = open('simple2.xls','rb').read()
# print(open_workbook(file_contents = aString))