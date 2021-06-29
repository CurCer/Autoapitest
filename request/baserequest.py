# coding=utf-8
import requests


class BaseRequest:
    # POST方法
    @staticmethod
    def dopost(url, data, header):
        respone = requests.post(url=url, data=data, headers=header)
        return respone

    # GET方法
    @staticmethod
    def doget(url, data, header):
        respone = requests.get(url=url, params=data, headers=header)
        return respone

    # 执行请求
    @staticmethod
    def dorequest(method, url, data, header):
        result = None
        try:
            if method.upper() == "GET":
                result = BaseRequest.doget(url, data, header)
            elif method.upper() == "POST":
                result = BaseRequest.dopost(url, data, header)
            return result
        except Exception as e:
            print("调用主函数失败：{}".format(e))

