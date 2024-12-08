import cv2
from ultralytics import YOLO
from PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys

class Main_W(QMainWindow):
    def __init__(self):
        super(Main_W,self).__init__()
        uic.loadUi('Main.ui',self)
        self.pushButton.clicked.connect(self.load)
        self.nhandien_button.clicked.connect(self.nhandien)
    def load(self):
        link =QFileDialog.getOpenFileName(filter='*.jpg *.png')
        self.Screen.setPixmap(QPixmap(link[0]))
        self.lineEdit.setText(link[0])
        lickpic = self.lineEdit.text()
        global linkchange
        linkchange = lickpic.replace('/', '//')

    def nhandien(self):
        try:
            global linkchange
            if linkchange:
                # Disable scientific notation for clarity
                # Tải mô hình (có thể thay 'yolov5s' bằng 'yolov8n', 'yolov8s', v.v.)
                model = YOLO('last.pt')

                # Đọc ảnh
                img_path = linkchange # Đường dẫn tới ảnh của bạn
                img = cv2.imread(img_path)

                # Nhận diện
                results = model(img)
                results = results[0]

                # Hiển thị kết quả
                results.show()  # Hiển thị ảnh với bounding boxes
                # results.save('output.jpg')  # Lưu kết quả
            else:
                print("Linkchange is not set.")
        except NameError:
            print("linkchange is not defined as a global variable.")

app = QApplication(sys.argv)

# widget = QtWidgets.QStackedWidget()
Main_f =Main_W()
Main_f.show()
app.exec()


