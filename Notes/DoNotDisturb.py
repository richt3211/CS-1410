import datetime

OFF = "off"
TOTAL_SILENCE = "totaly silence"
VIBRATE_ONLY = "vibrate only"

class SilenceMode:
	def __init__(self):
		self.mMode = OFF
		return
	def setOff(self):
		self.mMode = OFF
		return
	def setTotalSilence(self):
		self.mMode = TOTAL_SILENCE
		return
	def setVibrateOnly(self):
		self.mMode = VIBRATE_ONLY
		return

class DoNotDisturb:

	def __init__(self):
		self.mDuration = 0
		self.mMode = SilenceMode()
		self.mStartTime = datetime.datetime.now()
		return
	def addTime(self):
		self.mDuration += 1
		if self.mDuration > 24:
			self.mDuration = 24
		return
	def subtractTime(self):
		self.mDuration -= 1
		if self.mDuration < 0:
			self.mDuration == 0
		return
	def setMode (self, mode):
		self.mMode = mode
		return
	def setStartTime(self):
		self.mStartTime = datetime.datetime.now()
	def getMode(self):
		return self.mMode
	def getTimeRemaining(self):
		current_time = datetime.datetime.now()
		end_time = self.mStartTime + datetime.timedelta(hours = self.mDuration)
		remaining = end_time - current_time
		return remaining
