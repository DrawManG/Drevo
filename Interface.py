import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QTreeView, QHBoxLayout, QApplication, QLabel, QLineEdit, QVBoxLayout, QCompleter, \
    QPushButton

from main import DictForQTreeView

"""
line2 - txt_object
line3 - txt_model
line4 - txt_date
"""
class TreeView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.tree = DictForQTreeView.CreatingADictionaryBasedOnSkeletonSorting()
        backup_treeview_data = self.tree
        self.treeView = QTreeView(self)
        self.treeView.clicked.connect(self.Item_click)
        layout_main = QHBoxLayout(self)


        self.label_search = QLabel(self)
        self.label_search.setText('Search:')
        self.txtbox_search = QLineEdit(self)

        layout_main_right = QVBoxLayout(self)
        layout_main_left = QVBoxLayout(self)
        layout_main_left_search = QVBoxLayout(self)
        layout_main_right_buttons = QHBoxLayout(self)

        self.label_object = QLabel(self)
        self.label_object.setText('Object:')
        self.line2 = QLineEdit(self)

        self.Btn_cancel = QPushButton(self)
        self.Btn_cancel.setText("Cancel")
        self.btn_OK = QPushButton(self)
        self.btn_OK.setText("OK")

        layout_main_right_buttons.addWidget(self.Btn_cancel)
        layout_main_right_buttons.addWidget(self.btn_OK)

        self.label_model = QLabel(self)
        self.label_model.setText('Model:')
        self.line3 = QLineEdit(self)

        self.label_date = QLabel(self)
        self.label_date.setText('Date:')
        self.line4 = QLineEdit(self)

        layout_main_right.addWidget(self.label_object)
        layout_main_right.addWidget(self.line2)
        layout_main_right.addWidget(self.label_model)
        layout_main_right.addWidget(self.line3)
        layout_main_right.addWidget(self.label_date)
        layout_main_right.addWidget(self.line4)




        layout_main_left_search.addWidget(self.label_search)
        layout_main_left_search.addWidget(self.txtbox_search)

        layout_main_left.addLayout(layout_main_left_search)


        layout_main_right.addLayout(layout_main_right_buttons)



        self.txtbox_search.resize(200, 32)
        #self.nameLabel.move(20, 20)

        self.txtbox_search.textChanged.connect(self.onChanged)
        completer = QCompleter(backup_treeview_data)
        self.txtbox_search.setCompleter(completer)

        layout_main_left.addWidget(self.treeView)

        layout_main_left.addLayout(layout_main_left)
        layout_main.addLayout(layout_main_left)
        layout_main.addLayout(layout_main_right)


        layout_main.addLayout(layout_main)
        root_model = QStandardItemModel()
        self.treeView.setModel(root_model)
        self._populateTree(self.tree, root_model.invisibleRootItem())

    def onChanged(self):
        # TODO press enter
        _backup = self.tree
        find = self.txtbox_search.text()
        self.tree = {key: val for key, val in _backup.items() if find in key}
        root_model = QStandardItemModel()
        self.treeView.setModel(root_model)
        self._populateTree(self.tree, root_model.invisibleRootItem())
        self.tree = _backup


    def Item_click(self,*args):
        for index in self.treeView.selectedIndexes():
            data = "/" + index.data()
            while index.parent().isValid():
                index = index.parent()
                data = "/" + index.data() + data
            data=data.split("/")
            del data[0]
            self.line2.setText("")
            self.line3.setText("")
            self.line4.setText("")
            if len(data) <= 3:

                for i in range(len(data)):

                    code = """self.line{NUMB}.setText(data[{INDEX}])"""
                    code = code.replace("{NUMB}",str(i+2))
                    code = code.replace("{INDEX}",str(i))

                    exec(code)


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