all: Ui_MainWindow.py

Ui_MainWindow.py: MainWindow.ui
	pyuic4 MainWindow.ui -o Ui_MainWindow.py

clean:
	-rm *.pyc Ui_*.py
