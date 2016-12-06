# -*- coding: utf-8 -*
#--------------------------------------------------
# 程序：http_client
# 作者：ColeCai-蔡君君
# 文件：http_client.py
# 日期：2016/10/24-15:17
# 版本：1.0.0
# 环境：python 2.7
# 组件：httplib, urllib
# 描述：连接http服务器，支持get和post两种请求。
# 备注：
#--------------------------------------------------


import httplib
import urllib
import ssl
import socket
import urlparse
import sys
sys.path.append("../core")
from const import *

const.OPERATE_SUCCESS = 1
const.OPERATE_FAILURE = -1

class CHttpClient(object):

    def __init__(self):
        self.httpclient = None

    def __del__(self):
        self.DisConnect()

    def Connect(self, host, type='http', timeout=30 ):
        """
        @summary:连接http服务器，支持以http和https两种方式进行连接。
        @param host:网址或者IP地址。
        @param timeout:连接超时时间。
        @param type:连接类型，http或https。
        @return:操作成功则返回1，否则返回-1。
        """
        if type == 'http':
            try:
                self.httpclient = httplib.HTTPConnection(host, 80, timeout)
                return const.OPERATE_SUCCESS
            except:
                return const.OPERATE_FAILURE
        else:
            try:
                self.httpclient = httplib.HTTPSConnection(host, 443, timeout)
                sock = socket.create_connection((self.httpclient.host, self.httpclient.port))
                self.httpclient.sock = ssl.wrap_socket(sock, self.httpclient.key_file, self.httpclient.cert_file,
                                                       ssl_version=ssl.PROTOCOL_TLSv1)
                return const.OPERATE_SUCCESS
            except:
                return const.OPERATE_FAILURE

    def Get(self, url):
        """
        @summary:发起get请求。
        @param url:请求的资源的url。
        @return:操作成功返回response实例，否则返回-1。
        """
        try:
            self.httpclient.request('GET', url)
            response = self.httpclient.getresponse()
            return (response.status, response.read())
        except:
            return const.OPERATE_FAILURE

    def Post(self, url, body, headers):
        """
        :summary:发起post请求。
        :param url:请求的资源的url。
        :param body:提交到服务器的数据。
        :param headers:请求http的头。
        :return:操作成功返回response实例，否则返回-1。
        """
        try:
            param = urllib.urlencode(body)
            self.httpclient.request('POST', url, param, headers)
            response = self.httpclient.getresponse()
            return (response.status, response.read)
        except:
            return const.OPERATE_FAILURE

    def DisConnect(self):
        """
        :summary:关闭连接。
        :return:操作成功返回1，否则返回-1。
        """
        try:
            if self.httpclient:
                self.httpclient.close()
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE

    def GetUri(self, url):
        """
        :summary:截取url，读出协议、host、以及请求。
        :param url:完整的url。
        :return:操作成功返回一个包含协议、host、请求的字典，否则返回-1。
        """
        u = None
        protocol = None
        hostname = None
        try:
            if url.find('http://') == 0 or url.find('https://') == 0:
                u = urlparse.urlparse(url)
                protocol = u.scheme
                hostname = u.hostname
            else:
                url = 'http://' + url
                u = urlparse.urlparse(url)
                protocol = u.scheme
                hostname = u.hostname
            uri = url.split(protocol + '://' + hostname)
            res = {'protocol':protocol, 'host':hostname, 'uri':uri[1]}
            return res
        except:
            return const.OPERATE_FAILURE

    def Gets(self, url):
        """
        :param url:
        :return:
        """
        re = self.GetUri(url)
        if re is False:
            return const.OPERATE_FAILURE
        res = self.Connect(re['host'], re['protocol'])
        if res == 1:
            return self.Get(re['uri'])
        else:
            return const.OPERATE_FAILURE

    def Posts(self, url, headers, body=''):
        """
        :param url:
        :param body:
        :param headers:
        :return:
        """
        re = self.GetUri(url)
        if re is False:
            return const.OPERATE_FAILURE
        if self.Connect(re['host'], re['protocol']) == 1:
            return self.Post(re['uri'], headers, body)
        else:
            return const.OPERATE_FAILURE