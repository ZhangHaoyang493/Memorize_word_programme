from bs4 import BeautifulSoup
import requests

class getMeaning:

    def __init__(self):
        self.url = 'https://www.iciba.com/word?w='

        # 单词和词组的标释义的类名
        self.class_lable = '.Mean_part__1Xi6p'

        # 头部字段，没有的话爬取不了内容，应该是网站有爬虫的防止措施
        self.headers = {
            'Cookie': 'OCSSID=4df0bjva6j7ejussu8al3eqo03',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }

    def require(self, word):

        if word.find(' ') != -1:
            word1 = word.split(' ')
            word = ''

            # 重新拼接成为合适的url，并去掉多余的空格
            for ele in word1:
                if ele != '':
                    word += ele
                    word += '%20'
            word = word[:len(word) - 3]

        r = requests.get(self.url + word, headers=self.headers)

        soup = BeautifulSoup(r.text, 'lxml')

        # 单词释义模块的类名：Mean_normal__1OOyX
        # 通过类名查找单词释义的位置
        return soup.select(self.class_lable)[0].text