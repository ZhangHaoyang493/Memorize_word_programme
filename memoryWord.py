import ExcelOperation
import random

class memoryWord:

    def __init__(self):
        self.excelOp = ExcelOperation.excelOperation()

    def choose_word_book(self, name):
        self.excelOp.openExcel(name)

    def start_memory(self, word_num):
        print('背单词开始，输入q退出背单词。')
        length = self.excelOp.get_size()[0]
        x = [i for i in range(length)]
        x = random.sample(x, word_num)

        for index in x:
            word = self.excelOp.read_row(index)
            print('根据中文释义拼写单词：\n中文释义：')
            print(word[1])
            error_num = 0
            user_input = ''

            while error_num < 3:
                user_input = input('请输入拼写：')

                # 退出机制
                if user_input == 'q':
                    break

                if user_input == word[0]:
                    print('拼写正确！')
                    break
                else:
                    error_num += 1

            if user_input == 'q':
                print('提示：背单词结束。')
                break

            if error_num == 3 and user_input != word[0]:
                print('正确答案：', word[0])

    def go_default(self):
        self.excelOp.go_default()



