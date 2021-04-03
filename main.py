import sys  
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import gui  

class ExampleApp(QtWidgets.QMainWindow, gui.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  
    
    
    def accept(self):                                       
        if self.textEdit.toPlainText() == self.Eng[f'{self.rand}']:
            self.close()
        else:
            dialog = QtWidgets.QMessageBox.information(self, 'Delete?', 'Wrong word!', buttons = QtWidgets.QMessageBox.Ok)
def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp() 
    window.show() 
    app.exec_()  

if __name__ == '__main__':  
    main() 