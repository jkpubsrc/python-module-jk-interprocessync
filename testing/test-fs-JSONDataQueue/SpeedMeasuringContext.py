

import time




class SpeedMeasuringContext(object):

	def __init__(self):
		self.__n = 0
		self.__t0 = time.time()
	#

	def __enter__(self):
		return self
	#

	def __exit__(self, *args):
		pass
	#

	def tick(self, msg:str = ""):
		self.__n += 1
		t1 = time.time()
		duration = t1 - self.__t0
		if duration >= 2:
			rate = self.__n / duration
			self.__t0 = t1
			self.__n = 0
			print(msg + str(round(rate, 2)) + " items per second")		
	#

#






