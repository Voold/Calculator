from PyQt5 import QtCore, QtGui, QtWidgets
import CalcFunc


class Ui_MainWindow(object):
    # res = None
    operations = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 250)
        MainWindow.setStyleSheet("\n"
                                 "background-color: rgb(9, 9, 9);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(200, 250))
        self.centralwidget.setObjectName("centralwidget")
        self.RES = QtWidgets.QLabel(self.centralwidget)
        self.RES.setGeometry(QtCore.QRect(0, 0, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RES.sizePolicy().hasHeightForWidth())
        self.RES.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.RES.setFont(font)
        self.RES.setStyleSheet("color:white;\n"
                               "background-color: rgb(62, 62, 62);\n"
                               "border-bottom: 3px solid #684000;\n"
                               "")
        self.RES.setObjectName("RES")
        self.BUT1 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT1.setGeometry(QtCore.QRect(0, 50, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT1.setFont(font)
        self.BUT1.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT1.setObjectName("BUT1")
        self.BUT2 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT2.setGeometry(QtCore.QRect(50, 50, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT2.setFont(font)
        self.BUT2.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT2.setObjectName("BUT2")
        self.BUT3 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT3.setGeometry(QtCore.QRect(100, 50, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT3.setFont(font)
        self.BUT3.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT3.setObjectName("BUT3")
        self.BUT4 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT4.setGeometry(QtCore.QRect(0, 100, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT4.setFont(font)
        self.BUT4.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT4.setObjectName("BUT4")
        self.BUT6 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT6.setGeometry(QtCore.QRect(100, 100, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT6.setFont(font)
        self.BUT6.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT6.setObjectName("BUT6")
        self.BUT5 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT5.setGeometry(QtCore.QRect(50, 100, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT5.setFont(font)
        self.BUT5.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT5.setObjectName("BUT5")
        self.BUT7 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT7.setGeometry(QtCore.QRect(0, 150, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT7.setFont(font)
        self.BUT7.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT7.setObjectName("BUT7")
        self.BUT9 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT9.setGeometry(QtCore.QRect(100, 150, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT9.setFont(font)
        self.BUT9.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT9.setObjectName("BUT9")
        self.BUT8 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT8.setGeometry(QtCore.QRect(50, 150, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT8.setFont(font)
        self.BUT8.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT8.setObjectName("BUT8")
        self.BUT0 = QtWidgets.QPushButton(self.centralwidget)
        self.BUT0.setGeometry(QtCore.QRect(0, 200, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BUT0.setFont(font)
        self.BUT0.setStyleSheet("border-radius:15px;\n"
                                "border: 1px solid #bd8009;\n"
                                "background-color: rgb(255, 170, 0);")
        self.BUT0.setObjectName("BUT0")
        self.BUTequ = QtWidgets.QPushButton(self.centralwidget)
        self.BUTequ.setGeometry(QtCore.QRect(100, 200, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BUTequ.setFont(font)
        self.BUTequ.setStyleSheet("border-radius:15px;\n"
                                  "border: 1px solid  #820000;\n"
                                  "background-color: rgb(255, 62, 62);\n"
                                  "")
        self.BUTequ.setObjectName("BUTequ")
        self.BUTprocent = QtWidgets.QPushButton(self.centralwidget)
        self.BUTprocent.setGeometry(QtCore.QRect(150, 150, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BUTprocent.setFont(font)
        self.BUTprocent.setStyleSheet("border-radius:15px;\n"
                                      "border: 1px solid  #820000;\n"
                                      "background-color: rgb(255, 62, 62);")
        self.BUTprocent.setObjectName("BUTprocent")
        self.BUTminus = QtWidgets.QPushButton(self.centralwidget)
        self.BUTminus.setGeometry(QtCore.QRect(150, 100, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BUTminus.setFont(font)
        self.BUTminus.setStyleSheet("border-radius:15px;\n"
                                    "border: 1px solid  #820000;\n"
                                    "background-color: rgb(255, 62, 62);")
        self.BUTminus.setObjectName("BUTminus")
        self.BUTplus = QtWidgets.QPushButton(self.centralwidget)
        self.BUTplus.setGeometry(QtCore.QRect(150, 50, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BUTplus.setFont(font)
        self.BUTplus.setStyleSheet("border-radius:15px;\n"
                                   "border: 1px solid  #820000;\n"
                                   "background-color: rgb(255, 62, 62);")
        self.BUTplus.setObjectName("BUTplus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.RES.setText(_translate("MainWindow", "0"))
        self.BUT1.setText(_translate("MainWindow", "1"))
        self.BUT2.setText(_translate("MainWindow", "2"))
        self.BUT3.setText(_translate("MainWindow", "3"))
        self.BUT4.setText(_translate("MainWindow", "4"))
        self.BUT6.setText(_translate("MainWindow", "6"))
        self.BUT5.setText(_translate("MainWindow", "5"))
        self.BUT7.setText(_translate("MainWindow", "7"))
        self.BUT9.setText(_translate("MainWindow", "9"))
        self.BUT8.setText(_translate("MainWindow", "8"))
        self.BUT0.setText(_translate("MainWindow", "0"))
        self.BUTequ.setText(_translate("MainWindow", "="))
        self.BUTprocent.setText(_translate("MainWindow", "%"))
        self.BUTminus.setText(_translate("MainWindow", "-"))
        self.BUTplus.setText(_translate("MainWindow", "+"))

    def add_functions(self):

        # for var in [self.BUT1, self.BUT2, self.BUT3, self.BUT4, self.BUT5, self.BUT6, self.BUT7, self.BUT8, self.BUT9]:
        #     var.clicked.connect(lambda: CalcFunc.write_number(self.RES, var.text()))

        self.BUT0.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT0.text()))
        self.BUT1.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT1.text()))
        self.BUT2.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT2.text()))
        self.BUT3.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT3.text()))
        self.BUT4.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT4.text()))
        self.BUT5.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT5.text()))
        self.BUT6.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT6.text()))
        self.BUT7.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT7.text()))
        self.BUT8.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT8.text()))
        self.BUT9.clicked.connect(lambda: CalcFunc.write_number(self.RES, self.BUT9.text()))

        self.BUTplus.clicked.connect(lambda: CalcFunc.operate(CalcFunc.plus, self.RES, self.operations))
        self.BUTminus.clicked.connect(lambda: CalcFunc.operate(CalcFunc.minus, self.RES, self.operations))
        self.BUTprocent.clicked.connect(lambda: CalcFunc.operate(CalcFunc.percent, self.RES, self.operations))
        self.BUTequ.clicked.connect(lambda: CalcFunc.equ(self.RES, self.operations))

    # def add_functions(self):
    #     self.BUT0.clicked.connect(lambda: self.write_number(self.BUT0.text()))
    #     self.BUT1.clicked.connect(lambda: self.write_number(self.BUT1.text()))
    #     self.BUT2.clicked.connect(lambda: self.write_number(self.BUT2.text()))
    #     self.BUT3.clicked.connect(lambda: self.write_number(self.BUT3.text()))
    #     self.BUT4.clicked.connect(lambda: self.write_number(self.BUT4.text()))
    #     self.BUT5.clicked.connect(lambda: self.write_number(self.BUT5.text()))
    #     self.BUT6.clicked.connect(lambda: self.write_number(self.BUT6.text()))
    #     self.BUT7.clicked.connect(lambda: self.write_number(self.BUT7.text()))
    #     self.BUT8.clicked.connect(lambda: self.write_number(self.BUT8.text()))
    #     self.BUT9.clicked.connect(lambda: self.write_number(self.BUT9.text()))
    #     # self.BUTplus.clicked.connect(lambda: self.result(self.plus, self.RES.text()))
    #     # self.BUTminus.clicked.connect(lambda: self.result(self.minus, self.RES.text()))
    #     # self.BUTprocent.clicked.connect(lambda: self.result(self.procent, self.RES.text()))
    #     # self.BUTequ.clicked.connect(lambda: self.result(self.equ, self.RES.text()))
    #     self.BUTplus.clicked.connect(lambda: self.operate(self.plus))
    #     self.BUTminus.clicked.connect(lambda: self.operate(self.minus))
    #     self.BUTprocent.clicked.connect(lambda: self.operate(self.procent))
    #     self.BUTequ.clicked.connect(lambda: self.operate(self.equ))

    # def write_number(self, number):
    #     if self.RES.text() != "0":
    #         self.RES.setText(self.RES.text() + number)
    #     else:
    #         self.RES.clear()
    #         self.RES.setText(number)
    #
    # def operate(self,func):
    #     self.res = int(self.RES.text())
    #     self.operations.append([func,self.res])
    #     self.RES.clear()
    #     print(self.operations)
    #
    # def result(self, func, num):
    #     if self.res is not None:
    #         func(num)
    #     else:
    #         self.res = int(num)
    #         self.RES.clear()
    #
    # def minus(self, num):
    #     self.res -= int(num)
    #     self.RES.clear()
    #
    # def plus(self, num):
    #     self.res += int(num)
    #     self.RES.clear()
    #
    # def procent(self, num):
    #     num+=1
    #     print(num)
    # def equ(self, num):
    #     self.res = 4
    #     self.operations[0][0](4)
    #     self.RES.setText(str(self.res))
    #     # self.res = None


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
