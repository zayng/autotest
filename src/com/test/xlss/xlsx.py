import xlwt
import xlrd

book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('new', cell_overwrite_ok=True)
# sheet1=book.add_sheet('new1', cell_overwrite_ok=True)
sheet.write(0, 0, '根节点')
sheet.write(0, 1, '节点')
sheet.write(0, 2, '子节点')
sheet.write(1, 0, '储备认证管理')
sheet.write(1, 1, '认证管理')
sheet.write(1, 2, '认证开班管理')
# sheet.write(2, 0, 'fuck')
# sheet.write(2, 1, '星期一')
# sheet.write(2, 2, '星期二')
# sheet1.write(0,0,'fuck')
# sheet1.write(0,1,'星期一')
# sheet1.write(0,2,'星期二')
# sheet1.write(0,3,'星期三')
book.save('menus.xls')

# fname = "menus.xlsx"
# bk = xlrd.open_workbook(fname)
# # shs=bk.sheets()
# shname = bk.sheet_names()
# sh = bk.nsheets
# rsheet = bk.sheet_by_name(shname[0])
# rows = rsheet.nrows
# cols = rsheet.ncols
# value = rsheet.cell_value(0, 1)
# row_list = []
# for row in range(0, rows):
#     values = rsheet.row_values(row)
#     row_list.append(values)
# print("nrows:%d,nols:%d" % (rows, cols))
# print(shname, sh)
# print(value)
# print(row_list)
