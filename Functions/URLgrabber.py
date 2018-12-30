def namecollect(websiteurl):
	b = websiteurl.split(".")
	#print(b[0])
	e = (b[0])
	str(e)
	#print(e)
	h = e.split("/")
	r = h[2]
	#print(r)
	
	#if r in names:
		#print(True)
		#print(r) 
	#else:
		#print(False)
		#return 0

	a = len(r)
	random.seed(time)
	rand1 = random.randrange(0, a)
	rand2 = random.randrange(0, a)
	rand3 = random.randrange(0, a)
	rand4 = random.randrange(0, a)
	#rand5 = random.randrange(0, a)
	#rand6 = random.randrange(0, a)

	list(r)
	r1 = r[rand1]
	r2 = r[rand2]
	r3 = r[rand3]
	r4 = r[rand4]
	#r5 = r[rand5]
	#r6 = r[rand6]
	print(r)
	print(r1, r2, r3, r4)
	rlist = []
	rlist.append(r1)
	rlist.append(r2)
	rlist.append(r3)
	rlist.append(r4)