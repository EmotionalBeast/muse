#coding: utf-8
import os

path = "/Users/mac/Desktop/material/7.17Fashion Daily"
for root,dirs,files in os.walk(path):
	# print(files)
	for dir in dirs:
		if dir == "android":
			print(root)
	# print(dirs)
	# print(root)