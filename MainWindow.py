#!/usr/bin/env python
import re

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_MainWindow import Ui_MainWindow

class MainWindow(QWidget, Ui_MainWindow):
	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)

		QObject.connect(self.filterButton, SIGNAL("clicked()"),
			self.applyFilter)
		QObject.connect(self.filterComboBox.lineEdit(), SIGNAL("returnPressed()"),
			self.applyFilter)

		self.loadSettings()


	def closeEvent(self, event):
		self.saveSettings()
		event.accept()


	def applyFilter(self):
		text = self.filterComboBox.currentText()
		regex = re.compile(unicode(text))
		result = [x for x in self.log if regex.search(x)]
		self.fillView(result)
		self.filterComboBox.addItem(text)


	def setLog(self, log):
		self.log = log
		self.fillView(self.log)


	def fillView(self, lines):
		self.logEdit.clear()
		for line in lines:
			self.logEdit.insertPlainText(line + "\n")


	def loadSettings(self):
		settings = QSettings("bk12", "messparser")
		lst = settings.value("ui/filters").toStringList()
		self.filterComboBox.addItems(lst)


	def saveSettings(self):
		settings = QSettings("bk12", "messparser")
		lst = QStringList()
		for x in range(self.filterComboBox.count()):
			lst.append(self.filterComboBox.itemText(x))
		settings.setValue("ui/filters", QVariant(lst))
