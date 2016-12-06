#localclient.py
# -*- coding: utf-8 -*-


from tcphandler import  *
from packet import *


class CTcpClient(CSocketHandler):
    def __init__(self, reactor_, server_):
        CSocketHandler.__init__(self)
        self.m_Reactor = reactor_
        self.m_PacketParser = reactor_.GetPacketParser()
        self.m_Server = server_
        self.m_IsConnected = False

    def __del__(self):
        self.m_Server = None
        self.m_IsConnected = False

    def Destroy(self):
        self.m_Server = None
        self.m_IsConnected = False
        CSocketHandler.Destroy(self)

    def OnConnected(self):
        self.m_IsConnected = True
        self.m_Server.OnBackConnected(self)
        return 0

    def OnClose(self):
        self.m_IsConnected = False
        return self.m_Server.OnClose(self)

    def OnPacketComplete(self, buf_list):
        input_pkg = InputPacket()
        input_pkg.CopyFromListBuf(buf_list)

        ret = self.m_Server.ProccessBackPacket(self, input_pkg)
        return ret

    def InitConnect(self, ip_, port_):
        self.SetIp(ip_)
        self.SetPort(port_)
        self.m_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.m_Socket.connect((ip_, port_))
        except IOError as err:
            core_err("Connect [%s:%d] Failed,err_no=%d, err_str=%s ",
                     str(ip_), port_, err.errno, os.strerror(err.errno))
            self.HandleClose()
            return  False


        self.m_Socket.setblocking(0)
        self.EnableInput()
        self.DisableOutput()
        self.AttachPoller(self.m_Reactor.GetPollerUnit())

        ret = self.OnConnected()
        if(ret < 0):
            return  False

        return  True

    def SendPacket(self, outPkg):
        if(not self.m_IsConnected):
            return -1
        else:
            return self.SendBuf(outPkg.PacketListBuf())