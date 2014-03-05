__author__ = 'physalis'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from math import *

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        self.lineedit.setFocus()

        self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUI)
        self.setWindowTitle("Calculate")

    def updateUI(self):
        try:
            text = self.lineedit.text()
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid</font>" % text)
        self.lineedit.selectAll()

app = QApplication(sys.argv)
form = Form()
form.show()

print "TestText"

app.exec_()
