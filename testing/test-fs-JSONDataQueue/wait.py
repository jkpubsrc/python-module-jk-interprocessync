#!/usr/bin/python3


import jk_interprocesssync.fs




evt = jk_interprocesssync.fs.JSONDataQueue("queuedir")

for data in evt.waitG():
	print(data)









