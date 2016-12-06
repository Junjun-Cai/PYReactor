#main.py
# -*- coding: utf-8 -*-

import sys, os
import logging
import socket
sys.path.append("../core")

from packet import *
from encrypt import *
from reactor import *
from tcplistener import *
from udplistener import *
import server_unit_test




class baseA :
    def __init__(self):
        print ('init baseA')

    def __del__(self):
        print ( 'del baseA')


class childA(baseA):
    def __init__(self):
        baseA.__init__(self)
        print ('init childA')


    def __del__(self):
        print  ('del childA')
        baseA.__del__(self)

def test_listen(ip_, port_):
    try:
        m_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        m_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        m_Socket.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        m_Socket.bind((ip_, port_))
        m_Socket.listen(256)
        m_Socket.setblocking(0)
        #EnableInput()
        #DisableOutput()
    except IOError as err:
        print  err
        print ("listen [%s:%d] fail !! err_str=%s " % (ip_, port_,  os.strerror(err.errno)))
        m_Socket.close()
        return False
    except:
        print "unkonw err"
        return  False
    return True


def unitTest():

    #err = "listen port socket err, [%s:%d]" % ("127.0.0.1", 7001)
    #print  err

    parser = CPakectParser()
    server = server_unit_test.GameServer()
    reactor = CReactor.Instance()
    reactor2 = CReactor.Instance()
    reactor.SetPacketParser(parser)

    const.abc = 111
    print  const

    print ("reactor=", reactor)
    print ("reactor2=", reactor2)
    print ( isinstance(reactor, CReactor))

    listener = CTcpListener(reactor, server)
    udp_listener = CUdpListener(reactor, server)

    listener.Listen("0.0.0.0", 4800, 256)
    udp_listener.Listen("0.0.0.0", 4805)

    reactor.RunEventLoop()


    return

    print "unitTest  hello world!!"
    table_ = {}
    table_[1] = 100
    table_[2] = 99
    table_[3] = 98
    table_[5] = 97
    table_[6] = 96
    print  table_

    if (not table_.has_key(4)):
        print "4 is not in key"

    for inx in range(1, 7):
        try:
            v = table_[inx]
        except KeyError as err:
            print  err
            continue

        print inx , v



def main():
    args = sys.argv
    unitTest()


if __name__ == '__main__':
    print 'sys.argv= ' + __name__
    print   sys.argv
    logging.warning('call main  FFF')
    main()


