#main.py
# -*- coding: utf-8 -*-

import sys
import logging
sys.path.append("../core")
from encrypt import *
from packet import *




def unitTest():
    #return
    print "unitTest  hello world!!"

    str = ''
    print 'str len=', len(str)
    str =  "123456789"
    list_str = list(str)
    print 'list= ', list_str
    new_str = ''.join(list_str)
    print 'new_str=', ','.join(map(lambda x: hex(ord(x)), str))
    print 'oder_type=', ord('A')

    outPkg = OutPacket()
    outPkg.Begin(0x1122)
    outPkg.WriteInt32(0x1122)
    outPkg.WriteByte(0xCC)
    outPkg.WriteString("123")
    outPkg.WriteBinary("1234")
    outPkg.End()

    print 'outPkg.len=', len(outPkg.list_buff)
    print 'outPkg.str_buff=', ','.join(map(lambda x: hex(ord(x)), outPkg.list_buff))
    print 'outPkg.cmd=', hex(outPkg.GetCmd())
    CEncrypt.EncryptBuffer(outPkg)
    print 'encode outPkg.str_buff=', ','.join(map(lambda x: hex(ord(x)), outPkg.list_buff))

    inputPkg = InputPacket()
    inputPkg.CopyFromListBuf(outPkg.PacketListBuf())
    print 'inputPkg.len=', len(inputPkg.list_buff)
    print 'inputPkg.str_buff=', ','.join(map(lambda x: hex(ord(x)), inputPkg.list_buff))
    print 'inputPkg.cmd=', hex(inputPkg.GetCmd())
    CEncrypt.DecryptBuffer(inputPkg)
    print 'decode inputPkg.str_buff=', ','.join(map(lambda x: hex(ord(x)), inputPkg.list_buff))

    value = inputPkg.ReadInt32()
    print 'value_type', type(value)
    print 'value=', hex(value)
    value = inputPkg.ReadByte()
    print 'value_type', type(value)
    print 'value=', hex(value)
    value = inputPkg.ReadString()
    print 'value_type_str', type(value)
    print 'valuee_str=', ','.join(map(lambda x: hex(ord(x)), value))
    value = inputPkg.ReadBinary()
    print 'value_type_bin', type(value)
    print 'value_bin=',  ','.join(map(lambda x: hex(ord(x)), value))


    value = inputPkg.ReadString()
    print 'value_type', type(value)
    print 'value=', ','.join(map(lambda x: hex(ord(x)), value))

def main():
    args = sys.argv
    unitTest()


if __name__ == '__main__':
    print 'sys.argv= ' + __name__
    print   sys.argv
    logging.warning('call main  FFF')
    main()


