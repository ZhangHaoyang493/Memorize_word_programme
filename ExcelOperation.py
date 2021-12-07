import xlrd, xlwt, xlutils
from xlutils.copy import copy
import getMeaning
import strHandler

# 使用该库时记得关掉要操作的文件，否则要报错

strH = strHandler.strHandle()
getM = getMeaning.getMeaning()

class excelOperation:

    def __init__(self):
        self.name = None



    # 打开一个表
    def openExcel(self, name):
        self.name = name

        xlrd.open_workbook(name)

    # 获得表的大小
    def get_size(self):
        temp = xlrd.open_workbook(self.name).sheet_by_index(0)

        return (temp.nrows, temp.ncols)

    # 添加单词
    def add_word(self, word):
        row, col = self.get_size()
        mean = strH.handleMeaning(getM.require(word))
        # workBook = copy(self.name)
        # 报错：AttributeError: 'str' object has no attribute 'datemode'
        # 修改：
        workBook = copy(xlrd.open_workbook(self.name))
        sheet = workBook.get_sheet(0)

        # 写入数据
        sheet.write(row, 0, word)
        sheet.write(row, 1, mean)

        # 保存并覆盖
        try:
            workBook.save(self.name)
        except PermissionError:
            print('错误：请关闭文件{}！！！'.format(self.name))

    # 向索引i, j处写入信息(info)
    def write_in(self, i, j, info):
        workBook = copy(xlrd.open_workbook(self.name))
        sheet = workBook.get_sheet(0)
        # 写入
        sheet.write(i, j, info)
        # 保存并覆盖
        try:
            workBook.save(self.name)
        except PermissionError:
            print('错误：请关闭文件{}！！！'.format(self.name))

    # 读取第i行的数据，返回对应的list
    def read_row(self, i):
        sheet = xlrd.open_workbook(self.name).sheet_by_index(0)
        return sheet.row_values(i)

    # 读取第i列的数据，返回对应的list
    def read_col(self, i):
        sheet = xlrd.open_workbook(self.name).sheet_by_index(0)
        return sheet.col_values(i)

    # 清空表（重新创建一个表覆盖原来的）
    def clear_sheet(self):
        # 创建一个表
        workbook = xlwt.Workbook(encoding='ascii')
        workbook.add_sheet('sheet1')
        # 检测是否文件处于打开状态
        try:
            workbook.save(self.name)
        except PermissionError:
            print('错误：请关闭文件{}！！！'.format(self.name))

    # 列出所有表项
    def list_word(self):
        # 打开表
        sheet = xlrd.open_workbook(self.name).sheet_by_index(0)
        rows = self.get_size()[0]

        if rows == 0:
            print('提示：该单词本中还没有单词。')
        else:
            for i in range(rows):
                print('{}\n{}'.format(self.read_row(i)[0], self.read_row(i)[1]))

    # 恢复默认
    def go_default(self):
        self.name = None
