import xlrd, xlwt, xlutils
from xlutils.copy import copy
import ExcelOperation
import os

class globalFunction:

    def __init__(self):
        self.excel = ExcelOperation.excelOperation()

    def create(self, name):
        # 打开总表
        self.excel.openExcel(r'all_the_sheet.xls')

        # 创建一个表
        workbook = xlwt.Workbook(encoding='ascii')
        workbook.add_sheet('sheet1')

        # 添加表项（第二列的0代表没有删除）
        row_num = self.excel.get_size()[0]
        is_find_delete = False
        # 寻找有没有已经被删除的表项
        for i in range(row_num):
            if self.excel.read_row(i)[1] == 1:
                is_find_delete = True
                self.excel.write_in(i, 0, name)
                self.excel.write_in(i, 1, 0)
                break
        # 如果没找到，在最后写入
        if is_find_delete == False:
            self.excel.write_in(row_num, 0, name)
            self.excel.write_in(row_num, 1, 0)

        # 检测是否文件处于打开状态
        try:
            workbook.save(name)
        except PermissionError:
            print('错误：请关闭文件{}！！！'.format(name))

    def list_word_book(self):
        # 打开总表
        self.excel.openExcel(r'all_the_sheet.xls')
        row_num = self.excel.get_size()[0]

        if row_num == 0:
            print('提示：你还没有单词本。')

        # 只打印那些没有被删除的
        else:
            for i in range(row_num):
                if self.excel.read_row(i)[1] == 0:
                    print(self.excel.read_row(i)[0])

    def delete(self, name):
        # 打开总表
        self.excel.openExcel(r'all_the_sheet.xls')
        row_num = self.excel.get_size()[0]

        # 在总表中写入1表示已删除
        for i in range(row_num):
            if self.excel.read_row(i)[0] == name:
                self.excel.write_in(i, 1, 1)
        try:
            os.remove(name)
        except FileNotFoundError:
            print('错误：没有该文件，请检查是否输入错误！！！')

    def add_word_book(self, name):
        self.excel.openExcel(r'all_the_sheet.xls')

        # 检测文件是否存在
        xlrd.open_workbook(name)

        # 添加表项（第二列的0代表没有删除）
        row_num = self.excel.get_size()[0]
        is_find_delete = False
        # 寻找有没有已经被删除的表项
        for i in range(row_num):
            if self.excel.read_row(i)[1] == 1:
                is_find_delete = True
                self.excel.write_in(i, 0, name)
                self.excel.write_in(i, 1, 0)
                break
        # 如果没找到，在最后写入
        if is_find_delete == False:
            self.excel.write_in(row_num, 0, name)
            self.excel.write_in(row_num, 1, 0)

    # 如果all_the_sheet.xls不存在，那么创建
    def add_all_the_sheet_xls(self):

        if os.path.exists('all_the_sheet.xls') == False:
            # 创建一个表
            workbook = xlwt.Workbook(encoding='ascii')
            workbook.add_sheet('sheet1')
            # 保存
            workbook.save('all_the_sheet.xls')