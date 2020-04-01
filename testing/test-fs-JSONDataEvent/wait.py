#!/usr/bin/python3


import jk_interprocesssync.fs




evt = jk_interprocesssync.fs.JSONDataEvent("eventfile")

for _ in evt.waitG():
	print(_)









