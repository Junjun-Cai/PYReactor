#server_unit_test.py
# -*- coding: utf-8 -*-


import sys, os, time, datetime
sys.path.append("../core")
from baseserver import *


class GameServer(CBaseServer):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def InitServer(self):
        return 0

    def OnClose(self, client_handler):
        print("OnClose handler=", client_handler)
        return 0

    def ProcessPacket(self, client_handler, input_pkg):
        cmd = input_pkg.GetCmd()
        print ("ProcessPacket cmd=0x", hex(cmd))
        if(0x111 == cmd):
            num = input_pkg.ReadInt32()
            str_buf = input_pkg.ReadString()
            print("ProcessPacket ", num, str_buf)
            client_handler.SendPacket(input_pkg)
        else:
            # echo rcv packet
            client_handler.SendPacket(input_pkg)
        return 0

    def OnBackClose(self, back_client):
        print("OnBackClose client=", back_client)
        return 0

    def OnBackConnected(self, back_client):
        print ("OnBackConnected, obj=%s"%back_client)
        if (100 == back_client.GetType()):
            list_buff = []
            outPkg = OutPacket()
            outPkg.Begin(0x1122)
            outPkg.WriteString("hello word!!zhanbao_test aaaaaaaaaaaaaaaaaaaaa")
            outPkg.End()

            for i in range(3):
                list_buff.extend(outPkg.PacketListBuf())

            list_len = len(list_buff)
            while(len(list_buff) >= 17):
                back_client.SendBuf(list_buff[0:17])
                list_buff = list_buff[17:]
                time.sleep(0.050)
                #print ("while wait time=", datetime.datetime.now())

            back_client.SendBuf(list_buff)

            print ("send all packet")
        else:
            outPkg = OutPacket()
            outPkg.Begin(0x111)
            outPkg.WriteInt32(123)
            outPkg.WriteString("hello word!!")
            outPkg.End()
            back_client.SendPacket(outPkg)

        return 0

    def ProccessBackPacket(self, back_client, input_pkg):
        cmd = input_pkg.GetCmd()
        print ("ProccessBackPacket cmd=0x", hex(cmd))
        if(0x111 == cmd):
            num = input_pkg.ReadInt32()
            str_buf = input_pkg.ReadString()
            print("ProccessBackPacket ",  num, str_buf)
        elif (0x1122 == cmd):
            str_buf = input_pkg.ReadString()
            print("ProccessBackPacket str=",  str_buf)

        return 0

    def ProcUdpListenerPacket(self, udp_listener, str_buf, remote_addr):
        print("udp_listener  rcv_data=", str_buf)

        udp_listener.SendStrBuf(str_buf, remote_addr)
        return 0

    def ProcUdpClientPacket(self, udp_client, str_buf):
        print("udp_client rcv_data=", str_buf)
        return 0

    def OnUdpClientClose(self, udp_client):
        print("udp_client close, client_obj=", udp_client)
        return 0