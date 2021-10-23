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

# super() function in Python makes class inheritance more manageable and extensible.
# The function returns a temporary object that allows reference to a parent class by the keyword 'super'


# Making a class of main app window inheriting from QMainWindow
class Window(QMainWindow):
    # Adding a constructor taking parent window
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt5 Lab')
        self.setGeometry(40, 40, 800, 800)
        self.createMenu()
        self.createTabs()
        self.opened_txt = ''
        layout = QVBoxLayout(self)

    def open_file(self):
        # widget = self.centralWidget()
        widget = self.tab_1
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

    def clear_notepad(self):
        self.text.clear()
        print("clear notepad")
        return 'du'

    def open_text(self):
        widget = self.tab_2
        fileName, selectedFilter = QFileDialog.getOpenFileName(widget,
                                                               "Choose a file", "", "TXT (*.txt);; Python (*.py)")
        if fileName:
            file=open(fileName)
            content = file.read()
            self.text.setPlainText(content)
            self.opened_txt = fileName
            file.close()
        return 'pa'

    def save_text(self):
        if self.opened_txt:
            content = self.text.toPlainText()
            file = open(self.opened_txt, 'w')
            file.write(content)
            file.close()
        else:
            self.save_as()
        print("save notepad")
        return 'bl'

    def save_as(self):
        print("save as")
        name, selectedFilter = QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        content = self.text.toPlainText()
        file.write(content)
        file.close()
        self.opened_txt = name
        return 'a'

    def clear_fields(self):
        self.text_A.setText('')
        self.text_B.setText('')
        self.number_C.setValue(0)
        return 'da'

    def change_ABC(self):
        try:
            A = int(self.text_A.text())
            B = int(self.text_B.text())
            C = int(self.number_C.value())
            self.number_ABC.setText(str(A + B + C))
        except(ValueError):
            self.number_ABC.setText(self.text_A.text() + self.text_B.text() + self.number_C.text())

    def createMenu(self):
        menu = self.menuBar()

        # 'File'
        file_menu = menu.addMenu("&Window")
        file_menu.addAction('Exit', self.close)

        # 'Task 1'
        image_menu = menu.addMenu("&Image opener")

        img_opening = QAction("Open", self)
        img_opening.setShortcut("Ctrl+O")
        img_opening.triggered.connect(self.open_file)
        image_menu.addAction(img_opening)

        # 'Task 2'
        notepad_menu = menu.addMenu("'&Notepad'")

        notepad_clear = QAction("Clear", self)
        notepad_clear.setShortcut("Ctrl+L")
        notepad_clear.triggered.connect(self.clear_notepad)
        notepad_menu.addAction(notepad_clear)

        notepad_open = QAction("Open", self)
        notepad_open.setShortcut("Ctrl+P")
        notepad_open.triggered.connect(self.open_text)
        notepad_menu.addAction(notepad_open)

        notepad_save = QAction("Save", self)
        notepad_save.setShortcut("Ctrl+S")
        notepad_save.triggered.connect(self.save_text)
        notepad_menu.addAction(notepad_save)

        notepad_save = QAction("Save as", self)
        notepad_save.setShortcut("Ctrl+U")
        notepad_save.triggered.connect(self.save_as)
        notepad_menu.addAction(notepad_save)

        # 'Task 3'
        field_menu = menu.addMenu("&Field adder")

        field_clear = QAction("Clear", self)
        field_clear.setShortcut("Ctrl+R")
        field_clear.triggered.connect(self.clear_fields)
        field_menu.addAction(field_clear)

    def createTabs(self):
        # Making a widget containing tabs
        self.all_tabs = QTabWidget()

        # making separate widgets
        # tab1:
        self.tab_1 = QWidget()
        self.picture = QLabel(self)
        tab_1_layout = QHBoxLayout(self.tab_1)
        tab_1_layout.addWidget(self.picture, 0, Qt.AlignLeft | Qt.AlignTop)
        # layout = QGridLayout(self)

        # tab2:
        self.tab_2 = QWidget()
        self.text = QPlainTextEdit()  # add a text field there
        self.button_save = QPushButton("Save") # add a button - save to file
        self.button_save.clicked.connect(self.save_text)

        self.button_clear = QPushButton("Clear") # add a button - clear the notepad
        self.button_clear.clicked.connect(self.clear_notepad)

        tab_2_layout = QHBoxLayout(self.tab_2)
        tab_2_layout.addWidget(self.text)
        tab_2_layout.addWidget(self.button_save)
        tab_2_layout.addWidget(self.button_clear)

        # tab3:
        self.tab_3 = QWidget()
        self.label_A = QLabel("Field A:")
        self.text_A = QLineEdit()
        self.text_A.textChanged.connect(self.change_ABC)

        self.label_B = QLabel("Field B:")
        self.text_B = QLineEdit()
        self.text_B.textChanged.connect(self.change_ABC)

        self.label_C = QLabel("Field C:")
        self.number_C = QSpinBox()
        self.number_C.textChanged.connect(self.change_ABC)

        self.label_ABC = QLabel("Field A+B+C:")
        self.number_ABC = QLineEdit()
        self.change_ABC()

        tab_3_layout = QGridLayout(self.tab_3)
        tab_3_layout.addWidget(self.label_A, 0, 0)
        tab_3_layout.addWidget(self.text_A, 0, 1)

        tab_3_layout.addWidget(self.label_B, 1, 0)
        tab_3_layout.addWidget(self.text_B, 1, 1)

        tab_3_layout.addWidget(self.label_C, 2, 0)
        tab_3_layout.addWidget(self.number_C, 2, 1) 

        tab_3_layout.addWidget(self.label_ABC, 3, 0)
        tab_3_layout.addWidget(self.number_ABC, 3, 1)         
        layout = QGridLayout(self)

        # adding tabs to widgets
        self.all_tabs.addTab(self.tab_1, "Image viewer")
        self.all_tabs.addTab(self.tab_2, "Notepad")
        self.all_tabs.addTab(self.tab_3, "field adder")

        # Adding widget to window as a central widget
        self.setCentralWidget(self.all_tabs)
        # self.setLayout(layout)


# Uruchomienie okna
# widget = QWidget()
# widget.show()

app = QApplication([])  # window initialization
win = Window()
win.show()
app.exec_()
