#!/usr/bin/python3
import os, subprocess

PATH = os.path.dirname(__file__)
PATH_IN = os.path.join(PATH, "in")
PATH_OUT = os.path.join(PATH, "out")
PATH_ORIGIN = os.path.join(PATH, "origin")
PATH_ENCRYPT_JAR = os.path.join(PATH, "encrypt.jar")
PATH_TEMPLATETOLAYOUT_JAR = os.path.join(PATH, "TemplateToLayout.jar")

# command = "7z a " + targetFile + " " + pathNeed
def compressing():
    for root, dirs, files in os.walk(PATH_OUT):
        for dir in dirs:
            if root == PATH_OUT:
                fileName = dir + ".7z"
                targetFile = os.path.join(PATH_ORIGIN, fileName)
                pathNeed = os.path.join(PATH_OUT, dir)
                command = "7z a " + targetFile + " " + pathNeed
                os.system(command)

def encryption():
    command = "java -jar " + PATH_ENCRYPT_JAR + PATH_IN + PATH_OUT
    os.system(command)


if __name__ == "__main__":
    encryption()
    compressing()