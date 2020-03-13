# coding: utf-8

import os, sys, subprocess, shutil


class Tools(object):

    @staticmethod
    def encryption(self, path):
        pathIn = path
        pathOut = path[:-2] + "out"
        pathJar = "./resources/jar/encrypt.jar"
        command = "java -jar " + pathJar + " " + pathIn + pathOut
        return subprocess.check_call(command, shell=True)

    @staticmethod
    def compressing(self, path):
        key = 0
        pathOut = path[:-2] + "out"
        pathOrigin = path[:-2] + "origin"
        for root,dirs,files in os.walk(pathOut):
            for dir in dirs:
                if root = pathOut:
                    pathNeed = pathOut + "/" + dir + "/"
                    targetFile = pathOrigin + "/" + dir + ".7z"
                    command = "7z a " + targetFile + pathNeed
                    key += subprocess.check_call(command, shell=True)
        return key
    
    @staticmethod
    def cleanFile(self, path):
        files = os.listdir(path)
        for file in files:
            filePath = os.path.join(path, file)
            if os.path.isfile(filePath):
                os.remove(filePath)
            elif os.path.isdir(filePath):
                self.cleanFile(filePath)
            else:
                continue
        os.rmdir(path)

    @staticmethod
    def copyFile(self, path):
        pathMaterial = path[:-2] + "material"
        shutil.copytree(path, pathMaterial)

            


