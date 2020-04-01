#!/usr/bin/python3



import time
import random
import os

import jk_interprocesssync.fs




evt = jk_interprocesssync.fs.JSONDataQueue("queuedir")

while True:
	print("Sleeping for 2 seconds ...")
	time.sleep(2)

	print("Firing event ...")
	evt.put({
		"v": random.randint(1000, 9999)
	})









