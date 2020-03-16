# coding: utf-8

import json, sys, os, shutil

class JsonFile(object):    
    def __init__(self, path):
        self._jsonStr = ""
        self._dict = {}

    def readFile(self, path):
        with open(path, "r") as file:
            self._jsonStr = file.read()
            self._dict = json.loads(self._jsonStr, strict = False)
    
    def writeFile(self, path):
        with open(path, "w") as file:
            self._jsonStr = json.dumps(self._dict, sort_keys=True, indent=2, ensure_ascii=False)
            file.write(self._jsonStr)


class StoryChicJson(JsonFile):
    def __init__(self, path):
        super(StoryChicJson, self).__init__(path)
        #定义属性
        self._media = []
        self._background = {}
        self._text = []
        self._blur = {}
        self._level = {}
        self._elements = []
        self._version = "1.1"
        self._templateId = ""

        #初始化
        self.readFile(path)
        self.resolveJson()

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
    
    @property
    def getMediaContent(self):
        return self._media

    @property
    def getBackgroundContent(self):
        return self._background

    @property
    def getTextContent(self):
        return self._text

    @property
    def getBlurContent(self):
        return self._blur

    @property
    def getLevelContent(self):
        return self._level
    
    
    def setMeidaContent(self, *lis):
        pass

    def setBackgroundContent(self, **dict):
        pass

    def setTextContent(self, *lis):
        pass

    def setBlurContent(self, **dict):
        pass

    def setLevelContent(self, **dict):
        pass
    

    

class StoryVibeJson(JsonFile):
    pass





