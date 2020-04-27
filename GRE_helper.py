import xlrd
import random
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from GRE_UI import Ui_Frame
from Practice_mode_UI import Ui_MainWindow


# Main window (Random Evil Mode)
class GREHelper(QtWidgets.QMainWindow, Ui_Frame):
    def __init__(self):
        # File
        self.file = xlrd.open_workbook("data/GRE.xlsx")
        self.table = self.file.sheet_by_name("GRE")
        # random seed
        self.seed = random.randint(0, self.table.nrows - 1)
        # selected row
        self.row = self.table.row_values(self.seed)
        # count num
        self.num = 1
        super(GREHelper, self).__init__()
        self.setupUi(self)
        # buttons
        self.showButton.clicked.connect(lambda: self.show_word())
        self.coverButton.clicked.connect(lambda: self.cover_word())
        self.nextButton.clicked.connect(lambda: self.next_word())
        self.shiftButton.clicked.connect(lambda: self.change_mode())
        # init word
        self.word.setText(str(self.row[0]))
        # init count
        self.count.setText("Count: 1")

    # show word func: show the explain in the textbox
    def show_word(self):
        exp = ""
        length = len(self.row)
        for i in range(1, length, 2):
            temp = str(self.row[i]) + " " + str(self.row[i + 1]) + "\n"
            exp += temp
        self.explain.setPlainText(exp)

    # cover word func: cover the explain
    def cover_word(self):
        self.explain.setPlainText("")

    # next word func: get to the next word
    def next_word(self):
        self.seed = random.randint(0, self.table.nrows - 1)
        self.row = self.table.row_values(self.seed)
        self.word.setText(str(self.row[0]))
        self.explain.setPlainText("")
        self.num += 1
        self.count.setText("Count: %d" % self.num)

    # change mode func: exchange to another mode
    def change_mode(self):
        practice.show()
        self.close()


# Practice window
class PracticeMode(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # File
        self.file = xlrd.open_workbook("data/GRE.xlsx")
        self.table = self.file.sheet_by_name("GRE")
        # init some parameters
        self.seed = 0
        self.row = []
        self.num = 1
        self.mode = 0
        self.item = 0
        super(PracticeMode, self).__init__()
        self.setupUi(self)
        # buttons
        self.showButton.clicked.connect(lambda: self.show_word())
        self.coverButton.clicked.connect(lambda: self.cover_word())
        self.nextButton.clicked.connect(lambda: self.next_word())
        self.shiftButton.clicked.connect(lambda: self.change_mode())
        self.changeButton.clicked.connect(lambda: self.change_order())
        self.confirmButton.clicked.connect(lambda: self.confirm())
        # init textarea
        self.word.setText("")
        self.count.setText("")

    # confirm func: get everything done and confirm. Decide which mode and range you are in.
    def confirm(self):
        from_point = self.fromBox.value()
        to_point = self.toBox.value()
        # for count num orderly
        self.item = self.fromBox.value()
        # start point is smaller than the end one
        if from_point < to_point:
            # Random mode
            if self.mode == 0:
                self.seed = random.randint(from_point, to_point - 1)
                self.count.setText("")
            # Orderly mode
            else:
                self.seed = from_point
                self.count.setText("Count: 1")
            self.row = self.table.row_values(self.seed)
            self.word.setText(str(self.row[0]))
        else:
            QMessageBox.critical(self, "Error", "Range error! Check and confirm!", QMessageBox.Yes)

    # show word func: same above
    def show_word(self):
        exp = ""
        length = len(self.row)
        for i in range(1, length, 2):
            temp = str(self.row[i]) + " " + str(self.row[i + 1]) + "\n"
            exp += temp
        self.explain.setPlainText(exp)

    # cover word func: same above
    def cover_word(self):
        self.explain.setPlainText("")

    # next word func: attention! Have to consider different modes
    def next_word(self):
        # Random mode
        if self.mode == 0:
            self.seed = random.randint(self.fromBox.value(), self.toBox.value() - 1)
            self.row = self.table.row_values(self.seed)
            self.word.setText(str(self.row[0]))
            self.explain.setPlainText("")
        # Orderly mode
        else:
            self.item += 1
            self.seed = self.item
            if self.seed >= self.toBox.value():
                QMessageBox.information(self, "Info", "End of test!", QMessageBox.Yes)
            else:
                self.row = self.table.row_values(self.seed)
                self.word.setText(str(self.row[0]))
                self.explain.setPlainText("")
                self.num += 1
                self.count.setText("Count: %d" % self.num)

    # change order func: when press button, change mode
    def change_order(self):
        if self.mode == 0:
            self.mode = 1
            self.changeButton.setText("Orderly")
        else:
            self.mode = 0
            self.changeButton.setText("Random")

    # change mode func: same above
    def change_mode(self):
        ranprac.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # register windows
    ranprac = GREHelper()
    practice = PracticeMode()
    # select which to show
    ranprac.show()
    sys.exit(app.exec_())
