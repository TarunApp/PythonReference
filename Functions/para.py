def findtext(websiteurl):
	para = soup.body.findAll(text=re.compile(''))
	para2 = soup.body.findAll(text=re.compile(''))
	paracombine = para + para2
	print(paracombine)
	if "" or "" in paracombine:
		return True
	else:
		return False