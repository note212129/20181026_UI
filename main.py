import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from mainUI import Ui_Form
import time, threading

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pushButton_Click)   
        timer = threading.Timer(1,self.fun_timer)
        timer.start()    
        self.show()   

    def fun_timer(self):
        ticks= time.strftime("%Y-%m-%d %H:%m:%S",time.localtime())
        self.ui.lcdNumber.display(ticks)
        global timer
        timer = threading.Timer(1,self.fun_timer)
        timer.start()

    def pushButton_Click(self):
        
        NumberCount = self.ui.lcdNumber.value()
        QMessageBox.about(self,'PyQt',str(NumberCount))
        NumberCount +=1
        self.ui.lcdNumber.display(NumberCount)

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
        global count
        if count >3:
            buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want Exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                global app
                app.exit()
            else:
                print('No clicked.') 
        else:
            count+=1
app = QApplication(sys.argv)
changebtn_bool =False
count=0
w=AppWindow()
w.show()
app.exec_()
timer.cancel()