'''
Application: Spider with auto-notice function
Description: check Export Control License status
Version: 1.0
'''

import subprocess
# from multiprocessing import Process
# import time

# delete the old one
# terminal $ rm quotes.json
deleteCmd = ['rm', 'quotes.json']

# terminal $ scrapy crawl quotes_EL -o quotes.json -L WARN
# runSpiderCmd = ['scrapy', 'crawl', 'quotes_EL', '-o', '/Users/xiaoyangzhang/git_base/Spider/tutorial/quotes.json', '-L', 'WARN']
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
	except Exception as e:
		print("file doesn't exist, don't worry --- ", e)

	try:
		getData()
	except Exception as e:
		print("error in getData() --- ", e)

	try:
		sendEmail()
	except Exception as e:
		print("error in sendEmail() --- ", e)


def main():
	mySpider()
	# way 1
	# it is a dead loop, press ctrl c to exit!
	# while True:
	# 	p = Process(target=mySpider)
	# 	p.start()
	# 	p.join()
	# 	time.sleep(43200)
		# time.sleep(10)

	# run process in background , please add '&'
	# kill process $ kill pid

if __name__ == "__main__":
	main()
