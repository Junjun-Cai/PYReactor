# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：jason字串的编码与解析单元测试。
# 作者：ColeCai-蔡君君
# 文件：json_unit_test.py
# 日期：2016/10/11-14:11
# 版本：1.0.0
# 环境：python 2.7
# 组件：
# 描述：
# 备注：
#-------------------------------------------------------

import sys
import logging
sys.path.append("../lib")
from json_parse import *

def UnitTest():

    data = {}

    data['log_type'] = 'aaa'
    data['level'] = 'bbb'
    data['room_id'] = 'ccc'

    for i in range(5):
        data_sub1 = {}
        data_sub1['uid'] = '%s%s%s' % (i, i, i)
        data_sub1['start_money'] = '%s%s%s' % (i, i, i)
        data_sub1['money'] = '%s%s%s' % (i, i, i)
        data['num_%s' % (i)] = data_sub1

    for j in range(5):
        data_sub2 = {}
        data_sub2['uid'] = '%s%s%s' % (j, j, j)
        data_sub2['start_money'] = '%s%s%s' % (j, j, j)
        data_sub2['money'] = '%s%s%s' % (j, j, j)
        data['teer_%s' % (j)] = data_sub2

    myJs = CJson()

    res = myJs.Write(data)
    print res

    res = myJs.Read(res)
    print res
    print res['teer_3']['money']

def main():
    args = sys.argv
    UnitTest()

if __name__ == '__main__':
    print 'sys.argv=' +__name__
    print sys.argv

    logging.warning('call main FFF')
    main()
