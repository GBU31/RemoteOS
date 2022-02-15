#! /bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def __init__(self):
        from remoteOS import ip_and_port
        ip_and_port = ip_and_port()
        self.host = ip_and_port.get_local_ip()
        self.port = ip_and_port.get_port()    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 130, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 101, 41))
        self.label.setText(self.host)
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
        self.pushButton.setText(_translate("MainWindow", "Start"))

    def on_click(self):
        from server import Server
        self.pushButton.setText('test')
        s = Server(self.host, self.port)
        s.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = """
    QWidget {
        color: #fff;
        background: #262d27
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
