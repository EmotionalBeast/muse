#!/usr/bin/python3
#coding: utf-8
#@author: Lazy Yao
#@email: none
#@date: 2020/07/10 14:08

import os, json

CH = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
class AnimationData(object):
    def __init__(self, path1, path2):
        self.txt = path1
        self.json = path2
        self.img = self.getPictureName()
        self.dic = self.getJsonDic()
        self.index = []

    def getPictureName(self):
        img = []
        with open(self.text, "r") as f:
            content = f.read()
            img = content.split("\n")
        return img

    def getJsonDic(self):
        dic = {}
        with open(self.json, "r") as f:
            jsonStr = f.read()
            dic = json.loads(jsonStr, strict = False)
        return dic

    def replaceNM(self):
        for layer in self.dic["layers"]:
            if layer["refId"] in self.img:
                layer["nm"] = self.getValue(layer["refId"])
        
        with open(self.json, "w") as f:
            jsonStr = json.dumps(self.dic, sort_keys=True, indent=2, ensure_ascii=False)
            f.write(jsonStr)

    def getValue(self, value):
        for c1 in CH:
            tmp = value.replace("_", "") + c1
            if tmp not in self.index:
                self.index.append(tmp)
                return tmp
        return None
    
    def getLayersNM(self):
        dic = {}
        for layer in self.dic["layers"]:
            if layer["refId"] in self.img:
                dic[layer["refId"]].append(layer["nm"])
        return dic
    
    def getImageContentSize(self):
        dic = {}
        for asset in self.dic["assets"]:
            if asset["id"] in self.img:
                dic[asset["id"]].append(asset["w"])
                dic[asset["id"]].append(asset["h"])
        return dic


    


                


