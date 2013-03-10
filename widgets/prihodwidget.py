# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prihodwidget.ui'
#
# Created: Mon Jul 30 19:37:23 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PrihodWidget(object):
    def setupUi(self, PrihodWidget):
        PrihodWidget.setObjectName(_fromUtf8("PrihodWidget"))
        PrihodWidget.resize(942, 590)
        self.gridLayout = QtGui.QGridLayout(PrihodWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.closeButton = QtGui.QPushButton(PrihodWidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 5, 1, 1, 1)
        self.addButton = QtGui.QPushButton(PrihodWidget)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.prihodTableWidget = QtGui.QTableWidget(PrihodWidget)
        self.prihodTableWidget.setObjectName(_fromUtf8("prihodTableWidget"))
        self.prihodTableWidget.setColumnCount(6)
        self.prihodTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.prihodTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.prihodTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.prihodTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.prihodTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.prihodTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.prihodTableWidget.setHorizontalHeaderItem(5, item)
        self.prihodTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.prihodTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.prihodTableWidget, 0, 0, 6, 1)
        self.editButton = QtGui.QPushButton(PrihodWidget)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.gridLayout.addWidget(self.editButton, 1, 1, 1, 1)
        self.deleteButton = QtGui.QPushButton(PrihodWidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout.addWidget(self.deleteButton, 2, 1, 1, 1)

        self.retranslateUi(PrihodWidget)
        QtCore.QMetaObject.connectSlotsByName(PrihodWidget)

    def retranslateUi(self, PrihodWidget):
        PrihodWidget.setWindowTitle(QtGui.QApplication.translate("PrihodWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("PrihodWidget", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("PrihodWidget", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        item = self.prihodTableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("PrihodWidget", "Номер", None, QtGui.QApplication.UnicodeUTF8))
        item = self.prihodTableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("PrihodWidget", "Дата", None, QtGui.QApplication.UnicodeUTF8))
        item = self.prihodTableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("PrihodWidget", "Поставщик", None, QtGui.QApplication.UnicodeUTF8))
        item = self.prihodTableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("PrihodWidget", "Полное название", None, QtGui.QApplication.UnicodeUTF8))
        item = self.prihodTableWidget.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("PrihodWidget", "Основание", None, QtGui.QApplication.UnicodeUTF8))
        item = self.prihodTableWidget.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("PrihodWidget", "Сумма", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("PrihodWidget", "Изменить", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("PrihodWidget", "Удалить", None, QtGui.QApplication.UnicodeUTF8))

