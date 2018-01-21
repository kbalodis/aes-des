# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import os
import functools
import random, string
import binascii

from PyQt5 import QtCore, QtGui, QtWidgets

from pyDes import *
import aes as pyaes

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 352)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralWidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_AES = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_AES.setObjectName("radioButton_AES")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_AES)
        self.gridLayout_2.addWidget(self.radioButton_AES, 0, 0, 1, 1)
        self.radioButton_DES = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_DES.setObjectName("radioButton_DES")
        self.buttonGroup.addButton(self.radioButton_DES)
        self.gridLayout_2.addWidget(self.radioButton_DES, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_key = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.lineEdit_key.setDisabled(True)
        self.gridLayout.addWidget(self.lineEdit_key, 0, 1, 1, 1)
        
        self.label_length = QtWidgets.QLabel(self.widget)
        self.label_length.setObjectName("label_length")
        self.gridLayout.addWidget(self.label_length, 0, 2, 1, 1)
        self.label_length.setDisabled(True)
        
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("combo")
        self.comboBox.addItem("16")
        self.comboBox.addItem("24")
        self.comboBox.addItem("32")
        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 1)
        self.comboBox.setDisabled(True)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setDisabled(True)
        self.gridLayout.addWidget(self.pushButton, 0, 4, 1, 1)
        self.gridLayout_6.addWidget(self.widget, 2, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralWidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_plaintext = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_plaintext.setObjectName("lineEdit_plaintext")
        self.lineEdit_plaintext.setDisabled(True)
        self.gridLayout_3.addWidget(self.lineEdit_plaintext, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.widget_3, 3, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralWidget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_cyphertext = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_cyphertext.setObjectName("lineEdit_cyphertext")
        self.lineEdit_cyphertext.setDisabled(True)
        self.gridLayout_4.addWidget(self.lineEdit_cyphertext, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.widget_4, 4, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.centralWidget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_encrypt = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_encrypt.setObjectName("pushButton_encrypt")
        self.pushButton_encrypt.setDisabled(True)
        self.gridLayout_5.addWidget(self.pushButton_encrypt, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setDisabled(True)
        self.gridLayout_5.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.widget_5, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 498, 27))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.des = des(b"boogyman", CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AES and DES"))
        self.label.setText(_translate("MainWindow", "AES and DES"))
        self.radioButton_AES.setText(_translate("MainWindow", "AES (CTR)"))
        self.radioButton_DES.setText(_translate("MainWindow", "DES (CBC)"))
        self.label_2.setText(_translate("MainWindow", "Key:"))
        self.label_length.setText(_translate("MainWindow", "Length:"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.label_3.setText(_translate("MainWindow", "Plaintext:"))
        self.label_4.setText(_translate("MainWindow", "Cyphertext:"))
        self.pushButton_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.pushButton_3.setText(_translate("MainWindow", "Decrypt"))


    def HexToByte(self, hexStr):
        """
        Convert a string hex byte values into a byte string. The Hex Byte values may
        or may not be space separated.
        """
        # The list comprehension implementation is fractionally slower in this case    
        #
        #    hexStr = ''.join( hexStr.split(" ") )
        #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \
        #                                   for i in range(0, len( hexStr ), 2) ] )
    
        bytes = []

        hexStr = ''.join( hexStr.split(" ") )

        for i in range(0, len(hexStr), 2):
            bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

        return ''.join( bytes )

    def generateDESkey(self):
        rand_string = ''.join(random.choice(string.letters + string.digits + string.punctuation) for i in range(8))
        self.lineEdit_key.setText(rand_string)
        self.key = self.lineEdit_key.text().encode('latin-1')

    def encryptDES(self):
        #add check for existance of key 8 bytes;
        if len(self.lineEdit_key.text()) != 8:
            self.showdialog()
        else:
            if self.des is not None:
                self.des.setKey(self.lineEdit_key.text().encode('latin-1'))
                self.d = self.des.encrypt(self.lineEdit_plaintext.text().encode('latin-1'))
                self.lineEdit_cyphertext.setText(''.join( [ "%02X " % ord( x ) for x in self.d ] ).strip())
            else:
                print "here"

    def decryptDES(self):
        if self.des is not None:
            self.des.setKey(self.lineEdit_key.text().encode('latin-1'))
            self.d = self.HexToByte(self.lineEdit_cyphertext.text())
            self.lineEdit_plaintext.setText(self.des.decrypt(self.d))
        else:
            print "decrypt"
            #encode smting first
    
    def keyChangedDES(self, text):
        if len(self.lineEdit_key.text()) == 8:
            self.key = self.lineEdit_key.text().encode('latin-1')
            self.pushButton_encrypt.setEnabled(True)
            if len(self.lineEdit_cyphertext.text()) != 0:
                self.pushButton_3.setEnabled(True)
            else:
                self.pushButton_3.setEnabled(False)
        else:
            self.pushButton_encrypt.setEnabled(False)

    def cyphertextChangedDES(self, text):
        if len(self.lineEdit_cyphertext.text()) != 0:
            if len(self.lineEdit_key.text()) == 8:
                self.pushButton_3.setEnabled(True)
            else:
                self.pushButton_3.setEnabled(False)
        else:
            self.pushButton_3.setEnabled(False)

    def DES(self, checked):
        try:
            self.pushButton.disconnect()
        except:
            pass
        self.pushButton.pressed.connect(lambda:self.generateDESkey())
        self.lineEdit_key.setEnabled(True)
        self.pushButton.setEnabled(True)

        try:
            self.pushButton_encrypt.disconnect()
        except:
            pass
        self.pushButton_encrypt.pressed.connect(lambda:self.encryptDES())

        try:
            self.pushButton_3.disconnect()
        except:
            pass
        self.pushButton_3.pressed.connect(lambda:self.decryptDES())

        try:
            self.lineEdit_key.disconnect()
        except:
            pass
        self.lineEdit_key.textChanged.connect(functools.partial(self.keyChangedDES))
        self.lineEdit_key.clear()

        try:
            self.lineEdit_cyphertext.disconnect()
        except:
            pass
        self.lineEdit_cyphertext.textChanged.connect(functools.partial(self.cyphertextChangedDES))
        self.lineEdit_cyphertext.clear()
        self.lineEdit_cyphertext.setEnabled(True)

        self.lineEdit_plaintext.setEnabled(True)
        self.lineEdit_plaintext.clear()

        self.label_length.setDisabled(True)
        self.comboBox.setDisabled(True)

        if len(self.lineEdit_key.text()) != 8:
            self.pushButton_encrypt.setDisabled(True)
            self.pushButton_3.setDisabled(True)
        else:
            self.pushButton_encrypt.setDisabled(False)
            if len(self.lineEdit_cyphertext.text()) != 0:
                self.pushButton_3.setDisabled(False)

    def generateAESkey(self):
        if self.comboBox.currentText() == "16":
            rand_string = ''.join(random.choice(string.letters + string.digits + string.punctuation) for i in range(16))
            self.lineEdit_key.setText(rand_string)
            self.key = self.lineEdit_key.text().encode('latin-1')
        if self.comboBox.currentText() == "24":
            rand_string = ''.join(random.choice(string.letters + string.digits + string.punctuation) for i in range(24))
            self.lineEdit_key.setText(rand_string)
            self.key = self.lineEdit_key.text().encode('latin-1')
        if self.comboBox.currentText() == "32":
            rand_string = ''.join(random.choice(string.letters + string.digits + string.punctuation) for i in range(32))
            self.lineEdit_key.setText(rand_string)
            self.key = self.lineEdit_key.text().encode('latin-1')

    def encryptAES(self):
        try:
            self.lineEdit_plaintext.text().decode('ascii')
        except:
            self.showdialog()
        else:
            aes = pyaes.AESModeOfOperationCTR(self.key)
            self.ciphertext = aes.encrypt(self.lineEdit_plaintext.text().encode('latin-1'))
            self.lineEdit_cyphertext.setText(''.join( [ "%02X " % ord( x ) for x in self.ciphertext ] ).strip())

    def decryptAES(self):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        self.decrypted = aes.decrypt(self.HexToByte(self.lineEdit_cyphertext.text()))
        self.lineEdit_plaintext.setText(self.decrypted)

    def keyChangedAES(self):
        self.key = self.lineEdit_key.text().encode('latin-1')

    def cyphertextChangedAES(self):
        if len(self.lineEdit_cyphertext.text()) != 0:
            self.keyLengthChangedAES()
        else:
            self.pushButton_3.setEnabled(False)

    def keyLengthChangedAES(self):
        if self.comboBox.currentText() == "16":
            if len(self.lineEdit_key.text()) == 16:
                self.keyChangedAES()
                self.pushButton_encrypt.setEnabled(True)
                if len(self.lineEdit_cyphertext.text()) != 0:
                    self.pushButton_3.setEnabled(True)
                else:
                    self.pushButton_3.setEnabled(False)
            else:
                self.pushButton_encrypt.setEnabled(False)
                self.pushButton_3.setEnabled(False)
        elif self.comboBox.currentText() == "24":
            if len(self.lineEdit_key.text()) == 24:
                self.keyChangedAES()
                self.pushButton_encrypt.setEnabled(True)
                if len(self.lineEdit_cyphertext.text()) != 0:
                    self.pushButton_3.setEnabled(True)
                else:
                    self.pushButton_3.setEnabled(False)
            else:
                self.pushButton_encrypt.setEnabled(False)
                self.pushButton_3.setEnabled(False)
        elif self.comboBox.currentText() == "32":
            if len(self.lineEdit_key.text()) == 32:
                self.keyChangedAES()
                self.pushButton_encrypt.setEnabled(True)
                if len(self.lineEdit_cyphertext.text()) != 0:
                    self.pushButton_3.setEnabled(True)
                else:
                    self.pushButton_3.setEnabled(False)
            else:
                self.pushButton_encrypt.setEnabled(False)
                self.pushButton_3.setEnabled(False)
        else:
            self.pushButton_encrypt.setEnabled(False)
            self.pushButton_3.setEnabled(False)

    def AES(self):
        try:
            self.pushButton.disconnect()
        except:
            pass
        self.pushButton.pressed.connect(lambda:self.generateAESkey())
        self.lineEdit_key.setEnabled(True)
        self.pushButton.setEnabled(True)

        try:
            self.pushButton_encrypt.disconnect()
        except:
            pass
        self.pushButton_encrypt.pressed.connect(lambda:self.encryptAES())

        try:
            self.pushButton_3.disconnect()
        except:
            pass
        self.pushButton_3.pressed.connect(lambda:self.decryptAES())

        try:
            self.lineEdit_key.disconnect()
        except:
            pass
        self.lineEdit_key.textChanged.connect(functools.partial(self.keyLengthChangedAES))
        self.lineEdit_key.clear()

        try:
            self.lineEdit_cyphertext.disconnect()
        except:
            pass
        self.lineEdit_cyphertext.textChanged.connect(functools.partial(self.cyphertextChangedAES))
        self.lineEdit_cyphertext.clear()
        self.lineEdit_cyphertext.setEnabled(True)

        self.lineEdit_plaintext.setEnabled(True)
        self.lineEdit_plaintext.clear()

        self.label_length.setDisabled(False)
        self.comboBox.setDisabled(False)

        try:
            self.comboBox.disconnect()
        except:
            pass
        self.comboBox.activated.connect(functools.partial(self.keyLengthChangedAES))

        if len(self.lineEdit_key.text()) != 8:
            self.pushButton_encrypt.setDisabled(True)
            self.pushButton_3.setDisabled(True)
        else:
            self.pushButton_encrypt.setDisabled(False)
            if len(self.lineEdit_cyphertext.text()) != 0:
                self.pushButton_3.setDisabled(False)

    def showdialog(self):
        d = QtWidgets.QMessageBox(self.centralWidget)
        # label = QtWidgets.QLabel("Text must be in unicode!", d)
        # b1 =  QtWidgets.QPushButton("Ok",d)
        # b1.move(50,50)
        d.setWindowTitle("Warning!")
        d.setText("Text must be in unicode!")
        d.setModal(True)
        d.exec_()

    def connectUi(self, Mainwindow):
        self.radioButton_AES.toggled.connect(lambda:self.AES())
        self.radioButton_DES.toggled.connect(functools.partial(self.DES))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connectUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

