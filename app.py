#! /bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import core

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 600)
        font = QtGui.QFont()
        font.setFamily("aakar")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(440, 180, 131, 41))
        self.b1.setObjectName("b1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Padauk")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 140, 431, 31))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 120, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 300, 341, 201))
        self.label_3.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 280, 91, 17))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 22))
        self.menubar.setObjectName("menubar")
        self.menuPort_Scanner_webapp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK KR")
        self.menuPort_Scanner_webapp.setFont(font)
        self.menuPort_Scanner_webapp.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.menuPort_Scanner_webapp.setObjectName("menuPort_Scanner_webapp")
        self.menuPort_Scanner_API = QtWidgets.QMenu(self.menubar)
        self.menuPort_Scanner_API.setObjectName("menuPort_Scanner_API")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPort_Scanner_webapp.menuAction())
        self.menubar.addAction(self.menuPort_Scanner_API.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.b1.clicked.connect(lambda: self.on_click())
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Port Scanner"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>ip</p></body></html>"))
        self.b1.setText(_translate("MainWindow", "Scan"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#ad7fa8;\">Port Scanner</span></p></body></html>"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "127.0.0.1"))
        self.label_2.setText(_translate("MainWindow", "IP Address:"))
        self.label_3.setText(_translate("MainWindow", "."))
        self.label_4.setText(_translate("MainWindow", "Open Ports:"))
        
        
    def on_click(self):
        ip = self.lineEdit.text()
        scan = core.Scan(ip=ip)
        self.label_3.setText(str(scan.run()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = """
    QWidget {
        background: #262d27
    }
    QLabel#label_2, QLabel#label_4{
        color: #fff;
    }

    QPushButton {
        background:black;
        color:#fff;
    }
    QPushButton:hover {
        background:purple;
        color:#fff;
    }

    QLineEdit {
        padding: 1px;
        color: #fff;
        border: 2px solid #fff;
        border-radius: 8px;
        text-align: auto;
    }

    QLineEdit:hover {
        background-color:black;
    }
    """
    app.setStyleSheet(style)
    app.setWindowIcon(QIcon('icon.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
