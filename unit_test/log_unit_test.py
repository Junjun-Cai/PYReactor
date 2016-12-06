#log_unit_test.py
# -*- coding: utf-8 -*-
import sys
sys.path.append("../core")
from log import *




def UnitTest():

    init_log("my.log", "log")


    log_debug("hahha  %s ", "hello")
    log_err("hahha  %s ", "hello")
    log_boot("hahha   boot  %s ", "hello")

    core_debug("hahha  %s ", "hello")
    core_err("hahha  %s ", "hello")
    core_boot("hahha   boot  %s ", "hello")


    #print(time.strftime('%m%d'))
    #print time.strftime('%Y-%m-%d %H:%M:%S')
    #log_time = time.localtime()
    #print  log_time

def main():
    args = sys.argv
    UnitTest()


if __name__ == '__main__':
    print 'sys.argv= ' + __name__
    print   sys.argv
    #logging.warning('call main  FFF')
    main()
