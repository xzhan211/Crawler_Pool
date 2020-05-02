'''
Application: Spider with auto-notice function
Description: check Export Control License status
Version: 1.0
'''

import subprocess
from multiprocessing import Process
import time

# delete the old one
# terminal $ rm quotes.json 
deleteCmd = ['rm', 'quotes.json']

# terminal $ scrapy crawl quotes_EL -o quotes.json -L WARN
runSpiderCmd = ['scrapy', 'crawl', 'quotes_EL', '-o', 'quotes.json', '-L', 'WARN']

# terminal $ python sender.py
sendEmailCmd = ['python', 'sender.py']

def deleteDoc():
	subprocess.check_call(deleteCmd)

def getData():
	subprocess.check_call(runSpiderCmd)	

def sendEmail():
	subprocess.check_call(sendEmailCmd)	

def mySpider():
	try:
		deleteDoc()
		# print("quotes.json is deleted successful!")
	except:
		print("file doesn't exist, don't worry!")

	try:
		getData()
		# print("Grab data. Done!")
		sendEmail()
		# print("Send email. Done!")
	except:
		print("error in getData() or sendEmail()")


def main():
	# it is a dead loop, press ctrl c to exit!
	while True:
		p = Process(target=mySpider)
		p.start()
		p.join()
		time.sleep(43200)

	# run process in background , please add '&'
	# kill process $ kill pid 


if __name__ == "__main__":
	main()