#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mv_on_mac.py
@Time    :   2020/03/29 18:24:11
@Author  :   Lazy Yao 
@Version :   1.0
@Contact :   jhinyao@163.com
@License :   None yet
@Desc    :   None
'''

# here put the import lib


import os, subprocess, shutil, sys

PATH_MATERIAL = os.path.join(os.getcwd(), "material")
PATH_IN = os.path.join(os.getcwd(), "in")
PATH_OUT = os.path.join(os.getcwd(), "out")
PATH_ORIGIN = os.path.join(os.getcwd(), "origin")

def encryption(path):
    jarPath = os.path.join(path, "encrypt.jar")
    command = "java -jar " + jarPath + " " + PATH_IN + " " + PATH_OUT
    if info := subprocess.check_call(comand, shell=True) == 0:
        print("encrypt success!")
    else:
        if os.path.exists(PATH_IN) and os.path.exists(PATH_OUT):
            print("encrypt fail!")
            print("error:", info)
        else:
            print("encrypt fail! please check the dir")
    

def createBeatMV(path):
    jarPath = os.path.join(path, "generate.jar")
    command = "java -jar " + jarPath + " -an -vex " + PATH_IN
    if info := subprocess.check_call(command, shell=True) == 0:
        print("Beat MV create success!")
    else:
        if os.path.exists(PATH_IN):
            print("encrypt fail!")
            print("error:", info)
        else:
            print("encrypt fail! please check the dir")


def createChicMV(path):
    jarPath = os.path.join(path, "generate.jar")
    command = "java -jar " + jarPath + " -an " + PATH_IN 
    if info := subprocess.check_call(command, shell=True) == 0:
        print("Chic MV create success!")
    else:
        if os.path.exists(PATH_IN):
            print("encrypt fail!")
            print("error:", info)
        else:
            print("encrypt fail! please check the dir")

def compress(path):
    for root,dirs,files in os.walk(PATH_OUT):
			for dir in dirs:
				if root == PATH_OUT:
                    tmpStr = dir + ".7z"
					pathNeed = os.path.join(PATH_OUT, dir)
					targetFile = os.path.join(PATH_ORIGIN, tmpStr)
					command = "7z a " + targetFile + " " + pathNeed
					os.system(command)

def cleanFile(path):
    files = os.listdir(path)
	for file in files:
		filepath = os.path.join(path, file)
		if os.path.isfile(filepath):
			os.remove(filepath)
		elif os.path.isdir(filepath):
			self.cleanFile(filepath)
		else:
			continue
	os.rmdir(path)


if __name__ == "__main__":
    path = getcwd()
    shutil.copytree(PATH_IN, PATH_MATERIAL)
    createBeatMV(path)
    encryption(path)
    compress(path)
    cleanFile(PATH_IN)
    os.mkdir(PATH_IN)
    cleanFile(PATH_OUT)
    os.mkdir(PATH_OUT)