import xlrd
from xlutils.styles import Styles

def read_excel():

    wb = xlrd.open_workbook(filename="test.xls", formatting_info=True)    #打开文件
    style = Styles(wb)

    sheet = wb.sheet_by_index(0)
    cell = sheet.cell(0, 0)
    print("cell.xf_index is %d" % cell.xf_index)
    fmt = wb.xf_list[cell.xf_index]
    print("type(fmt) is %s" % type(fmt))
    print("fmt.dump():")
    fmt.dump()

    # https://xlutils.readthedocs.io/en/latest/styles.html
    print(style[sheet.cell(0, 0)])
    print(style[sheet.cell(0, 0)].xf)


if __name__ == '__main__':
    read_excel()