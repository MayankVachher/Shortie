import base64
flag=1
def genB64here(text):
	return base64.b64encode(text)
	
	
def getPPTReadyButton():
	return flag
	
def setPPTReadyButton(flag_ppt):
	flag = flag_ppt 

