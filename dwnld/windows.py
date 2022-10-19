from PyQt5.QtWidgets import QApplication,\
    QAction, \
    QTabWidget, \
    QWidget,  \
    QLabel, \
    QMainWindow,\
    QStatusBar,\
    QToolBar,\
    QGridLayout,\
    QFileDialog, \
    QVBoxLayout , \
    QHBoxLayout, \
    QLineEdit, QPlainTextEdit, QPushButton, QSpinBox
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtCore import Qt
import os

print(os.getenv("HOME"))

# super() function in Python makes class inheritance more manageable and extensible.
# The function returns a temporary object that allows reference to a parent class by the keyword 'super'


# Making a class of main app window inheriting from QMainWindow
class Window(QMainWindow):
    # Adding a constructor taking parent window
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Pobieranie z YT')
        self.setGeometry(40, 40, 800, 800)
        # self.createTabs()
        self.opened_txt = ''
        layout = QVBoxLayout(self)

    def open_file(self):
        widget = self.centralWidget()
        fileName, selectedFilter = QFileDialog.getOpenFileName(widget,
                                                               "Choose an image", "", "JPG (*.jpg);; PNG (*.png)")
        if fileName:
            # label = QLabel(widget)
            print("tried opening")
            pixmap = QPixmap(fileName)
            resized_pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio)
            # label.setPixmap(pixmap)
            # window.resize(pixmap.width(), pixmap.height())
            self.picture.setPixmap(resized_pixmap)

    def destination(self):
        return QFileDialog.getExistingDirectory(self, str("Open Directory"), "/home",
                                                QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

    # def save_as(self):
    #     print("save as")
    #     name, selectedFilter = QFileDialog.getSaveFileName(self, 'Save File')
    #     file = open(name, 'w')
    #     content = self.text.toPlainText()
    #     file.write(content)
    #     file.close()
    #     self.opened_txt = name
    #     return 'a'



        # Adding widget to window as a central widget
        # self.setCentralWidget(self.all_tabs)
        # self.setLayout(layout)


# Uruchomienie okna
# widget = QWidget()
# widget.show()

app = QApplication([])  # window initialization
win = Window()
win.show()
app.exec_()
