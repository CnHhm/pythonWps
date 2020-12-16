import os
import shutil
import tempfile
import win32api
import win32print
import win32com.client
import time

path ='E:\\12-15lj'
src_n = 'E:\\12-15lj\\invoice template.xls'
src_bd = 'E:\\12-15lj\\invoice template for BD.xls'
src_n_200 = 'E:\\12-15lj\\invoice template_200.xls'
def get_filelist(dir):
    Filelist = []
    DirList = []
    for home, dirs, files in os.walk(path):
        DirList.append(home)
        for filename in files:
            # 文件名列表，包含完整路径
            Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    return Filelist,DirList

def printFile(filename):
    #example filename = r'E:\12-15lj\开票模板.xls'
    win32api.ShellExecute(
     0,
     "print",
     filename,
     '/d:"%s"' % win32print.GetDefaultPrinter(),
     ".",
     0
    )
    return

def modifyExcel(file,rank,column,str):
    # 打开wps的表格et
    et = win32com.client.Dispatch("Excel.Application")
    # et.Visible = True # 确定ET是否可见
    # file = r'e:\12-15lj\中文路径测试.xls'
    # 打开wps表格文件
    wb = et.Workbooks.Open(file)
    # # 新建一个wps工作簿
    # # wb = et.Workbooks.Add()
    # 打开wps表格文件中的第一张表
    sht = wb.Worksheets(1)
    # 修改单元格的内容
    sht.Cells(rank,column).Value = str
    # 保存文件 另存为命令为workbook.SaveAs()
    wb.Save()
    # 关闭文件
    wb.Close()
    # 退出程序
    et.Quit()
    return
 
if __name__ =="__main__":
    Filelist,DirList = get_filelist(dir)
    print("*************program begin ******************")
    for dir in DirList:
        if os.path.isdir(dir):
            #拷贝标名
            if len(dir.split(os.path.sep)) == 3:
                tenderName = dir.split(os.path.sep)[2]
                if tenderName == '012 模具钢' or tenderName == '013 氟化铝' or tenderName == '019 隔热条（聚酰胺型材）采购':
                    price = 200
                else:
                    price = 100

                print('******************标名：'+tenderName+' price:'+str(price)+'******************')
            #找到各标下的公司文件夹，并拷贝公司名
            if len(dir.split(os.path.sep)) == 5:
                companyName = dir.split(os.path.sep)[4]
                print(companyName)
                #创建output文件夹，并拷贝开票文件.xls
                if os.path.exists(dir+os.path.sep+'output'):
                    print('In '+dir+'already exists output dir')
                else:
                    os.mkdir(dir+os.path.sep+'output')
                dst = dir+os.path.sep+'output'+os.path.sep+'invoice_template.xls'
                #区别公司标和板带标
                if tenderName == 'FJNLBDZZZB2020001-PE保护膜' or tenderName == 'FJNLBDZZZB2020002-纸套筒':
                    shutil.copyfile(src_bd,dst)
                    print('板带模板')
                elif tenderName == '012 模具钢' or tenderName == '013 氟化铝' or tenderName == '019 隔热条（聚酰胺型材）采购':
                    shutil.copyfile(src_n_200,dst)
                    print('公司模板模板_200')               	
                else:
                    shutil.copyfile(src_n,dst)
                    print('公司模板模板')
                #修改公司名
                inner_str = '单位：'+companyName+'            2020 年 12月 16日'
                modifyExcel(dst,2,5,inner_str)
                time.sleep(0.3)
                modifyExcel(dst,15,5,inner_str)
                time.sleep(0.3)
                # if price == 200:
                #     modifyExcel(dst,4,23,price)#标书费
                #     time.sleep(0.3)
                #     modifyExcel(dst,3,36,price/100)#标书费
                #     time.sleep(0.3)
    print('program finish')