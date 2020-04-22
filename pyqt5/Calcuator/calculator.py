#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2020 ali <ali@parrot>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(6, 14, 411, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(300, 70, 110, 33))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_backSpace = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_backSpace.setGeometry(QtCore.QRect(190, 70, 110, 33))
        self.pushButton_backSpace.setObjectName("pushButton_backSpace")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 150, 81, 33))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(95, 150, 81, 33))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(180, 150, 81, 33))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 81, 33))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(95, 190, 81, 33))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 190, 81, 33))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(95, 228, 81, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 228, 81, 33))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 228, 81, 33))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_point = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_point.setGeometry(QtCore.QRect(95, 266, 81, 33))
        self.pushButton_point.setObjectName("pushButton_point")
        self.pushButton_postiveNegitive = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_postiveNegitive.setGeometry(QtCore.QRect(180, 266, 81, 33))
        self.pushButton_postiveNegitive.setObjectName("pushButton_postiveNegitive")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(10, 266, 81, 33))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_sum = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sum.setGeometry(QtCore.QRect(270, 266, 70, 33))
        self.pushButton_sum.setObjectName("pushButton_sum")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(340, 266, 70, 33))
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_mins = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mins.setGeometry(QtCore.QRect(270, 228, 70, 33))
        self.pushButton_mins.setObjectName("pushButton_mins")
        self.pushButton_1barX = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1barX.setGeometry(QtCore.QRect(340, 228, 70, 33))
        self.pushButton_1barX.setObjectName("pushButton_1barX")
        self.pushButton_multi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multi.setGeometry(QtCore.QRect(270, 190, 70, 33))
        self.pushButton_multi.setObjectName("pushButton_multi")
        self.pushButton_devision = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_devision.setGeometry(QtCore.QRect(270, 152, 70, 33))
        self.pushButton_devision.setObjectName("pushButton_devision")
        self.pushButton_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqrt.setGeometry(QtCore.QRect(340, 152, 70, 33))
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.pushButton_pow2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pow2.setGeometry(QtCore.QRect(340, 190, 70, 33))
        self.pushButton_pow2.setObjectName("pushButton_pow2")
        self.pushButton_sin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sin.setGeometry(QtCore.QRect(10, 112, 80, 33))
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.pushButton_cos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cos.setGeometry(QtCore.QRect(96, 113, 80, 33))
        self.pushButton_cos.setObjectName("pushButton_cos")
        self.pushButton_tan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tan.setGeometry(QtCore.QRect(180, 114, 80, 33))
        self.pushButton_tan.setObjectName("pushButton_tan")
        self.pushButton_log = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_log.setGeometry(QtCore.QRect(270, 114, 70, 32))
        self.pushButton_log.setObjectName("pushButton_log")
        self.pushButton_Ln = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Ln.setGeometry(QtCore.QRect(340, 114, 70, 32))
        self.pushButton_Ln.setObjectName("pushButton_Ln")
        self.pushButton_bin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bin.setGeometry(QtCore.QRect(10, 70, 60, 33))
        self.pushButton_bin.setObjectName("pushButton_bin")
        self.pushButton_oct = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_oct.setGeometry(QtCore.QRect(70, 70, 60, 33))
        self.pushButton_oct.setObjectName("pushButton_oct")
        self.pushButton_hexa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hexa.setGeometry(QtCore.QRect(130, 70, 60, 33))
        self.pushButton_hexa.setObjectName("pushButton_hexa")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 40, 17))
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        question = ""
        self.isNegative = False
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText(question)
        self.pushButton_equal.clicked.connect(self.pushButton_equalClicked)
        self.pushButton_1.clicked.connect(self.numberButtonPressed1)
        self.pushButton_2.clicked.connect(self.numberButtonPressed2)
        self.pushButton_3.clicked.connect(self.numberButtonPressed3)
        self.pushButton_4.clicked.connect(self.numberButtonPressed4)
        self.pushButton_5.clicked.connect(self.numberButtonPressed5)
        self.pushButton_6.clicked.connect(self.numberButtonPressed6)
        self.pushButton_7.clicked.connect(self.numberButtonPressed7)
        self.pushButton_8.clicked.connect(self.numberButtonPressed8)
        self.pushButton_9.clicked.connect(self.numberButtonPressed9)
        self.pushButton_0.clicked.connect(self.numberButtonPressed0)
        self.pushButton_sin.clicked.connect(self.sinX)
        self.pushButton_cos.clicked.connect(self.cosX)
        self.pushButton_tan.clicked.connect(self.tanX)
        self.pushButton_log.clicked.connect(self.logX)
        self.pushButton_Ln.clicked.connect(self.lnX)
        self.pushButton_point.clicked.connect(self.point)
        self.pushButton_backSpace.clicked.connect(self.backspace)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_sum.clicked.connect(self.sum)
        self.pushButton_mins.clicked.connect(self.mins)
        self.pushButton_multi.clicked.connect(self.multi)
        self.pushButton_devision.clicked.connect(self.devision)
        self.pushButton_postiveNegitive.clicked.connect(self.postiveNegitive)
        self.pushButton_sqrt.clicked.connect(self.sqrtX)
        self.pushButton_pow2.clicked.connect(self.pow2)
        self.pushButton_1barX.clicked.connect(self.x1barX)
        self.pushButton_bin.clicked.connect(self.binX)
        self.pushButton_oct.clicked.connect(self.octX)
        self.pushButton_hexa.clicked.connect(self.hexaX)
        self.label.mousePressEvent = self.about

    def about(self, event):
        self.clear()
        self.lineEdit.setPlaceholderText("Simple Calculator designed by Ali Aref Mohammadi")
    def hexaX(self):
        self.lineEdit.setText(str(hex(int(self.lineEdit.text()))))
    def octX(self):
        self.lineEdit.setText(str(oct(int(self.lineEdit.text()))))        
    def binX(self):
        self.lineEdit.setText(str(bin(int(self.lineEdit.text()))))
    def x1barX(self):
        self.lineEdit.setText(str(1/(float(self.lineEdit.text()))))
    def pow2(self):
        self.lineEdit.setText(str(math.pow(float(self.lineEdit.text()),2)))
    def sqrtX(self):
        self.lineEdit.setText(str(math.sqrt(float(self.lineEdit.text()))))
    def lnX(self):
        self.lineEdit.setText(str(math.log(float(self.lineEdit.text()),math.e)))
    def logX(self):
        self.lineEdit.setText(str(math.log10(float(self.lineEdit.text()))))
    def sinX(self):
        self.lineEdit.setText(str(math.sin(float(self.lineEdit.text()))))
    def cosX(self):
        self.lineEdit.setText(str(math.cos(float(self.lineEdit.text()))))
    def tanX(self):
        self.lineEdit.setText(str(math.tan(float(self.lineEdit.text()))))
    def pushButton_equalClicked(self):
        result = str(eval(self.lineEdit.text()))
        self.lineEdit.setText(result)
    def clear(self):
        self.lineEdit.setText("")
    def backspace(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])
    def numberButtonPressed1(self):
        self.lineEdit.setText(self.lineEdit.text() + str(1))
    def numberButtonPressed2(self):
        self.lineEdit.setText(self.lineEdit.text() + str(2))
    def numberButtonPressed3(self):
        self.lineEdit.setText(self.lineEdit.text() + str(3))
    def numberButtonPressed4(self):
        self.lineEdit.setText(self.lineEdit.text() + str(4))
    def numberButtonPressed5(self):
        self.lineEdit.setText(self.lineEdit.text() + str(5))
    def numberButtonPressed6(self):
        self.lineEdit.setText(self.lineEdit.text() + str(6))
    def numberButtonPressed7(self):
        self.lineEdit.setText(self.lineEdit.text() + str(7))
    def numberButtonPressed8(self):
        self.lineEdit.setText(self.lineEdit.text() + str(8))
    def numberButtonPressed9(self):
        self.lineEdit.setText(self.lineEdit.text() + str(9))
    def numberButtonPressed0(self):
        self.lineEdit.setText(self.lineEdit.text() + str(0))
    def sum(self):
        self.lineEdit.setText(self.lineEdit.text() + "+")
    def mins(self):
        self.lineEdit.setText(self.lineEdit.text() + "-")
    def multi(self):
        self.lineEdit.setText(self.lineEdit.text() + "*")
    def devision(self):
        self.lineEdit.setText(self.lineEdit.text() + "/")
    def point(self):
        if self.lineEdit.text() != "":
            self.lineEdit.setText(self.lineEdit.text()+".")
        else :
            self.lineEdit.setText(self.lineEdit.text()+"0.")
    def postiveNegitive(self):
        if  not self.isNegative :
            self.isNegative = True 
            self.lineEdit.setText("-"+self.lineEdit.text())
        else :
            self.isNegative = False
            self.lineEdit.setText(self.lineEdit.text()[1:])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_backSpace.setText(_translate("MainWindow", "Backspace"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.pushButton_postiveNegitive.setText(_translate("MainWindow", u"\N{PLUS-MINUS SIGN}"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_sum.setText(_translate("MainWindow", "+"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_mins.setText(_translate("MainWindow", "-"))
        self.pushButton_1barX.setText(_translate("MainWindow", "1/x"))
        self.pushButton_multi.setText(_translate("MainWindow", "x"))
        self.pushButton_devision.setText(_translate("MainWindow", u"\N{DIVISION SIGN}"))
        self.pushButton_sqrt.setText(_translate("MainWindow", "Sqrt"))
        self.pushButton_pow2.setText(_translate("MainWindow", u"x\N{SUPERSCRIPT TWO}"))
        self.pushButton_sin.setText(_translate("MainWindow", "Sin"))
        self.pushButton_cos.setText(_translate("MainWindow", "cos"))
        self.pushButton_tan.setText(_translate("MainWindow", "tan"))
        self.pushButton_log.setText(_translate("MainWindow", "Log"))
        self.pushButton_Ln.setText(_translate("MainWindow", "Ln"))
        self.pushButton_bin.setText(_translate("MainWindow", "bin"))
        self.pushButton_oct.setText(_translate("MainWindow", "Oct"))
        self.pushButton_hexa.setText(_translate("MainWindow", "Hexa"))
        self.label.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
