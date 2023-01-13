from PyQt5.QtGui import *
import sys


from PyQt5.QtWidgets import QWidget, QTreeView, QHBoxLayout, QApplication, QLabel, QLineEdit, QVBoxLayout, QCompleter, \
    QPushButton
from PyQt5.uic.properties import QtGui

from main import DictForQTreeView

class finder(QTextLine):
    def join(self):

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
class TreeView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        tree = DictForQTreeView.CreatingADictionaryBasedOnSkeletonSorting()
        self.tree = QTreeView(self)
        layout = QHBoxLayout(self)
        layout2 = QHBoxLayout(self)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Search:')
        self.line = QLineEdit(self)

        layout3 = QVBoxLayout(self)
        layout4 = QVBoxLayout(self)
        layout5 = QHBoxLayout(self)
        layout6 = QHBoxLayout(self)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Object:')
        self.line2 = QLineEdit(self)

        self.but = QPushButton(self)
        self.but.setText("Cancel")
        self.but2 = QPushButton(self)
        self.but2.setText("OK")

        layout6.addWidget(self.but)
        layout6.addWidget(self.but2)

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Model:')
        self.line3 = QLineEdit(self)

        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('Date:')
        self.line4 = QLineEdit(self)

        layout3.addWidget(self.nameLabel2)
        layout3.addWidget(self.line2)
        layout3.addWidget(self.nameLabel3)
        layout3.addWidget(self.line3)
        layout3.addWidget(self.nameLabel4)
        layout3.addWidget(self.line4)




        layout5.addWidget(self.nameLabel)
        layout5.addWidget(self.line)

        layout4.addLayout(layout5)
        layout4.addLayout(layout2)

        layout3.addLayout(layout6)



        self.line.resize(200, 32)
        #self.nameLabel.move(20, 20)
        self.line.returnPressed.connect(self.onChanged)
        completer = QCompleter(tree)
        self.line.setCompleter(completer)

        layout4.addWidget(self.tree)

        layout4.addLayout(layout4)
        layout.addLayout(layout4)
        layout.addLayout(layout3)


        layout.addLayout(layout)
        root_model = QStandardItemModel()
        self.tree.setModel(root_model)
        self._populateTree(tree, root_model.invisibleRootItem())

    def onChanged(self):
        # TODO press enter
        print("222")

    def _populateTree(self, children, parent):
        for child in sorted(children):
            child_item = QStandardItem(child)
            parent.appendRow(child_item)
            if isinstance(children, dict):
                self._populateTree(children[child], child_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TreeView()
    main.show()
    sys.exit(app.exec_())