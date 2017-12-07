def canConnect(self):
	fnull = open(os.devnull, 'w')
	result = subprocess.call('ping www.baidu.com', shell = True, stdout = fnull, stderr = fnull)
	fnull.close()
	if result:
		print 'yes'
	else:
		print 'no'
