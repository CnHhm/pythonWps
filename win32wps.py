# import win32com.client
# #新建WPS进程<br />
# #wps、et、wpp对应的是金山文件、表格和演示<br />
# #word、excel、powerpoint对应的是微软的文字、表格和演示<br />
# wpsApp=win32com.client.Dispatch("kwps.Application")
# wpsApp.Visible=~False

import win32com.client

# 打开wps的表格et
et = win32com.client.Dispatch("Excel.Application")
et.Visible = True # 确定ET是否可见
file = r'e:\12-15lj\中文路径测试.xls'
# 打开wps表格文件
wb = et.Workbooks.Open(file)
# # 新建一个wps工作簿
# # wb = et.Workbooks.Add()
# 打开wps表格文件中的第一张表
sht = wb.Worksheets(1)
# 修改单元格的内容
string = "福建省游泳馆"
sht.Cells(2, 5).Value = '单位：'+string+'            2020 年 12月 16日'
# 保存文件 另存为命令为workbook.SaveAs()
wb.Save()
# 关闭文件
wb.Close()
# 退出程序
et.Quit()