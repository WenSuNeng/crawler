import urllib
import urllib2 
import re
import thread
import time

class QSBK:
	def __init__(self):
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		self.headers = {'User-Agent' : self.user_agent}
		self.stories = []
		self.enable = False
	def getPage(self,pageIndex):
		try: 
			url = 'http://www.qiushibaike.com/hot'
			request = urllib2.Request(url,headers = self.headers)
			response = urllib2.urlopen(request)
			pageCode =  reponse.read().decode('utf-8')

		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print u"failed to connect to qiushibaike",e.reason
				return Node
