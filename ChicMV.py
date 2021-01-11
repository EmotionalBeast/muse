# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/10/30 11:08



import subprocess, shutil, sys, json, os

IMAGE_FORMAT = ["jpg", "png", "PNG", "JPG"]


class ChicMv(object):

    def __init__(self, path, dic):
        self.path = path
        self.config = {}
        self.elements = []
        self.layers = []

        #文件结构
        self.filter = dic["filter"]
        self.noreplace = dic["noreplace"]
        self.overlay = dic["overlay"]
        self.overlay1 = dic["overlay1"]
        self.audio = dic["audio"]

        #配置文件信息
        self.images = self.getImages()
        self.data = self.getData()
        self.filters = self.getFilters()

    def generateElements(self):
        for i in range(len(self.images)):
            element = {}
            element["contentSize"] = self.data[self.images[i]]
            element["id"] = str(i)
            element["mediaId"] = str(i)
            element["keyPath"] = "images/" + self.images[i]
            element["imageId"] = "image_" + self.images[i].split(".")[0].split("_")[1]
            element["type"] = "media"
            self.elements.append(element)
        
        if self.filter:
            for element in self.elements:
                name = element["keyPath"].split("/")[1]
                if name in self.filters.keys():
                    element["artFilter"] = self.filters[name][0]
                    element["type"] = "clone_media"
                    for item in self.elements:
                        if item["keyPath"].split("/")[1] == self.filters[name][1]:
                          element["refId"] = item["id"]   

    def generateLayers(self):
        if self.overlay1:
            self.layers.append({"type":"backlay_video", "path":"overlay1.mp4"})
        self.layers.append({"type":"lottie", "path":"data.json"})
        if self.audio:
            aac = os.path.join(self.path, "audio.aac")
            if os.path.exists(aac):
                self.layers.append({"type":"audio", "path":"audio.aac"})
            else:
                self.layers.append({"type":"audio", "path":"audio.mp3"})
        if self.overlay:
            self.layers.append({"type":"overlay_video", "path":"overlay.mp4"})

    def generateConfig(self):
        self.generateElements()
        self.generateLayers()

        self.config["width"] = self.data["width"]
        self.config["height"] = self.data["height"]
        self.config["duration"] = self.data["duration"]
        self.config["fps"] = self.data["fps"]
        self.config["version"] = 1
        self.config["layers"] = self.layers
        self.config["elements"] = self.elements

    def writeConfig(self):
        configJson = os.path.join(self.path, "config.json")
        self.generateConfig()
        with open(configJson, "w") as f:
            content = json.dumps(self.config, sort_keys=True, indent=2, ensure_ascii=False)
            f.write(content)

    def getImages(self):
        images_path = os.path.join(self.path, "images")
        images = os.listdir(images_path)
        images = [i for i in images if i.split(".")[1] in IMAGE_FORMAT ]
        images.sort(key=lambda image: int(image.split(".")[0].split("_")[1]))
        if self.noreplace:
            noreplace_path = os.path.join(self.path, "noreplace.txt")
            with open(noreplace_path, "r") as f:
                content = f.read()
                nore_image = content.split("\n")
            images = [i for i in images if i not in nore_image]
        return images

    def getFilters(self):
        filters = {}
        if self.filter:
            filter_path = os.path.join(self.path, "filter.txt")
            with open(filter_path, "r") as f:
                content = f.read()
                temp_list = content.split("\n")
                temp_list = [i for i in temp_list if i != "" and i != " "]
            for temp in temp_list:
                items = temp.split(" ")
                filters[items[0]] = [items[1], items[2]]
            return filters
        return 0
                 

    def getData(self):
        dic = {}
        data_path = os.path.join(self.path, "data.json")
        with open(data_path, "r", encoding='utf-8') as f:
            content = f.read()
            data_dic = json.loads(content, strict = False)

        dic["width"] = data_dic["w"]
        dic["height"] = data_dic["h"]
        dic["duration"] = int(float(data_dic["op"]/data_dic["fr"])*1000)
        dic["fps"] = data_dic["fr"]
        for asset in data_dic["assets"]:
            if "image" in asset["id"]:
                dic[asset["p"]] = [asset["w"], asset["h"]]
        return dic





