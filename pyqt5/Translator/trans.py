# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'untitled.ui'
# Created by: PyQt5 UI code generator 5.14.2
# WARNING! All changes made in this file will be lost!
import googletrans
from googletrans import Translator
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_src = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_src.setGeometry(QtCore.QRect(10, 67, 561, 251))
        self.textEdit_src.setObjectName("textEdit_src")
        self.comboBox_src = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_src.setGeometry(QtCore.QRect(10, 15, 170, 30))
        self.comboBox_src.setObjectName("comboBox_src")
        self.comboBox_dest = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_dest.setGeometry(QtCore.QRect(230, 13, 170, 32))
        self.comboBox_dest.setObjectName("comboBox_dest")
        self.textEdit_trans = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_trans.setGeometry(QtCore.QRect(10, 322, 561, 271))
        self.textEdit_trans.setObjectName("textEdit_trans")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(406, 11, 160, 34))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(191, 12, 31, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 55, 560, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 30))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionTheme = QtWidgets.QAction(MainWindow)
        self.actionTheme.setObjectName("actionTheme")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout_app = QtWidgets.QAction(MainWindow)
        self.actionAbout_app.setObjectName("actionAbout_app")
        self.menuMenu.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuSettings.addAction(self.actionTheme)
        self.menuSettings.addAction(self.actionSettings)
        self.menuAbout.addAction(self.actionAbout_app)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox_init()
        self.menuAbout.triggered.connect(self.about_clicked)
        self.pushButton.clicked.connect(self.pushButton_clicked)

    def pushButton_clicked(self):
        try:
            translator = Translator()
            self.textEdit_trans.clear()
            src_lang = self.comboBox_src.currentText().split("-")[0].strip()
            des_lang = self.comboBox_dest.currentText().split("-")[0].strip()
            src_text = self.textEdit_src.toPlainText()
            dest_text = translator.translate(src_text, src=src_lang, dest=des_lang)
            self.textEdit_trans.setText(dest_text.text)
        except:
            self.textEdit_trans.setText(
                "Connection Error!\nPlease check your internet and try again!"
            )

    def comboBox_init(self):
        langs = []
        for x in googletrans.LANGUAGES:
            langs.append(f"{x} - {googletrans.LANGUAGES[x]}")
        self.comboBox_src.addItems(langs)
        self.comboBox_dest.addItems(langs)

    def about_clicked(self):
        print("it is about")
        self.textEdit_src.setText(
            "python google Translator designed by Ali Aref Mohammadi, All Rights are reserved!"
        )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Translate"))
        self.label.setText(_translate("MainWindow", "To"))
        self.menuMenu.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open File"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionTheme.setText(_translate("MainWindow", "Theme"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionAbout_app.setText(_translate("MainWindow", "About app"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
