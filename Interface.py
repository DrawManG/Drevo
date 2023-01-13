from PyQt5.QtGui import *
import sys


from PyQt5.QtWidgets import QWidget, QTreeView, QHBoxLayout, QApplication
from main import DictForQTreeView

class MainFrame(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        tree = DictForQTreeView.CreatingADictionaryBasedOnSkeletonSorting()
        self.tree = QTreeView(self)
        layout = QHBoxLayout(self)
        layout.addWidget(self.tree)
        root_model = QStandardItemModel()
        self.tree.setModel(root_model)
        self._populateTree(tree, root_model.invisibleRootItem())

    def _populateTree(self, children, parent):
        for child in sorted(children):
            child_item = QStandardItem(child)
            parent.appendRow(child_item)
            if isinstance(children, dict):
                self._populateTree(children[child], child_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainFrame()
    main.show()
    sys.exit(app.exec_())