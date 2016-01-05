import xlrd
import xlwt
from datetime import date,datetime
from xlrd.xldate import xldate_as_datetime

def  read_excel():
    #打开文件
    book=xlrd.open_workbook('demo.xlsx')
    #获取所有的sheet
    print(book.sheet_names())
    sheet2_name=book.sheet_names()[1]
    #根据sheet索引或者名称获取内容
    sheet2=book.sheet_by_index(1)
    sheet2=book.sheet_by_name('Sheet2')
    #sheet的名称，行数，列数
    print(sheet2.name,sheet2.nrows,sheet2.ncols)
    
    #获取整行和整列的值
    rows=sheet2.row_values(3)
    cols=sheet2.col_values(2)
    print(rows)
    print(cols)
    #获取单元格内容
    print(sheet2.cell(1,0).value)
    print(sheet2.cell_value(1,0))
    print(sheet2.row(1)[0].value)
    #ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    #获取单元格内容的数据类型
    print(sheet2.cell(2,2).ctype)
    print(sheet2.cell(2,1).ctype)
    print(sheet2.cell(2,0).ctype)
    print(sheet2.cell(2,4).ctype)
    print(sheet2.cell(2,2).ctype)
    date_value=xlrd.xldate_as_tuple(sheet2.cell_value(2,2), book.datemode)
    date1=xldate_as_datetime(sheet2.cell_value(2,2), book.datemode)
    print(date1)
    print(date_value)
    for i in range(sheet2.nrows):
        r=sheet2.col_values(4)[i]
        print(r)
if __name__=='__main__':
    read_excel()