# coding=utf-8
from until.exclconfig import *
from until.excldata import Excldata


class Getexcldata:
    def __init__(self, filename):
        self.filename = filename
        self.table = Excldata(self.filename)

    # 获取用例个数
    def getcases(self):
        return self.table.getrow()

    # 获取用例编号
    def getcaseid(self, row):
        colnum = get_case_id()
        return self.table.getcellvalue(row, colnum)

    # 获取模块名
    def getrequestname(self, row):
        colnum = get_request_name()
        return self.table.getcellvalue(row, colnum)

    # 获取是否执行
    def getisrun(self, row):
        colnum = get_is_run()
        return self.table.getcellvalue(row, colnum)

    # 获取地址
    def geturl(self, row):
        colnum = get_url()
        return self.table.getcellvalue(row, colnum)

    # 获取方法
    def getmethod(self, row):
        colnum = get_method()
        return self.table.getcellvalue(row, colnum)

    # 获取数据
    def getdata(self, row):
        colnum = get_data()
        return self.table.getcellvalue(row, colnum)

    # 获取预期结果
    def getexpect(self, row):
        colnum = get_expect()
        return self.table.getcellvalue(row, colnum)

    # 写入实际结果
    def writeresult(self, row, value):
        colnum = get_result()
        return self.table.writecellvalue(row, colnum, value)

    # 写入是否通过
    def writeispass(self, row, value):
        colnum = get_is_pass()
        return self.table.writecellvalue(row, colnum, value)