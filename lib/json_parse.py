# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：jason字串的编码与解析。
# 作者：ColeCai-蔡君君
# 文件：json_parse.py
# 日期：2016/10/11-11:47
# 版本：1.0.0
# 环境：python 2.7
# 组件：json
# 描述：程序用于对字典类型的数据进行编码得到jason字串以及对jason
# 进行解析得到字典类型的数据。
# 备注：
#-------------------------------------------------------

import json
import sys
sys.path.append("../core")
from const import *

const.OPERATE_SUCCESS = 1
const.OPERATE_FAILURE = -1

class CJson(object):

    def Write(self, data):
        """
        @summary:将数据编码成json字串。
        @param data: 需要进行编码的数据，字典类型。
        @return: 操作成功则返回编码成功的json字串，否则返回-1。
        """
        try:
            return json.dumps(data)
        except:
            return const.OPERATE_FAILURE

    def Read(self,jsondata):
        """
        @summary:对json字串进行解码操作。
        @param jsondata: json字串。
        @return: 操作成功则返回解码后的数据(字典类型)，否则返回-1。
        """
        try:
            return json.loads(jsondata)
        except:
            return const.OPERATE_FAILURE