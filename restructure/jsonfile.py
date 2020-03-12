# coding: utf-8

import json, sys, os, shutil

class StoryChicJson(object):
    def __init__(self, path):
        #定义属性
        self._jsonStr = ""
        self._dict = {}
        self._media = []
        self._background = {}
        self._text = []
        self._blur = {}
        self._level = {}

        #初始化
        self.readFile(path)
        self.resolveJson()

    def readFile(self, path):
        with open(path, "r") as file:
            self._jsonStr = file.read()
            self._dict = json.loads(self._jsonStr, strict = False)

    def writeFile(self, path):
        pass

    def resolveJson(self):
        items = self._dict["elements"]
        for i in range(len(items)):
            if "blur" in items[i].keys():
                self._blur = items[i]
            if "mediaId" in items[i].keys():
                self._media.append(items[i])
            if "imageName" in items[i].keys():
                self._background = items[i].keys()
            if "textId" in items[i].keys():
                self._text.append(items[i])
            if "contentMode" in items[i].keys():
                self._level = items[i]
    
    def getMediaContent(self):
        return self._media

    def getBackgroundContent(self):
        return self._background

    def getTextContent(self):
        return self._text

    def getBlurContent(self):
        return self._blur

    def getLevelContent(self):
        return self._level
    
    def setMeidaContent(self, **dict):
        pass

    def setBackgroundContent(self, **dict):
        pass

    def setTextContent(self, **dict):
        pass

    def setBlurContent(self, **dict):
        pass

    def setLevelContent(self, **dict):
        pass






