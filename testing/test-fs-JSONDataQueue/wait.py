#!/usr/bin/python3


import jk_interprocesssync.fs




queue = jk_interprocesssync.fs.JSONDataQueue("queuedir")

for data in queue.getG():
	print(data)









