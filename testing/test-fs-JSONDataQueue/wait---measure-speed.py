#!/usr/bin/python3


import time

import jk_interprocesssync.fs

from SpeedMeasuringContext import SpeedMeasuringContext




queue = jk_interprocesssync.fs.JSONDataQueue("/tmp/myramdisk", sleepTime=0)

with SpeedMeasuringContext() as ctx:
	for data in queue.getG():
		ctx.tick("Queue length: " + str(len(queue)) + " :::: ")







