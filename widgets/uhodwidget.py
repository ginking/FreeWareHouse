# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uhodwidget.ui'
#
# Created: Mon Jul 30 19:37:38 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_UhodWidget(object):
    def setupUi(self, UhodWidget):
        UhodWidget.setObjectName(_fromUtf8("UhodWidget"))
        UhodWidget.resize(942, 590)
        self.gridLayout = QtGui.QGridLayout(UhodWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.closeButton = QtGui.QPushButton(UhodWidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 5, 1, 1, 1)
        self.addButton = QtGui.QPushButton(UhodWidget)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.uhodTableWidget = QtGui.QTableWidget(UhodWidget)
        self.uhodTableWidget.setObjectName(_fromUtf8("uhodTableWidget"))
        self.uhodTableWidget.setColumnCount(6)
        self.uhodTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.uhodTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.uhodTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.uhodTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.uhodTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.uhodTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.uhodTableWidget.setHorizontalHeaderItem(5, item)
        self.uhodTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.uhodTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.uhodTableWidget, 0, 0, 6, 1)
        self.editButton = QtGui.QPushButton(UhodWidget)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.gridLayout.addWidget(self.editButton, 1, 1, 1, 1)
        self.deleteButton = QtGui.QPushButton(UhodWidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout.addWidget(self.deleteButton, 2, 1, 1, 1)

        self.retranslateUi(UhodWidget)
        QtCore.QMetaObject.connectSlotsByName(UhodWidget)

    def retranslateUi(self, UhodWidget):
        UhodWidget.setWindowTitle(QtGui.QApplication.translate("UhodWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("UhodWidget", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("UhodWidget", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uhodTableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("UhodWidget", "Номер", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uhodTableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("UhodWidget", "Дата", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uhodTableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("UhodWidget", "Поставщик", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uhodTableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("UhodWidget", "Полное название", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uhodTableWidget.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("UhodWidget", "Основание", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uhodTableWidget.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("UhodWidget", "Сумма", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("UhodWidget", "Изменить", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("UhodWidget", "Удалить", None, QtGui.QApplication.UnicodeUTF8))

