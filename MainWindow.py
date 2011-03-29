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
        self.fillView(unicode(text))
        self.filterComboBox.addItem(text)


    def setLog(self, log):
        self.log = log
        self.fillView("")


    def fillView(self, filterText):
        def createItem(number, text):
            return QTreeWidgetItem([str(number), text])

        if filterText:
            regex = re.compile(filterText)
            search = regex.search
        else:
            search = lambda x: True

        self.tree.clear()
        topLevelItem = createItem(0, "[Start]")
        self.tree.addTopLevelItem(topLevelItem)
        for number, line in enumerate(self.log):
            item = createItem(number + 1, line)
            if search(line):
                topLevelItem = item
                self.tree.addTopLevelItem(topLevelItem)
            else:
                topLevelItem.addChild(item)


    def loadSettings(self):
        settings = QSettings("bk12", "messparser")
        lst = settings.value("ui/filters").toStringList()
        self.filterComboBox.addItems(lst)
        self.filterComboBox.clearEditText()


    def saveSettings(self):
        settings = QSettings("bk12", "messparser")
        lst = QStringList()
        for x in range(self.filterComboBox.count()):
            lst.append(self.filterComboBox.itemText(x))
        settings.setValue("ui/filters", QVariant(lst))
