# coding: utf-8

from basicjson import BasicJson

class BackgroundJson(BasicJson):

	def __init__(self, **dic):
		self.id = dic["id"]
		self.imageName = dic["imageName"]
		self.type = dic["image"]
		self.left_constant = dic["constraints"]["left"]["constant"]
		self.left_percentage = dic["constraints"]["left"]["percentage"]
		self.right_constant = dic["constraints"]["right"]["constant"]
		self.right_percentage = dic["constraints"]["right"]["percentage"]
		self.top_constant = dic["constraints"]["top"]["constant"]
		self.top_percentage = dic["constraints"]["top"]["percentage"]
		self.bottom_constant = dic["constraints"]["bottom"]["constant"]
		self.bottom_percentage = dic["constraints"]["bottom"]["percentage"]


	def produce_json_dic(self):
		pass
		

class BlurJson(BasicJson):

	def __init__(self, **dic):
		self.id = dic["id"]
		self.refId = dic["refId"]
		self.type = dic["type"]
		self.blur = dic["blur"]
		self.left_constant = dic["constraints"]["left"]["constant"]
		self.left_percentage = dic["constraints"]["left"]["percentage"]
		self.right_constant = dic["constraints"]["right"]["constant"]
		self.right_percentage = dic["constraints"]["right"]["percentage"]
		self.top_constant = dic["constraints"]["top"]["constant"]
		self.top_percentage = dic["constraints"]["top"]["percentage"]
		self.bottom_constant = dic["constraints"]["bottom"]["constant"]
		self.bottom_percentage = dic["constraints"]["bottom"]["percentage"]

	def produce_json_dic(self):
		pass


class LevelJson(BasicJson):

	def __init__(self, **dic):
		self.id = dic["id"]
		self.contentMode = dic["contentMode"]
		self.type = dic["type"]
		self.height_constant = dic["constraints"]["height"]["constant"]
		self.height_percentage = dic["constraints"]["height"]["percentage"]
		self.right_constant = dic["constraints"]["right"]["constant"]
		self.right_percentage = dic["constraints"]["right"]["percentage"]
		self.top_constant = dic["constraints"]["top"]["constant"]
		self.top_percentage = dic["constraints"]["top"]["percentage"]
		self.width_constant = dic["constraints"]["width"]["constant"]
		self.width_percentage = dic["constraints"]["width"]["percentage"]

	def produce_json_dic(self):
		pass



