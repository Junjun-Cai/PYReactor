#timer_unit_test.py
# -*- coding: utf-8 -*-
import sys, os, time, datetime
sys.path.append("../core")
from timer import *
from reactor import  *

class  TimerTest(CBYTimer):
    def __init__(self):
        CBYTimer.__init__(self)

    def OnTimerOut(self, timer_id):
        log_debug("timer_id =%d,  cur_time=%f", timer_id, time.time())


def unitTest():

    reactor = CReactor.Instance()
    obj = TimerTest()

    obj.StartTimer(100, 1, True)
    obj.StartTimer(101, 0.5, True)


    reactor.RunEventLoop()

    curr_t =  time.time()
    print  type(curr_t)
    print  curr_t
    for i in range(15):
        time.sleep(0.1)
        curr_t = time.time()
        print  curr_t


if __name__ == '__main__':
    #unitTest = TestCase()
    #unitTest.unitTest()
    unitTest()
