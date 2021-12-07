import xlrd, xlwt, xlutils

import getMeaning
import strHandler
import ExcelOperation
import memoryWord
import globalFun
import help

getMeaning = getMeaning.getMeaning()
strH = strHandler.strHandle()
excel = ExcelOperation.excelOperation()
memoryW = memoryWord.memoryWord()
globalF = globalFun.globalFunction()
helper = help.help()

activate_file_name = 'No Word Book'
helper.copyright()

# 判断是否有all_the_sheet.xls，没有则添加
globalF.add_all_the_sheet_xls()

while True:
    cmd = input('({}) >>> '.format(activate_file_name))

    cmd1 = cmd.split(' ')
    cmd = []
    for ele in cmd1:
        if ele != '':
            cmd.append(ele)

    if cmd == []:
        continue

    elif cmd[0] == 'create':
        if activate_file_name != 'No Word Book':
            print('错误：该命令不可以对特定单词本操作！！！')
            continue
        globalF.create(cmd[1])
        print('提示：创建成功。')

    elif cmd[0] == 'list':
        if activate_file_name != 'No Word Book':
            print('错误：该命令不可以对特定单词本操作！！！')
            continue
        globalF.list_word_book()

    elif cmd[0] == 'lookup':
        print('提示：进入查单词或词组模式（输入q退出）')
        while True:
            word = input('(Look Up) > ')
            if word == 'q':
                break
            else:
                try:
                    print(strH.handleMeaning(getMeaning.require(word)))
                except IndexError:
                    print('提示：该单词或词组不存在。')
                    continue

    elif cmd[0] == 'activate':
        try:
            if cmd[1] == 'default':
                activate_file_name = 'No Word Book'
                excel.go_default()
                memoryW.go_default()
            else:
                excel.openExcel(cmd[1])
                memoryW.choose_word_book(cmd[1])
                activate_file_name = cmd[1]
        except FileNotFoundError:
            print('错误：没有该文件！！！')

    elif cmd[0] == 'addword':
        if activate_file_name == 'No Word Book':
            print('错误：请选择单词本进行操作！！！')
            continue
        try:
            excel.add_word(cmd[1])
            print('提示：成功添加单词{}。'.format(cmd[1]))
        except IndexError:
            print('提示：该单词或词组不存在。')

    elif cmd[0] == 'addwordbook':
        if activate_file_name != 'No Word Book':
            print('错误：该命令不可以对特定单词本操作！！！')
            continue
        try:
            globalF.add_word_book(cmd[1])
            print('提示：成功添加单词本{}。'.format(cmd[1]))
        except FileNotFoundError:
            print('错误：文件不存在！！！')

    elif cmd[0] == 'memory':
        if activate_file_name == 'No Word Book':
            print('错误：请选择单词本进行操作！！！')
            continue
        memoryW.start_memory(eval(cmd[1]))

    elif cmd[0] == 'delete':
        if activate_file_name != 'No Word Book':
            print('错误：该命令不可以对特定单词本操作！！！')
            continue
        globalF.delete(cmd[1])
        print('提示：已删除单词本{}。'.format(cmd[1]))

    elif cmd[0] == 'listword':
        if activate_file_name == 'No Word Book':
            print('错误：请选择单词本进行操作！！！')
            continue
        excel.list_word()

    elif cmd[0] == 'clear':
        if activate_file_name == 'No Word Book':
            print('错误：请选择单词本进行操作！！！')
            continue
        excel.clear_sheet()
        print('提示：已清空单词本{}。'.format(activate_file_name))

    elif cmd[0] == 'h':
        helper.help()

    else:
        print('错误：没有该指令！！！')