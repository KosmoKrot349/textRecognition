from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.reader = TesseratReader()

        grid = QGridLayout()
        self.btn = QPushButton('Select')
        self.image = QLabel('your picture will here')
        self.text = QTextEdit()


        grid.addWidget(self.btn, 1,1)
        grid.addWidget(self.image,1,2)
        grid.addWidget(self.text,2,1,1,2)
        self.btn.clicked.connect(self.showDialog)


        self.setLayout(grid)

        self.show()


    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home',"Image Files (*.png *.jpg *.bmp)")[0]
        pixmap = QPixmap(fname)
        self.image.setPixmap(pixmap)
        self.text.setText(self.reader.read(fname))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())




