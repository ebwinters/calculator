import os

hostname = input("What website should be pinged? ")
response = os.system("ping -c 1 " + hostname)


if response == 0:
	print('host is up')
else:
	print('host is down')