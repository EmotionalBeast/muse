# coding: utf-8

class BasicTable(object):

	def __init__(self):
		super(BasicTable, self).__init__()

	def produceList(self):
		pass

	def setTableItem(self, tableWidget, *lis):
		for i in range(len(lis)):
    		for j in range(len(lis[i])):
    				tableWidget.setItem(i, j, QTableWidgetItem(lambda lis[i][j]: lis[i][j] if isinstance(lis[i][j], str) else str(lis[i][j])))

	def getTableItem(self, tableWidget):
    	pass
	
	
	
		
