import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mainUI import Ui_Form
import time

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.pushButton_Click)       
        self.show()

    def pushButton_Click(self):
        ticks= time.strftime("%Y-%m-%d %H:%m:%S",time.localtime())
        global changebtn_bool
        if changebtn_bool:
            labelstring = ticks
            changebtn_bool =False
        else:
            labelstring = ticks
            changebtn_bool =True
        self.ui.label_show.setText(labelstring)       
        self.ui.progressBar.setValue(int(time.strftime("%S",time.localtime())))
app = QApplication(sys.argv)
changebtn_bool =False
w=AppWindow()
w.show()
app.exec_()