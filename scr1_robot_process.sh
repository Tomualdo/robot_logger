#!/bin/sh

if ps -ef | grep -v grep | grep scr1_robot_loger.py ; then
        echo running
		exit 0
else
		echo not running
        /home/tom/Projects/proface/scr1_logger/scr1_robot_loger.py
        exit 0
fi
