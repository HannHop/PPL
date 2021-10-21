from PyQt5.QtWidgets import QApplication,\
    QAction, \
    QTabWidget, \
    QWidget,  \
    QLabel, \
    QMainWindow,\
    QStatusBar,\
    QToolBar,\
    QGridLayout,\
    QFileDialog
from PyQt5.QtGui import QPixmap, QKeySequence

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
            # label.setPixmap(pixmap)
            # window.resize(pixmap.width(), pixmap.height())
            picture.setPixmap(pixmap)

    def clear_notepad(self):
        print("clear notepad")
        return 'du'

    def open_text(self):
        return 'pa'

    def save_text(self):
        return 'bl'

    def save_as(self):
        return 'a'

    def clear_fields(self):
        return 'da'

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
        # Tworzenie widżetu posiadającego zakładki
        self.all_tabs = QTabWidget()

        # making separate widgets
        self.tab_1 = QWidget()
        #self.tab_1.layout.add
        self.picture = QLabel()
        layout = QGridLayout(self)
        # self.tab_1.layout.addWidget(self.picture)
        self.tab_1.addWidget(self.picture)
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()
        self.tab_4 = QWidget()

        # adding tabs to widgets
        self.all_tabs.addTab(self.tab_1, "1")
        self.all_tabs.addTab(self.tab_2, "2")
        self.all_tabs.addTab(self.tab_3, "3")
        self.all_tabs.addTab(self.tab_4, "4")

        # Dodanie widżetu do głównego okna jako centralny widżet
        self.setCentralWidget(self.all_tabs)
        self.setLayout(layout)


# Uruchomienie okna
# widget = QWidget()
# widget.show()

app = QApplication([])  # window initialization
win = Window()
win.show()
app.exec_()
