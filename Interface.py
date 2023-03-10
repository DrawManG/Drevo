import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QTreeView, QHBoxLayout, QApplication, QLabel, QLineEdit, QVBoxLayout, QCompleter, \
    QPushButton, QGridLayout, QFileSystemModel
import os
import platform
import subprocess

from PyQt5.uic.properties import QtCore

from main import DictForQTreeView,type_2
from PyQt5 import QtCore, QtGui

from PyQt5.QtWidgets import QWidget, QApplication, QFileSystemModel, QTreeView, QLabel, QLineEdit, QGridLayout, \
    QVBoxLayout

"""
line2 - txt_object
line3 - txt_model
line4 - txt_date
"""
class TreeView(QWidget):



    def __init__(self):
        QWidget.__init__(self)
        layout_main = QHBoxLayout(self)
        layout_main_right = QVBoxLayout(self)
        layout_main_left = QVBoxLayout(self)
        layout_main_left_search = QVBoxLayout(self)
        layout_main_right_buttons = QHBoxLayout(self)
        self.root_path = DictForQTreeView.pather()
        self.pathRoot = r'C:\Users\DHOUSE\Desktop\New folder'

        self.model = QFileSystemModel(self)

        self.model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)
        self.model.setRootPath(self.pathRoot)

        self.indexRoot = self.model.index(self.model.rootPath())

        self.treeView = QTreeView(self)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)


        self.labelFileName = QLabel(self)
        self.labelFileName.setText("File Name:")

        self.lineEditFileName = QLineEdit(self)

        self.labelFilePath = QLabel(self)
        self.labelFilePath.setText("File Path:")

        self.lineEditFilePath = QLineEdit(self)

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.labelFileName, 0, 0)
        self.gridLayout.addWidget(self.lineEditFileName, 0, 1)
        self.gridLayout.addWidget(self.labelFilePath, 1, 0)
        self.gridLayout.addWidget(self.lineEditFilePath, 1, 1)

        self.layout = QVBoxLayout(self)
        self.layout.addLayout(self.gridLayout)
        self.layout.addWidget(self.treeView)





        self.label_search = QLabel(self)
        self.label_search.setText('Search:')
        self.txtbox_search = QLineEdit(self)
        self.txtbox_search.textChanged.connect(self.onChanged)


        self.label_object = QLabel(self)
        self.label_object.setText('Object:')
        self.line2 = QLineEdit(self)
        self.line2.setReadOnly(True)

        self.Btn_Open = QPushButton(self)
        self.Btn_Open.setText("Open")
        self.Btn_Open.clicked.connect(self.open_btn)
        #self.btn_OK = QPushButton(self)
        #self.btn_OK.setText("OK")

        layout_main_right_buttons.addWidget(self.Btn_Open)
        #layout_main_right_buttons.addWidget(self.btn_OK)

        self.label_model = QLabel(self)
        self.label_model.setText('Model:')
        self.line3 = QLineEdit(self)
        self.line3.setReadOnly(True)

        self.label_date = QLabel(self)
        self.label_date.setText('Date:')
        self.line4 = QLineEdit(self)
        self.line4.setReadOnly(True)

        layout_main.addLayout(layout_main_left)
        layout_main.addLayout(layout_main_right)
        layout_main.addLayout(layout_main)

        layout_main_right.addWidget(self.label_object)
        layout_main_right.addWidget(self.line2)
        layout_main_right.addWidget(self.label_model)
        layout_main_right.addWidget(self.line3)
        layout_main_right.addWidget(self.label_date)
        layout_main_right.addWidget(self.line4)
        layout_main_right.addLayout(layout_main_right_buttons)

        layout_main_left_search.addWidget(self.label_search)
        layout_main_left_search.addWidget(self.txtbox_search)
        layout_main_left.addLayout(layout_main_left_search)
        layout_main_left.addWidget(self.treeView)
        layout_main_left.addLayout(layout_main_left)

        self.root_model = QStandardItemModel()
        self.treeView.setModel(self.root_model)


    def open_btn(self):


        if len(self.line2.text()) > 0 and len(self.line3.text()) > 0 and len(self.line4.text()) > 0 :
            self.root_path = DictForQTreeView.pather()
            path = str(self.root_path+self.line2.text()+"/"+self.line3.text()+"/"+self.line4.text())

            if platform.system() == "Windows":
                if self.line2.text() and self.line3.text() and self.line4.text():
                    path = os.path.join(DictForQTreeView.pather(), self.line2.text(), self.line3.text(),
                                        self.line4.text())
                    os.startfile(path)
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])


    def onChanged(self):

        _backup = self.tree
        self.root_model = QStandardItemModel()
        self.tree = {key: val for key, val in _backup.items() if self.txtbox_search.text() in key}
        self.treeView.setModel(self.root_model)
        self._populateTree(self.tree, self.root_model.invisibleRootItem())

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




if __name__ == "__main__":


    app = QApplication(sys.argv)
    main = TreeView()
    main.resize(750,300)
    main.show()
    sys.exit(app.exec_())