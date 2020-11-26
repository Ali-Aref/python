# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faceRecognaization.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSelectPhoto = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSelectPhoto.setGeometry(QtCore.QRect(20, 60, 120, 34))
        self.pushButtonSelectPhoto.setObjectName("pushButtonSelectPhoto")
        self.ImgLable = QtWidgets.QLabel(self.centralwidget)
        self.ImgLable.setGeometry(QtCore.QRect(20, 100, 641, 441))
        self.ImgLable.setFrameShape(QtWidgets.QFrame.Box)
        self.ImgLable.setText("")
        self.ImgLable.setObjectName("ImgLable")
        self.pushButtonRecognation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRecognation.setGeometry(QtCore.QRect(140, 60, 120, 34))
        self.pushButtonRecognation.setObjectName("pushButtonRecognation")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 270, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Display SemiCondensed SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButtonWhoIs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonWhoIs.setGeometry(QtCore.QRect(260, 60, 120, 34))
        self.pushButtonWhoIs.setObjectName("pushButtonWhoIs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonSelectPhoto.setText(_translate("MainWindow", "Select Photo"))
        self.pushButtonRecognation.setText(_translate("MainWindow", "Recognation"))
        self.label_2.setText(_translate("MainWindow", "Face Recognation Application"))
        self.pushButtonWhoIs.setText(_translate("MainWindow", "Who is "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# by Ali Aref Mohammadi