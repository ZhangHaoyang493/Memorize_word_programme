class strHandle:

    def __init__(self):
        return

    # 判断一个字符是否是字母
    def isAlpha(self, c):
        if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            return True
        return False

    def handleMeaning(self, str):
        # 没有词性，则为词组，意思无需分割，直接返回
        if (str.find('.') == -1):
            return str

        # 返回的字符串
        ret, ret1 = '', ''
        ret = str

        # 将不同的词性分行，根据'.'的位置
        i = 0
        ret1 = ret
        ret = ''
        ret1 = ret1.split('.')
        ret += (ret1[0] + '.')

        for i in range(1, len(ret1) - 1):
            ind1 = len(ret1[i]) - 1
            while self.isAlpha(ret1[i][ind1]):
                ind1 -= 1
            ret += (ret1[i][:ind1 + 1] + '\n')
            ret += (ret1[i][ind1 + 1:] + '.')

        ret += ret1[len(ret1) - 1]

        return ret