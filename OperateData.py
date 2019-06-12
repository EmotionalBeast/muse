# -*- coding: utf-8 -*-
#author: Jhin Yao
import json

#加载Json文件的模块
class OperateJson:
	def __init__(self, filePath):
		self.filePath_ = filePath

	def loadJson(self):

		with open(self.filePath_, 'r') as load_f:
			jsonStr = load_f.read()
			self.dic = json.loads(jsonStr, strict=False) 
		
		return self.dic 


	def dumpJson(self,dic):
		with open(self.filePath_, 'w') as dump_f:
			jsonStr = json.dumps(dic, sort_keys=True, indent=2)
			dump_f.write(jsonStr)




