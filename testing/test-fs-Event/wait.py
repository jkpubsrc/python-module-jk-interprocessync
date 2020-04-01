#!/usr/bin/python3


import jk_interprocesssync.fs




evt = jk_interprocesssync.fs.Event("eventfile")

for _ in evt.waitG():
	print(_)









