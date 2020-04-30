'''
Application: Spider with auto-notice function
Description: check Export Control License status
Version: 1.0
'''

import subprocess

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

def main():
	try:
		deleteDoc()
		print("quotes.json is deleted successful!")
	except:
		print("quotes.json has been already deleted.")
	

	getData()
	print("Grab data, Done!")

	sendEmail()
	print("Send email, Done!")

if __name__ == "__main__":
	main()