#!/usr/bin/python3



import time
import random
import os

import jk_interprocesssync.fs




queue = jk_interprocesssync.fs.JSONDataQueue("queuedir")

while True:
	print("Sleeping for 2 seconds ...")
	time.sleep(2)

	print("Firing event ...")
	queue.put({
		"v": random.randint(1000, 9999)
	})









