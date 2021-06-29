# coding=utf-8
import configparser


class Configdata:
    def __init__(self, filepath):
        self.filepath = filepath
        cf = configparser.ConfigParser()
        cf.read(self.filepath, encoding="utf-8")
        self.cf = cf

    # 获取config.ini中section的值，以字典格式返回
    def getsectiondict(self, section):
        secdict = {}
        seclist = self.cf.options(section)
        for list in seclist:
            secdict[list] = self.cf.get(section, list)
        return secdict

    # 修改config.ini中item的值
    def setvaluse(self, section, item, value):
        self.cf.set(section, item, value)
        self.cf.write(open(self.filepath, 'w', encoding='utf-8'))
