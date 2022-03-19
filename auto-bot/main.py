from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtDesigner import QFormBuilder
from ui import UI

def window():
    app = QApplication(sys.argv)
    win = UI()
    win.show()
    sys.exit(app.exec_())

window()