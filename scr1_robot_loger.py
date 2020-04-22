#!/usr/bin/env python3

import nclib
while True:

 logfile = open('/home/tom/Projects/proface/scr1_logger/logScr1.txt', 'ab')
 nc = nclib.Netcat(listen=('',2197),udp=True,verbose=0,log_recv=logfile)
 nc.readline()
 logfile.close()
 nc.close()
