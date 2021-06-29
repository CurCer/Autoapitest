# coding=utf-8


class Exclconfig:
    case_id = 1
    request_name = 2
    is_run = 3
    url = 4
    method = 5
    data = 6
    expect = 7
    result = 8
    is_pass = 9

def get_case_id():
    return Exclconfig.case_id

def get_request_name():
    return Exclconfig.request_name

def get_is_run():
    return Exclconfig.is_run

def get_url():
    return Exclconfig.url

def get_method():
    return Exclconfig.method

def get_data():
    return Exclconfig.data

def get_expect():
    return Exclconfig.expect

def get_result():
    return Exclconfig.result

def get_is_pass():
    return Exclconfig.is_pass