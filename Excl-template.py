import xlrd
from xlutils.filter import process, XLRDReader, XLWTWriter
 
rb = xlrd.open_workbook('test.xls', formatting_info=True)
table = rb.sheets()[0]
print(table.cell(9,2))
# 参考xlutils.copy库内的用法 参考xlutils.filter内的参数定义style_list
w = XLWTWriter()

process(XLRDReader(rb, 'unknown.xls'), w)
wb = w.output[0][1]
style_list = w.style_list

for n, sheet in enumerate(rb.sheets()):
    print('n:'+str(n));
    print('sheet:'+str(sheet));
    sheet2 = wb.get_sheet(n)
    for r in range(sheet.nrows):
        for c, cell in enumerate(sheet.row_values(r)):
            style = style_list[sheet.cell_xf_index(r, c)]
            if table.cell(r,c) == 66:
                sheet2.write(r, c, 'no problem sir', style)
wb.save('save.xls')
print("done")