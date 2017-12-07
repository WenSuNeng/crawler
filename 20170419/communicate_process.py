from multiprocessing import Process, Queue
import os, time, random

def write(q):
	for value in ['A', 'B', 'C']
		print 'Put %s to queue ...' % value
		q.put(value)
		time.sleep(random.random())

def read(q):
	while 

