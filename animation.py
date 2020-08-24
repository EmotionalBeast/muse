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
        with open(self.txt, "r") as f:
            content = f.read()
            pic_list = content.split("\n")

        pic_list = [i for i in pic_list if i != '']
        
        for name in pic_list:
            tmp = name.replace("img", "image").split(".")[0]
            img.append(tmp)
        return img

    def getJsonDic(self):
        dic = {}
        with open(self.json, "r") as f:
            jsonStr = f.read()
            dic = json.loads(jsonStr, strict = False)
        return dic

    def replaceNM(self):
        print(self.img)
        for i in range(len(self.dic["layers"])):
            if "refId" in self.dic["layers"][i].keys():
                if self.dic["layers"][i]["refId"] in self.img:
                    self.dic["layers"][i]["nm"] = self.getValue(self.dic["layers"][i]["refId"])

        for i in range(len(self.dic["assets"])):
            if "layers" in self.dic["assets"][i].keys():
                for j in range(len(self.dic["assets"][i]["layers"])):
                    if "refId" in self.dic["assets"][i]["layers"][j].keys():
                        if self.dic["assets"][i]["layers"][j]["refId"] in self.img:
                            self.dic["assets"][i]["layers"][j]["nm"] = self.getValue(self.dic["assets"][i]["layers"][j]["refId"])

        with open(self.json, "w") as f:
            jsonStr = json.dumps(self.dic, sort_keys=True, indent=2, ensure_ascii=False)
            f.write(jsonStr)

    def getValue(self, value):
        for c1 in CH:
            tmp = value.replace("_", "") + c1
            if tmp not in self.index:
                self.index.append(tmp)
                return tmp
        print(self.index)
        return None
    
    def getLayersNM(self):
        dic = {}
        index = []
        #layer层
        for layer in self.dic["layers"]:
            if "refId" in layer.keys():
                if layer["refId"] not in index and layer["refId"] in self.img:
                    index.append(layer["refId"])
                    dic[layer["refId"]] = []

        for layer in self.dic["layers"]:
            if "refId" in layer.keys():
                if layer["refId"] in self.img:
                    dic[layer["refId"]].append(layer["nm"])
        #assert层
        for i in range(len(self.dic["assets"])):
            if "layers" in self.dic["assets"][i].keys():
                for j in range(len(self.dic["assets"][i]["layers"])):
                    if "refId" in self.dic["assets"][i]["layers"][j].keys():
                        refId = self.dic["assets"][i]["layers"][j]["refId"]
                        if refId not in index and refId in self.img:
                            index.append(refId)
                            dic[refId] = []

        for i in range(len(self.dic["assets"])):
            if "layers" in self.dic["assets"][i].keys():
                for j in range(len(self.dic["assets"][i]["layers"])):
                    if "refId" in self.dic["assets"][i]["layers"][j].keys():
                        refId = self.dic["assets"][i]["layers"][j]["refId"]
                        if refId in self.img:
                            dic[refId].append(self.dic["assets"][i]["layers"][j]["nm"])
                            
        return dic
    
    def getImageContentSize(self):
        dic = {}
        for asset in self.dic["assets"]:
            if asset["id"] in self.img:
                dic[asset["id"]] = []
                dic[asset["id"]].append(asset["w"])
                dic[asset["id"]].append(asset["h"])
        return dic
    
    def ignore(self): #bool
        dic = self.getLayersNM()
        for image in dic.keys():
            if len(dic[image]) > 1:
                return True
        return False



    


                


