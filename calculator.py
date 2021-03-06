# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator_jeng.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(755, 911)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        Form.setFont(font)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:1, y2:0.0113636, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255))")
        self.key_label = QtWidgets.QLabel(Form)
        self.key_label.setGeometry(QtCore.QRect(30, 20, 691, 191))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.key_label.setFont(font)
        self.key_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.key_label.setObjectName("key_label")
        self.key_7 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('7'))
        self.key_7.setGeometry(QtCore.QRect(40, 280, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_7.setFont(font)
        self.key_7.setObjectName("key_7")
        self.key_8 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('8'))
        self.key_8.setGeometry(QtCore.QRect(220, 280, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_8.setFont(font)
        self.key_8.setObjectName("key_8")
        self.key_9 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('9'))
        self.key_9.setGeometry(QtCore.QRect(390, 280, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_9.setFont(font)
        self.key_9.setObjectName("key_9")
        self.key_divide = QtWidgets.QPushButton(Form, clicked= lambda: self.func('/'))
        self.key_divide.setGeometry(QtCore.QRect(570, 280, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_divide.setFont(font)
        self.key_divide.setObjectName("key_divide")
        self.key_4 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('4'))
        self.key_4.setGeometry(QtCore.QRect(40, 410, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_4.setFont(font)
        self.key_4.setObjectName("key_4")
        self.key_5 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('5'))
        self.key_5.setGeometry(QtCore.QRect(220, 410, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_5.setFont(font)
        self.key_5.setObjectName("key_5")
        self.key_6 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('6'))
        self.key_6.setGeometry(QtCore.QRect(390, 410, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_6.setFont(font)
        self.key_6.setObjectName("key_6")
        self.key_star = QtWidgets.QPushButton(Form, clicked= lambda: self.func('*'))
        self.key_star.setGeometry(QtCore.QRect(570, 410, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_star.setFont(font)
        self.key_star.setObjectName("key_star")
        self.key_1 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('1'))
        self.key_1.setGeometry(QtCore.QRect(40, 550, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_1.setFont(font)
        self.key_1.setObjectName("key_1")
        self.key_3 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('3'))
        self.key_3.setGeometry(QtCore.QRect(390, 550, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_3.setFont(font)
        self.key_3.setObjectName("key_3")
        self.key_2 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('2'))
        self.key_2.setGeometry(QtCore.QRect(220, 550, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_2.setFont(font)
        self.key_2.setObjectName("key_2")
        self.key_C = QtWidgets.QPushButton(Form, clicked= lambda: self.ceandcanddot('c'))
        self.key_C.setGeometry(QtCore.QRect(70, 800, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_C.setFont(font)
        self.key_C.setObjectName("key_C")
        self.key_plus = QtWidgets.QPushButton(Form, clicked= lambda: self.func('+'))
        self.key_plus.setGeometry(QtCore.QRect(570, 680, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_plus.setFont(font)
        self.key_plus.setObjectName("key_plus")
        self.key_dot = QtWidgets.QPushButton(Form, clicked= lambda: self.ceandcanddot('.'))
        self.key_dot.setGeometry(QtCore.QRect(390, 680, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_dot.setFont(font)
        self.key_dot.setObjectName("key_dot")
        self.key_0 = QtWidgets.QPushButton(Form, clicked= lambda: self.num('0'))
        self.key_0.setGeometry(QtCore.QRect(220, 680, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_0.setFont(font)
        self.key_0.setObjectName("key_0")
        self.key_equal = QtWidgets.QPushButton(Form, clicked= lambda: self.equal())
        self.key_equal.setGeometry(QtCore.QRect(40, 680, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_equal.setFont(font)
        self.key_equal.setObjectName("key_equal")
        self.key_minus = QtWidgets.QPushButton(Form, clicked= lambda: self.func('-'))
        self.key_minus.setGeometry(QtCore.QRect(570, 550, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_minus.setFont(font)
        self.key_minus.setObjectName("key_minus")
        self.key_CE = QtWidgets.QPushButton(Form, clicked= lambda: self.ceandcanddot('ce'))
        self.key_CE.setGeometry(QtCore.QRect(400, 800, 321, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key_CE.setFont(font)
        self.key_CE.setObjectName("key_CE")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.key_label.setText(_translate("Form", "0"))
        self.key_7.setText(_translate("Form", "7"))
        self.key_8.setText(_translate("Form", "8"))
        self.key_9.setText(_translate("Form", "9"))
        self.key_divide.setText(_translate("Form", "/"))
        self.key_4.setText(_translate("Form", "4"))
        self.key_5.setText(_translate("Form", "5"))
        self.key_6.setText(_translate("Form", "6"))
        self.key_star.setText(_translate("Form", "*"))
        self.key_1.setText(_translate("Form", "1"))
        self.key_3.setText(_translate("Form", "3"))
        self.key_2.setText(_translate("Form", "2"))
        self.key_C.setText(_translate("Form", "C"))
        self.key_plus.setText(_translate("Form", "+"))
        self.key_dot.setText(_translate("Form", "."))
        self.key_0.setText(_translate("Form", "0"))
        self.key_equal.setText(_translate("Form", "="))
        self.key_minus.setText(_translate("Form", "-"))
        self.key_CE.setText(_translate("Form", "CE"))

    def num(self, pressed):
        screen = self.key_label.text()
        if self.key_label.text() == '0':
            self.key_label.setText(pressed)
        else:
            self.key_label.setText(f'{self.key_label.text()}{pressed}')

    def equal(self):
        answer = eval(self.key_label.text())
        try:
            last = str(answer)
            if len(last) <= 9:
                self.key_label.setText(last)
            else:
                self.key_label.setText('error')
        except:
            self.key_label.setText('error')

    def ceandcanddot(self, pressed):
        screen = self.key_label.text()
        if pressed == '.':
            if '.' in screen:
                pass
            else:
                self.key_label.setText(f'{screen}.')
        if pressed == "ce":
            AAA = self.key_label.text()
            self.key_label.setText(AAA[:-1])
        if pressed == "c":
            self.key_label.setText("0")

    def func(self,pressed):
        if self.key_label.text() == '0':
            pass
        else:
            self.key_label.setText(f'{self.key_label.text()}{pressed}')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
