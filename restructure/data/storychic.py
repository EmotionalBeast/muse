#coding: utf-8

from basictable import BasicTable

class MediaTable(BasicTable):
	def __init__(self, **dic):
		pass

class StaticMediaTable(MediaTable):
	def __init__(self):
		pass


class AnimateMediaTable(MediaTable):
	def __init__(self):
		pass

class BackgroundTable(BasicTable):
	def __init__(self, **dict):
		pass
				
class BlurTable(BasicTable):
	def __init__(self, **dict):
		pass


class LevelTable(BasicTable):
	def __init__(self, **dict):
		pass


class AnimateTable(BasicTable):
    	def __init__(self, **dict):
    		pass

class TextTable(BasicTable):
	def __init__(self):
		pass

class StaticTextTable(TextTable):
	def __init__(self):
		pass


class AnimateTextTable(TextTable):
	def __init__(self):
		pass
