from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Liczenie pkt na PG 2020")
        icon = QIcon("student.png")
        self.setWindowIcon(icon)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(300, 300)
        self.initUI()

    def initUI(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Pkt z matematyki: ")
        self.label1.move(10, 0)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Pkt z p. dod: ")
        self.label2.move(10, 40)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Pkt z j. polskiego: ")
        self.label3.move(10, 80)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText("Pkt z j. obcego: ")
        self.label4.move(10, 120)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Oblicz")
        self.b1.move(100, 230)
        self.b1.clicked.connect(self.submit)

        self.mat = QLineEdit(self)
        self.mat.move(100, 5)
        self.mat.setFixedSize(30, 20)

        self.pdod = QLineEdit(self)
        self.pdod.move(100, 45)
        self.pdod.setFixedSize(30, 20)

        self.pol = QLineEdit(self)
        self.pol.move(100, 85)
        self.pol.setFixedSize(30, 20)

        self.ang = QLineEdit(self)
        self.ang.move(100, 125)
        self.ang.setFixedSize(30, 20)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText("Rozszerzenie: ")
        self.label5.move(150, 0)

        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText("Rozszerzenie: ")
        self.label6.move(150, 40)

        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText("Rozszerzenie: ")
        self.label7.move(150, 80)

        self.label8 = QtWidgets.QLabel(self)
        self.label8.setText("Rozszerzenie: ")
        self.label8.move(150, 120)

        self.cb_mat = QtWidgets.QCheckBox(self)
        self.cb_mat.move(225, 2)

        self.cb_pdod = QtWidgets.QCheckBox(self)
        self.cb_pdod.move(225, 42)

        self.cb_pol = QtWidgets.QCheckBox(self)
        self.cb_pol.move(225, 82)

        self.cb_ang = QtWidgets.QCheckBox(self)
        self.cb_ang.move(225, 122)

        self.result = QtWidgets.QLabel(self)
        self.result.move(130, 200)

    def submit(self):
        try:
            self.result.move(130, 200)
            self.result.setText(str(self.counting()) + '/220')
        except:
            self.result.move(82, 200)
            self.result.setText("Podaj poprawne wartości")
        self.update_size()

    def update_size(self):
        self.result.adjustSize()

    def counting(self):
        mat_pkt = int(self.mat.text())
        pdod_pkt = int(self.pdod.text())
        pol_pkt = int(self.pol.text()) * 0.1
        ang_pkt = int(self.ang.text()) * 0.1
        if mat_pkt not in range(0, 101) or pdod_pkt not in range(0, 101) or int(self.pol.text()) not in range(0, 101) or int(self.ang.text()) not in range(0, 101):
            return "" + 1
        if not self.cb_mat.isChecked():
            mat_pkt *= 0.4
        if not self.cb_pdod.isChecked():
            pdod_pkt *= 0.4
        if not self.cb_pol.isChecked():
            pol_pkt *= 0.4
        if not self.cb_ang.isChecked():
            ang_pkt *= 0.4

        wynik = mat_pkt + pdod_pkt + pol_pkt + ang_pkt
        return round(wynik, 2)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
