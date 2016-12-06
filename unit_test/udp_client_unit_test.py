#udp_client_unit_test.py
# -*- coding: utf-8 -*-

import sys, os
import logging
sys.path.append("../core")
from core.packet import *
from core.encrypt import *
#from core.reactor import *
import  socket
#from core.clienthandler import *
#from core.tcpclient import *
from core.udpclient import *
from core.reactor import *
import server_unit_test

class ObjA:
    def __init__(self):
        self.tt = 0

    def __del__(self):
        pass


def unitTest():
    parser = CPakectParser()
    server = server_unit_test.GameServer()
    reactor = CReactor(parser)

    client =  CUdpClient(reactor, server)


    if (platform.system() == "Windows"):
        client.InitConnect("127.0.0.1", 4805)
    else:
        client.InitConnect("192.168.96.152", 4805)

    #linux test
    #client.InitConnect("192.168.96.152", 4800)


    client.SendStrBuf("udp hello test!!")

    reactor.RunEventLoop()
    str = raw_input("please input:")
    print ("content: ", str)


def main():
    args = sys.argv
    unitTest()


if __name__ == '__main__':
    print 'sys.argv= ' + __name__
    print   sys.argv
    logging.warning('call main  FFF')
    main()