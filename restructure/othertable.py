# coding: utf-8

from basictable import BasicTable

class BackgroundTable(BasicTable):
	def __init__(self, **dict):
		self.id = dict["id"]
		self.imageName = dict["imageName"]
		self.type = dict["image"]
		self.left_constant = dict["constraints"]["left"]["constant"]
		self.left_percentage = dict["constraints"]["left"]["percentage"]
		self.right_constant = dict["constraints"]["right"]["constant"]
		self.right_percentage = dict["constraints"]["right"]["percentage"]
		self.top_constant = dict["constraints"]["top"]["constant"]
		self.top_percentage = dict["constraints"]["top"]["percentage"]
		self.bottom_constant = dict["constraints"]["bottom"]["constant"]
		self.bottom_percentage = dict["constraints"]["bottom"]["percentage"]
		

class BlurTable(BasicTable):
	def __init__(self, **dict):
		self.id = dict["id"]
		self.refId = dict["refId"]
		self.type = dict["type"]
		self.blur = dict["blur"]
		self.left_constant = dict["constraints"]["left"]["constant"]
		self.left_percentage = dict["constraints"]["left"]["percentage"]
		self.right_constant = dict["constraints"]["right"]["constant"]
		self.right_percentage = dict["constraints"]["right"]["percentage"]
		self.top_constant = dict["constraints"]["top"]["constant"]
		self.top_percentage = dict["constraints"]["top"]["percentage"]
		self.bottom_constant = dict["constraints"]["bottom"]["constant"]
		self.bottom_percentage = dict["constraints"]["bottom"]["percentage"]



class LevelTable(BasicTable):
	def __init__(self, **dict):
		self.id = dict["id"]
		self.contentMode = dict["contentMode"]
		self.type = dict["type"]
		self.height_constant = dict["constraints"]["height"]["constant"]
		self.height_percentage = dict["constraints"]["height"]["percentage"]
		self.right_constant = dict["constraints"]["right"]["constant"]
		self.right_percentage = dict["constraints"]["right"]["percentage"]
		self.top_constant = dict["constraints"]["top"]["constant"]
		self.top_percentage = dict["constraints"]["top"]["percentage"]
		self.width_constant = dict["constraints"]["width"]["constant"]
		self.width_percentage = dict["constraints"]["width"]["percentage"]




