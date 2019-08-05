# #coding: utf-8
# import os

# path = "/Users/mac/Desktop/material/7.17Fashion Daily"
# for root,dirs,files in os.walk(path):
# 	# print(files)
# 	for dir in dirs:
# 		if dir == "android":
# 			print(root)
# 	# print(dirs)
# 	# print(root)

# def log(func):
# 	def wrapper(*args, **kw):
# 		print('call %s()' %func.__name__)
# 		return func(*args, **kw)
# 	return wrapper

# @log
# def now():
# 	print("2019-07-26")

# def nextDay():
# 	print("2019-07-27")

# if __name__ == "__main__":
# 	now()
# 	nextDay = log(nextDay)
# 	nextDay()


# def log(text):
# 	def decorator(func):
# 		def wrapper(*args,**kw):
# 			print('%s %s():' %(text,func.__name__))
# 			return func(*args,**kw)
# 		return wrapper
# 	return decorator

#装饰器
# class Student(object):

# 	@property
# 	def score(self):
# 		return self._score

# 	@score.setter
# 	def score(self,value):
# 		if not isinstance(value, int):
# 			raise ValueError("score must be an integer!")
# 		if value < 0 or value > 100:
# 			raise ValueError('score must between 0 ~ 100!')
# 		self._score = value

# if __name__ == "__main__":
# 	s = Student()
# 	s.score = 60
# 	s.score
# 	s.score = 9999

# try except finally
try:
	print('try...')
	r = 10/0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')























	