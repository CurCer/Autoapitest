# coding=utf-8
import json


from request.baserequest import BaseRequest
from until.condigdata import Configdata
from until.getexcldata import Getexcldata

filname = 'D:/file/pyt/Autoapitest/testdata/test.xlsx'
filepath = 'D:/file/pyt/Autoapitest/config/config.ini'
values = None
excldata = Getexcldata(filname)
rowxnome = excldata.getcases()
print("表格路径：", filname)
print("执行用例数：", rowxnome-1)
for i in range(2, rowxnome+1):
    isrun = excldata.getisrun(i)
    if isrun:
        # 表格结果初始化
        excldata.writeresult(i, None)
        excldata.writeispass(i, None)

        caseid = excldata.getcaseid(i)
        requestname = excldata.getrequestname(i)
        url = excldata.geturl(i)
        method = excldata.getmethod(i)
        data = json.loads(excldata.getdata(i))
        expect = excldata.getexpect(i)
        header = Configdata(filepath).getsectiondict("hzxzhxyheader")
        # 验证token的时候重新给data赋值
        if requestname == "验证token":
            data = Configdata(filepath).getsectiondict("hzxzhxy")

        rsp = BaseRequest.dorequest(method, url, data, header)
        jsonrsp = rsp.json()
        strsp = json.dumps(jsonrsp, ensure_ascii=False)
        excldata.writeresult(i, strsp)
        try:
            assert expect in strsp
            excldata.writeispass(i, "PASS")
            print('\033[0;32m 用例编号:%s,执行成功 \033[0m'%(caseid))
        except Exception as e:
            excldata.writeispass(i, "FAIL")
            print('\033[0;31m 用例编号:%s,执行失败 \033[0m'%(caseid))
        # 取得token后,取出token值
        if requestname == "获取token" and rsp.status_code == 200:
            values = "Bearer {}".format(jsonrsp["access_token"])
            Configdata(filepath).setvaluse("hzxzhxy", "token", jsonrsp["access_token"])

        elif requestname == "验证token" and rsp.status_code == 200:
            Configdata(filepath).setvaluse("hzxzhxyheader", "Authorization", values)

# 初始化authorization和token
Configdata(filepath).setvaluse("hzxzhxyheader", "Authorization", " ")
Configdata(filepath).setvaluse("hzxzhxy", "token", " ")
