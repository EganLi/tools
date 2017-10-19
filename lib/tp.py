#!/usr/bin/python

import configparser

def readConfig(path):
    cf = configparser.ConfigParser()
    cf.read(path)

    USER_NUM = cf.sections()
    LEN = len(USER_NUM)
    if LEN == 0:
        print("请确认配置文件正确！")
        return None

    return cf

def selectHost(cf):
    NUM = 0
    
    USER_NUM = cf.sections()
    LEN = len(USER_NUM)

    output = "%-7s |%-18s |%-16s |%-30s" % ('序号', '主机', '用户', '说明')
    print(output)
    for i in range(LEN):
        output = "%-9d |%-20s |%-18s |%-32s" % (i, cf.get(USER_NUM[i], "ip"), cf.get(USER_NUM[i], "user"), cf.get(USER_NUM[i], "comment"))
        print(output)

    strNum = input("请输入要登入的服务器序号：")
    while True:
        if strNum is None:
            NUM = 0
            break
        if strNum == 'q':
            return None
        try:
            NUM = int(strNum)
            if (0 <= NUM and NUM < LEN):
                break
            strNum = input("请输入要登入的服务器序号：")
        except:
            strNum = input("请输入要登入的服务器序号：")
            continue
    return NUM
