from time import sleep as sl
import os
def sleep_pc():
	print("This system will auto sleep/hibernate in 1 hour.")
	sl(3600)
	os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
	exit()
sleep_pc()
