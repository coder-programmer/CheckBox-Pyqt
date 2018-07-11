import sys
import os
from PyQt5.QtWidgets import (QCheckBox, QWidget, QApplication, QGridLayout)
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("checkbox")
        path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'img.png')
        self.setWindowIcon(QIcon(path))
        
        layout = QGridLayout()
        self.setLayout(layout)

        self.checkbox = QCheckBox("Kestrel")
        self.checkbox.setChecked(True)
        self.checkbox.toggled.connect(self.checkbox_click)
        layout.addWidget(self.checkbox, 0, 0)


        self.checkbox1 = QCheckBox("Sparrowhawk")
        self.checkbox1.setChecked(True)
        self.checkbox1.toggled.connect(self.checkbox_click)
        layout.addWidget(self.checkbox1, 1, 0)


        self.checkbox2 = QCheckBox("Hobby")
        self.checkbox2.setChecked(True)
        self.checkbox2.toggled.connect(self.checkbox_click)
        layout.addWidget(self.checkbox2, 2, 0)
    
    def checkbox_click(self):
        selected = []

        if self.checkbox.isChecked():
            selected.append("Kestrel")

        if self.checkbox1.isChecked():
            selected.append("Sparrowhawk")

        if self.checkbox2.isChecked():
            selected.append("Hobby")

        print("Selected : %s" % (" ".join(selected)))
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
    
