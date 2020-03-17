# coding: utf-8

class BasicTable(object):

	_INT = ["blur", ]
	_FLOAT = ["left_percentage", "right_percentage","top_percentage","bottom_percentage","left_constant","right_constant","top_constant", "bottom_constant", "height_percentage", "height_constant","width_percentage","width_constant","filterStrength","rotation"]
	def __init__(self):
		super(BasicTable, self).__init__()

	def produceList(self):
		pass

	def setTableItem(self, tableWidget, *lis):
		for i in range(len(lis)):
    		for j in range(len(lis[i])):
    				tableWidget.setItem(i, j, QTableWidgetItem(lambda lis[i][j]: lis[i][j] if isinstance(lis[i][j], str) else str(lis[i][j])))

	def getTableItem(self, tableWidget):
		lis = []
    	for i in range(tableWidget.rowCount()):
			for j in range(tableWidget.columnCount()):
				lis[i][tableWidget.horizontalHeaderItem(j)] = tableWidget.item(i, j).text()
		return lis
	
	
	
		
