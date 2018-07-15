import DoNotDisturb

def main():
	dnd = DoNotDisturb.DoNotDisturb()

	new_mode = DoNotDisturb.SilenceMode()
	new_mode.setTotalSilence()
	dnd.setMode(new_mode)

	dnd.addTime()
	dnd.addTime()

	#time.sleep(10)

	print(dnd.getMode())
	print(dnd.getTimeRemaining())


main()
