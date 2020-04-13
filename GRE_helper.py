import xlrd
import random
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from GRE_UI import Ui_Frame


class GRE_Helper(QtWidgets.QMainWindow, Ui_Frame):
    def __init__(self):
        self.file = xlrd.open_workbook("data/GRE.xlsx")
        self.table = self.file.sheet_by_name("GRE")
        # # 随机模式
        # self.seed = random.randint(0, self.table.nrows - 1)
        # self.row = self.table.row_values(self.seed)
        # 练习模式
        self.row = self.table.row_values(0)
        self.num = 1
        super(GRE_Helper, self).__init__()
        self.setupUi(self)
        self.showButton.clicked.connect(lambda: self.show_word())
        self.coverButton.clicked.connect(lambda: self.cover_word())
        self.nextButton.clicked.connect(lambda: self.next_word())
        self.word.setText(str(self.row[0]))
        self.count.setText("Count: 1")

    def show_word(self):
        exp = ""
        length = len(self.row)
        for i in range(1, length, 2):
            temp = str(self.row[i]) + " " + str(self.row[i + 1]) + "\n"
            exp += temp
        self.explain.setPlainText(exp)

    def cover_word(self):
        self.explain.setPlainText("")

    def next_word(self):
        # # 随机模式
        # self.seed = random.randint(0, self.table.nrows - 1)
        # self.row = self.table.row_values(self.seed)
        # 练习模式
        self.row = self.table.row_values(self.num)
        self.word.setText(str(self.row[0]))
        self.explain.setPlainText("")
        self.num += 1
        self.count.setText("Count: %d" % self.num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = GRE_Helper()
    ui.show()
    sys.exit(app.exec_())
