from fromSelenium import get_id, takeover_browser, open_browser
from manageXlsl import open_read_xls, open_write_xls, read_order, write_id, safe_xls
from fromSelenium.getWarm import getSentence

import time


def manipute(driver):
    workbook = open_read_xls()
    sheet_for_read = workbook.sheets()[0]
    sheet_for_write = open_write_xls(workbook)
    rows = sheet_for_read.nrows

    for row in range(rows):
        order_id = read_order(sheet_for_read, row)
        if order_id:
            id_number = get_id(driver, order_id)
            write_id(sheet_for_write, row, id_number)
    safe_xls(sheet_for_write)

    print('完成啦！小爱姐天天开心噢 (*^▽^*) ')
    print('--------------------------------')
    print('--------------------------------')
    print('--------------------------------')


if __name__ == '__main__':
    print("------------------------------------")
    print("------------------------------------")
    getSentence()
    print("------------------------------------")
    print("------------------------------------")
    print('')
    print('准备开始程序了喔~~~')
    print('')
    open_browser()
    time.sleep(0.5)
    driver = takeover_browser()
    time.sleep(0.5)
    input('请登录后在此窗口点击Enter键：')
    manipute(driver)

