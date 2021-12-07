class help:

    def __init__(self):
        return

    def copyright(self):
        print('WORD KILLER [版本 1.0.0]')
        print('copyright@ Zhy。保留所有权利。')
        print('输入 h 查看帮助文档。')

    def help(self):
        print('主要命令：\n'
              '1. (list)：列出现在已有的单词本。\n'
              '2. (create 单词本名字)：创建一个新的单词本，名字是输入的名字，名字结尾要为.xls。\n'
              '3. (lookup)：输入该命令后进入查单词模式，输入单词进行查询。\n'
              '4. (activate 单词本名字)：激活某一个单词本。\n'
              '5. (addwordbook 单词本名字)：添加一个单词本。\n'
              '6. (addword 单词)：添加一个单词。\n'
              '7. (memory 单词数量)：在激活的单词本上记单词，记得输入想要背的单词数量。\n'
              '8. (delete 单词本名字)：删除一个单词本。\n'
              '9. (listword)：列出现在激活的单词本上的单词。\n'
              '10. (clear)：清空现在激活的单词本。\n'
              '11. (activate default)：回到默认单词本（无单词本）')