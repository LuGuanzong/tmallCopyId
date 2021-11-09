import xlrd
from xlutils.copy import copy


# 打开表格准备读取
def open_read_xls():
    import os
    if os.path.exists('springLoveShi.xls'):
        path = 'springLoveShi.xls'
    else:
        path = 'springLoveShi.xlsx'
    workbook = xlrd.open_workbook(path, encoding_override='utf-8')
    print('-----------------------------------------------')
    print(f'一共有{workbook.sheets()[0].nrows}行数据')
    print('-----------------------------------------------')
    return workbook


# 读取指定行的订单号
def read_order(sheet, row):
    if not sheet.cell_value(row, 8):
        if sheet.cell_value(row, 0):
            return sheet.cell_value(row, 0)
    print(f'第{row+1}行不需要填入数据.')
    return 0


# 将xlrd读取的对象转为xlwt可操作对象
def open_write_xls(workbook):
    sheet = copy(workbook)
    return sheet


# 把id写入指定行
def write_id(sheet, row, id_number):
    sheet.get_sheet(0).write(row, 8, id_number)
    print(f'第{row+1}行数据写入完毕.')


# 保存表格
def safe_xls(sheet):
    sheet.save("身份证号码提取.xlsx")  # 保存工作簿
