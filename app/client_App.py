#! /bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 200, 331, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 260, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 170, 67, 17))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(lambda: self.on_click())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote OS"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "ip:"))
    
    def on_click(self):
        from remoteOS import Client
        
        text = self.lineEdit.text()
        try:
            c = Client(text, 8889)
            c.Connect()
        except:
            app.setStyleSheet("""
    QWidget {
        background: #262d27
    }
    QLabel{
        color: #fff;
    }

    QLineEdit {
        padding: 1px;
        color: white;
        border: 2px solid red;
        border-radius: 8px;
        text-align: auto;
    }
    QPushButton {
        background:grey;
        
    }
    QPushButton:hover {
        background:blue;
        
    }""")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = """
    QWidget {
        background: #262d27
    }
    QLabel{
        color: #fff;
    }

    QLineEdit {
        padding: 1px;
        color: #fff;
        border: 2px solid #fff;
        border-radius: 8px;
        text-align: auto;
    }
    QPushButton {
        background:grey;
        
    }
    QPushButton:hover {
        background:blue;
        
    }

    """
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
