                         # ***Created on 2016/11/08 by Taufiq***

import os
import sys
import GraphVariables as GV
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
                             QMainWindow,
                             QComboBox,
                             QFileDialog,
                             QApplication,
                             QPushButton,
                             QLineEdit,
                             QLabel,
                             QRadioButton,
                             QMessageBox,
                             )
from Logistics import (
                             GraphData,
                             LiveGraph
                          )


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 529, 300)
        #QWidget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        # self.QSize(529, 300)
        self.setWindowTitle("GraphPy 1.0")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        button = QPushButton('Choose File', self)
        button.setGeometry(QtCore.QRect(70, 20, 91, 31))
        button.clicked.connect(self.file_dialog)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 272, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(" ")
        label = QLabel(self)
        label.setGeometry(QtCore.QRect(70, 80, 91, 31))
        label.setObjectName("label")
        self.radioButton = QRadioButton("    Grid", self)
        self.radioButton.setGeometry(QtCore.QRect(30, 120, 82, 21))
        self.radioButton.setObjectName("radioButton")
        self.cb = QComboBox(self)
        self.cb.setGeometry(QtCore.QRect(170, 70, 121, 28))
        self.cb_2 = QComboBox(self)
        self.cb_2.setGeometry(QtCore.QRect(362, 70, 121, 28))
        label_5 = QLabel("Y-variable", self)
        label_5.setGeometry(QtCore.QRect(306, 83, 47, 13))
        label_5.setObjectName("label_3")
        label_6 = QLabel("X-variable", self)
        label_6.setGeometry(QtCore.QRect(115, 83, 47, 13))
        label_6.setObjectName("label_3")
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 120, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(382, 120, 100, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(157, 120, 100, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(93, 120, 53, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_2 = QLabel("    Title", self)
        self.label_2.setGeometry(QtCore.QRect(187, 141, 47, 13))
        self.label_2.setObjectName("label_2")
        label_3 = QLabel(" X-Label", self)
        label_3.setGeometry(QtCore.QRect(300, 141, 47, 13))
        label_3.setObjectName("label_3")
        label_4 = QLabel(" Y-Label", self)
        label_4.setGeometry(QtCore.QRect(412, 141, 47, 13))
        label_4.setObjectName("label_4")
        label_5 = QLabel("Threshold", self)
        label_5.setGeometry(QtCore.QRect(96, 141, 47, 13))
        label_5.setObjectName("label_4")
        self.pushButton_2 = QPushButton("Graph Data", self)
        self.pushButton_2.setGeometry(QtCore.QRect(355, 170, 130, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.click_graph)
        self.pushButton_3 = QPushButton("Preview File", self)
        self.pushButton_3.setGeometry(QtCore.QRect(217, 170, 130, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.preview)
        self.pushButton_4 = QPushButton("Live Mode", self)
        self.pushButton_4.setGeometry(QtCore.QRect(78, 170, 130, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.live_graph)
        self.status = self.statusBar()
        self.status.showMessage('')
        self.show()

    def file_dialog(self):
        self.cb.clear()
        self.cb_2.clear()
        f_name = QFileDialog.getOpenFileName(self, 'Choose file', 'g', ("files (*.txt *.csv *.xlsx *.xlrs *.xlr )"))
        self.file  = f_name[0]
        print(self.file)
        self.lineEdit.setText(self.file)
        self.combo(self.file)
        self.status.showMessage('File selected')

    def click_graph(self):
        if self.radioButton.isChecked():
            print("grid:true")
            grid = True
        else:
            print("grid:false")
            grid = False
        self.threshold = self.lineEdit_5.text()
        print(self.lineEdit_4.text())  # title
        print(self.lineEdit_2.text())  # x
        print(self.lineEdit_3.text())  # y
        print(int(self.lineEdit_5.text()))  # threshold
        print(str(self.get_x))
        print(str(self.get_y))
        gd = GraphData(
            self.file,
            self.lineEdit_4.text(),
            self.lineEdit_2.text(),
            self.lineEdit_3.text(),
            grid,
            self.get_x,
            self.get_y,
            float(self.lineEdit_5.text())
        )

        gd.file_type()


    def preview(self):
        print(self.file)
        os.system('"'+(self.file)+'"')

    def combo(self,file):
        print("combo function triggered")
        print(file)
        vars = GV.read_vars_beta(file)
        for i in range(0, len(vars)):
            self.cb.addItem(vars[i])
            self.cb_2.addItem(vars[i])
            print(vars[i])
        self.cb.currentIndexChanged.connect(self.combo_selected)
        self.cb_2.currentIndexChanged.connect(self.combo_selected)

    def combo_selected(self):
        x =str(self.cb.currentText())
        print ("x= ", x)
        y = str(self.cb_2.currentText())
        print("y= ", y)
        self.get_x = x
        self.get_y = y

    def get_x(self, x):
        return x

    def get_y(self, y):
        return y

    def live_graph(self):
        lv = LiveGraph(self.file)
        lv.showupdate()

    def showmessage(self, message):
        msg = self.QMessageBox()
        msg.setIcon(self.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Error!")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

app = QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
