#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from sys import platform

import os
import subprocess

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QKeySequence
from PyQt5.QtWidgets import QWidget, QApplication, QFileSystemModel, QTreeView, QLabel, QLineEdit, QGridLayout,\
    QVBoxLayout, QPushButton, QCompleter, QTreeWidgetItem, QAction, QMessageBox, QDialog, QHBoxLayout




class ModalWindow(QDialog):
    """
    Окно для осуществление изменения пути в программе.
    """
    def __init__ (self):
        super().__init__()

        self.setWindowTitle('Изменения пути')
        self.layout = QVBoxLayout()

        message = QLabel('''<h1 style=text-align:center>Введите путь до нужной папки!</h1>
        <p></p>
        <h3 style=text-align:center>(При закрытии ПО, он вернётся в значение по умолчанию)</h3>
        <p></p>
        <h5>После нажатия на кнопку "Изменить" вы должны нажать на кнопку "Открыть", чтоб виджет обновился</h5> ''')
        self.layout.addWidget(message)

        close_button = QPushButton('Заменить')
        self.line_edit = QLineEdit()
        close_button.clicked.connect(self.button_close)

        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(close_button)
        replace_pather = self.line_edit.text()

        self.line_edit.setText("")
        self.setLayout(self.layout)

    """
    Действие при нажатии на кнопку (сохранения информации в массив)
    """
    def button_close (self):
        replace_pather.append(self.line_edit.text())
        self.accept()


class MyWindow(QWidget):
    """
    Запуск программы + проверка пути
        """
    def __init__ (self, parent = None):
        super(MyWindow, self).__init__(parent)

        if platform == "linux" or platform == "linux2":
            self.dir = "/home/drawmang/disk-z/DigitRock Models Backup/"
        elif platform == "win32":
            self.dir = "Z:/DigitRock Models Backup/"

        self.dir = MyWindow.check_path(self.dir)
        self.pathRoot = self.dir
        self.interface()

    """
    Проверка пути, заменя палок и добавление туда где не хватает
        """
    def check_path (dir):

        if dir [-1] != "/":
            if dir [-1] == '\\':
                dir = str(dir).replace("\\", "/")
            else:
                dir = dir + "/"
                if dir.find("\\") != -1:
                    dir = str(dir).replace("\\", "/")
        return dir

    """
    Чисто интерфейсная функция
        """
    def interface (self):

        self.model = QFileSystemModel(self)

        self.model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)

        self.model.setRootPath(self.pathRoot)

        self.indexRoot = self.model.index(self.model.rootPath())

        self.treeView = QTreeView(self)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        self.treeView.clicked.connect(self.on_treeView_clicked)

        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.setSortingEnabled(True)
        self.treeView.setHeaderHidden(True)

        action = QAction(self)
        action.setShortcut(QKeySequence('Ctrl+Q'))
        action.triggered.connect(self.handleHotkey)

        self.addAction(action)

        self.label_object = QLabel(self)
        self.label_object.setText('Объект:')
        self.line2 = QLineEdit(self)
        self.line2.setReadOnly(True)

        self.label_model = QLabel(self)
        self.label_model.setText('Модель:')
        self.line3 = QLineEdit(self)
        self.line3.setReadOnly(True)

        self.label_date = QLabel(self)
        self.label_date.setText('Дата:')
        self.line4 = QLineEdit(self)
        self.line4.setReadOnly(True)

        self.Btn_Open = QPushButton(self)
        self.Btn_Open.setText("Открыть")
        self.Btn_Open.clicked.connect(self.open_btn)

        self.label_search = QLabel(self)
        self.label_search.setText('Поиск:')

        self.txt_search = QLineEdit(self)
        self.txt_search.textChanged [str].connect(self.onChanged2)
        self.txt_search.returnPressed.connect(self.onChanged)

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.label_search, 2, 0)
        self.gridLayout.addWidget(self.txt_search, 2, 1)

        self.gridLayout2 = QGridLayout()
        self.gridLayout2.addWidget(self.treeView, 0, 0)

        self.gridLayout3 = QGridLayout()

        self.horizont_grid3 = QHBoxLayout()

        self.vertical_grid3 = QVBoxLayout()
        self.vertical_grid3.addWidget(self.label_object)

        self.vertical_grid3_2 = QVBoxLayout()
        self.vertical_grid3_2.addWidget(self.line2)
        self.vertical_grid3_2.addWidget(self.line3)
        self.vertical_grid3_2.addWidget(self.line4)

        self.vertical_grid3.addWidget(self.label_model)
        self.vertical_grid3.addWidget(self.label_date)

        self.horizont_grid3.addLayout(self.vertical_grid3)
        self.horizont_grid3.addLayout(self.vertical_grid3_2)

        self.gridLayout3.addLayout(self.horizont_grid3, 0, 0)
        self.gridLayout3.addWidget(self.Btn_Open, 4, 0)

        self.gridLayout2.addLayout(self.gridLayout3, 0, 1)
        try:
            self.root_folder = [f.path for f in os.scandir(self.dir) if f.is_dir()]
        except:
            print("Ошибка пути, введите другой в коде или же через CTRL+Q")
            if platform == "linux" or platform == "linux2":
                self.dir = "/home/"
                self.dir = MyWindow.check_path(self.dir)
                self.pathRoot = self.dir
                self.model.setRootPath(self.dir)
                self.indexRoot = self.model.index(self.model.rootPath())
                self.treeView.setModel(self.model)
                self.treeView.setRootIndex(self.indexRoot)

            elif platform == "win32":
                self.dir = "С:/"
                self.dir = MyWindow.check_path(self.dir)
                self.pathRoot = self.dir
                self.model.setRootPath(self.dir)
                self.indexRoot = self.model.index(self.model.rootPath())
                self.treeView.setModel(self.model)
                self.treeView.setRootIndex(self.indexRoot)

        self.layout_left = QVBoxLayout(self)
        self.layout_left.addLayout(self.gridLayout)
        self.layout_left.addLayout(self.gridLayout2)

        self.comp = []

    """
    Работа ХотКея Ктрл+Й
        """
    def handleHotkey (self):
        modal_window = ModalWindow()
        modal_window.exec_()


    def _accept_index (self, idx):
        if idx.isValid():
            text = idx.data(QtCore.Qt.DisplayRole)
            if self.filterRegExp().indexIn(text) >= 0:
                return True
            for row in range(idx.model().rowCount(idx)):
                if self._accept_index(idx.model().index(row, 0, idx)):
                    return True

        return False

    def filterAcceptsRow (self, sourceRow, sourceParent):
        idx = self.sourceModel().index(sourceRow, 0, sourceParent)
        return self._accept_index(idx)

    """
    Нажатие на кнопку Открыть
        """
    def onChanged2 (self, text):

        if self.txt_search.text() == "":
            self.model.setRootPath(self.dir)
            self.indexRoot = self.model.index(self.model.rootPath())
            self.treeView.setModel(self.model)
            self.treeView.setRootIndex(self.indexRoot)

        finders = []

        for i in range(len(self.root_folder)):
            self.root_folder [i] = str(self.root_folder [i]).split("/") [-1]
            if self.txt_search.text() in self.root_folder [i] and self.txt_search.text() != "":
                finders.append(self.root_folder [i])

        completer = QCompleter(finders)

        if text in finders:
            pass
        else:
            if not self.comp:
                completer.setFilterMode(Qt.MatchContains)
                self.txt_search.setCompleter(completer)
                self.comp.append(completer)
            if self.comp [-1] == completer:
                pass
            else:

                completer.setFilterMode(Qt.MatchContains)
                self.txt_search.setCompleter(completer)
                self.comp.append(completer)
        if len(finders) == 1:
            self.pathRoot = self.dir + finders [0]
            self.model.setRootPath(self.pathRoot)

            self.indexRoot = self.model.index(self.model.rootPath())
            self.treeView.setRootIndex(self.indexRoot)

    """
    Вроде как тут находится только ввод текста в поисковую строку
        """
    def onChanged (self):
        finders = []
        filter = []
        id = []
        for i in range(len(self.root_folder)):
            self.root_folder [i] = str(self.root_folder [i]).split("/") [-1]
            if self.txt_search.text() in self.root_folder [i] and self.txt_search.text() != "":
                finders.append(self.root_folder [i])
                id.append(i)
                filter.append("*." + self.root_folder [i])
                self.pathRoot = self.dir + finders [0]

                if self.txt_search.text() != finders [0]:
                    self.txt_search.setText(str(finders [0]))

        self.model = QFileSystemModel(self)

        self.model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)

        self.model.setRootPath(self.dir)
        if self.txt_search.text() == "":
            self.model.setRootPath(self.dir)
        else:
            self.model.setRootPath(self.pathRoot)

        self.indexRoot = self.model.index(self.model.rootPath())

        self.treeView.setModel(self.model)

        self.treeView.setRootIndex(self.indexRoot)

    """
    Функция при открытии кнопки
        """
    def open_btn (self):
        try:
            if len(replace_pather) != 0:
                if replace_pather [-1] != "":
                    self.model.setRootPath(replace_pather [-1])
                    self.dir = replace_pather [-1]
                    self.dir = MyWindow.check_path(self.dir)
                    self.pathRoot = replace_pather [-1]
                    self.treeView.setModel(self.model)
                    MyWindow.onChanged2(self, "")
        except Exception as e:
            print("[secret event] error: ", e)
        if self.line4.text() != "":
            path = self.dir + self.lvl1 + "/" + self.lvl2 + "/" + self.lvl3
            if platform == "Windows":
                os.startfile(path)
            elif platform == "Darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])

    """
    Функция при клике на древо путей
        """
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked (self, index):
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")
        indexItem = self.model.index(index.row(), 0, index.parent())
        self.informer(self.dir, self.model.filePath(indexItem))

    """
    Функция для передачи данных в пункты ДАТА/МОДУЛИ/ОБЪЕКТЫ
        """
    def informer (self, dir_root, path_index):

        self.index_path = path_index.replace(dir_root, "")
        if self.index_path.count(r'/') >= 2:
            self.lvl1, self.lvl2, self.lvl3 = self.index_path.split("/") [0], self.index_path.split("/") [1],\
                self.index_path.split("/") [2]
            self.line2.setText(self.lvl1)
            self.line3.setText(self.lvl2)
            self.line4.setText(self.lvl3)


if __name__ == "__main__":

    replace_pather = []
    app = QApplication(sys.argv)
    app.setApplicationName('База резервного копирования')

    main = MyWindow()
    main.resize(666, 333)
    main.move(app.desktop().screen().rect().center() - main.rect().center())
    main.show()

    sys.exit(app.exec_())
