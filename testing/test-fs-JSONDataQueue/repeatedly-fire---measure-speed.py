#!/usr/bin/python3



import time
import random
import os

import jk_interprocesssync.fs

from SpeedMeasuringContext import SpeedMeasuringContext




queue = jk_interprocesssync.fs.JSONDataQueue("/tmp/myramdisk")

with SpeedMeasuringContext() as ctx:
	while True:
		queue.put({
			"v": random.randint(1000, 9999)
		})
		ctx.tick()









