#!/usr/bin/env python
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MainWindow import *


def main():
	app = QApplication(sys.argv)
	window = MainWindow()

	log = file(sys.argv[1]).readlines()
	log = [x.rstrip() for x in log]
	window.setLog(log)

	window.show()
	app.exec_()


if __name__=="__main__":
	main()
