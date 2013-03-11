#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2012 Sergey <sergey@Pent4-desktop>


import sqlite3
from PyQt4 import QtCore, QtGui
from widgets.main_window import Ui_MainWindow, _fromUtf8
from widgets.addGoods import Ui_addGoods
from widgets.whsstate import Ui_WhsStateForm
from widgets.prihodwidget import Ui_PrihodWidget
from widgets.addPrihod import Ui_addPrihodForm
from widgets.chooseGoods import Ui_ChooseGoodsForm
#from mainclass import Main
#from widgets.uhodwidget import Ui_UhodWidget
import os.path


NDS = 18
db_filename = ''
config_file = 'main.conf'
try:
    f = open (config_file, 'r')
    for line in f.readlines():
        if 'last_db' in line:
            db_filename = line.split('=')[1].strip()
    if os.path.exists(db_filename):
        pass
    else: db_filename = ''
    f.close()
except IOError:
    pass



# Класс основного окна >>

class Main(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.hide()
        self.ui.tabWidget.setTabsClosable(True)
        self.setWindowIcon(QtGui.QIcon('images/shop-icon.png'))
        QtCore.QObject.connect(self.ui.action_open_goods, QtCore.SIGNAL(_fromUtf8("activated()")), self.checked_goodsTabShow)
        QtCore.QObject.connect(self.ui.action_change_db, QtCore.SIGNAL(_fromUtf8("activated()")), self.open_db)
        QtCore.QObject.connect(self.ui.action_create_db, QtCore.SIGNAL(_fromUtf8("activated()")), self.new_db)
        QtCore.QObject.connect(self.ui.action_open_whsstate, QtCore.SIGNAL(_fromUtf8("activated()")), self.whsStateTabShow)
        QtCore.QObject.connect(self.ui.action_12, QtCore.SIGNAL(_fromUtf8("activated()")), self.prihodTabShow)
        QtCore.QObject.connect(self.ui.action_13, QtCore.SIGNAL(_fromUtf8("activated()")), self.uhodTabShow)
        self.ui.tabWidget.tabCloseRequested.connect(self.ui.tabWidget.removeTab)

        # Устанавливаем размер шрифта >>
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ui.centralwidget.setFont(font)
        # << Устанавливаем размер шрифта

        self.ui.tabWidget.show()


    def uhodTabShow(self):
        self.ui.uhod_tab = UhodTab(self)
        self.ui.tabWidget.addTab(self.ui.uhod_tab, _fromUtf8(""))
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.uhod_tab), QtGui.QApplication.translate("MainWindow", "Уходы", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.tabWidget.setCurrentWidget(self.ui.uhod_tab)
        QtCore.QObject.connect(self.ui.uhod_tab.uhodWidget.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeCurrentTab)



    def prihodTabShow(self):
        self.ui.prihod_tab = PrihodTab(self)
        self.ui.tabWidget.addTab(self.ui.prihod_tab, _fromUtf8(""))
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.prihod_tab), QtGui.QApplication.translate("MainWindow", "Приходы", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.tabWidget.setCurrentWidget(self.ui.prihod_tab)
        QtCore.QObject.connect(self.ui.prihod_tab.prihodWidget.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeCurrentTab)


    def whsStateTabShow(self):
        self.ui.whsState_tab = WhsStateTab(self)
        self.ui.tabWidget.addTab(self.ui.whsState_tab, _fromUtf8(""))
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.whsState_tab), QtGui.QApplication.translate("MainWindow", "Состояние склада", None, QtGui.QApplication.UnicodeUTF8))

        self.ui.tabWidget.setCurrentWidget(self.ui.whsState_tab)

        QtCore.QObject.connect(self.ui.whsState_tab.whsStateWidget.CloseWhsStateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeCurrentTab)


    def checked_goodsTabShow(self):
        if not hasattr(self.ui, 'goods_tab'):
            self.goodsTabShow()
        elif self.ui.tabWidget.indexOf(self.ui.goods_tab) < 0:
            self.goodsTabShow()
        else:
            self.ui.tabWidget.setCurrentWidget(self.ui.goods_tab)


    def goodsTabShow(self):
        #goods_widget = QtGui.QWidget()
        #self.ui.tabWidget.addTab(goods_widget, _fromUtf8("Справочник товаров"))

        # Вкладка "Справочник товаров" >>
        self.ui.goods_tab = QtGui.QWidget()
        self.ui.goods_tab.setObjectName(_fromUtf8("goods_tab"))
        self.ui.tabWidget.addTab(self.ui.goods_tab, _fromUtf8(""))
        self.ui.goodsgridLayout = QtGui.QGridLayout(self.ui.goods_tab)
        self.ui.goodsgridLayout.setObjectName(_fromUtf8("goodsgridLayout"))
        # << Вкладка "Справочник товаров"
        # Кнопки >>
        self.ui.addGroupButton = QtGui.QPushButton(self.ui.goods_tab)
        self.ui.addGroupButton.setObjectName(_fromUtf8("addGroupButton"))
        self.ui.goodsgridLayout.addWidget(self.ui.addGroupButton, 7, 0, 1, 1)
        self.ui.deleteGroupButton = QtGui.QPushButton(self.ui.goods_tab)
        self.ui.deleteGroupButton.setObjectName(_fromUtf8("deleteGroupButton"))
        self.ui.goodsgridLayout.addWidget(self.ui.deleteGroupButton, 7, 1, 1, 1)
        self.ui.copyUnitButton = QtGui.QPushButton(self.ui.goods_tab)
        self.ui.copyUnitButton.setObjectName(_fromUtf8("copyUnitButton"))
        self.ui.goodsgridLayout.addWidget(self.ui.copyUnitButton, 1, 5, 1, 1)
        self.ui.CloseGoodsButton = QtGui.QPushButton(self.ui.goods_tab)
        self.ui.CloseGoodsButton.setObjectName(_fromUtf8("CloseGoodsButton"))
        self.ui.goodsgridLayout.addWidget(self.ui.CloseGoodsButton, 7, 5, 1, 1)
        self.ui.addUnitButton = QtGui.QPushButton(self.ui.goods_tab)
        self.ui.addUnitButton.setObjectName(_fromUtf8("addUnitButton"))
        self.ui.goodsgridLayout.addWidget(self.ui.addUnitButton, 0, 5, 1, 1)
        self.ui.editUnitButton = QtGui.QPushButton(self.ui.goods_tab)
        self.ui.editUnitButton.setObjectName(_fromUtf8("editUnitButton"))
        self.ui.goodsgridLayout.addWidget(self.ui.editUnitButton, 2, 5, 1, 1)
        self.ui.deleteUnitButton = QtGui.QPushButton(self.ui.goods_tab)
        self.ui.deleteUnitButton.setObjectName(_fromUtf8("deleteUnitButton"))
        self.ui.goodsgridLayout.addWidget(self.ui.deleteUnitButton, 3, 5, 1, 1)

        self.ui.filter_label = QtGui.QLabel(self.ui.goods_tab)
        self.ui.filter_label.setObjectName(_fromUtf8("filter_label"))
        self.ui.goodsgridLayout.addWidget(self.ui.filter_label, 7, 2, 1, 1)
        self.ui.filter_lineEdit = QtGui.QLineEdit(self.ui.goods_tab)
        self.ui.filter_lineEdit.setObjectName(_fromUtf8("filter_lineEdit"))
        self.ui.goodsgridLayout.addWidget(self.ui.filter_lineEdit, 7, 3, 1, 1)
        self.ui.ClearFilterButton = QtGui.QPushButton(self.ui.goods_tab)
        self.ui.ClearFilterButton.setObjectName(_fromUtf8("ClearFilterButton"))
        self.ui.goodsgridLayout.addWidget(self.ui.ClearFilterButton, 7, 4, 1, 1)

        # << Кнопки
        # Дерево групп >>
        self.ui.treeWidget = QtGui.QTreeWidget(self.ui.goods_tab)
        self.ui.treeWidget.setObjectName(_fromUtf8("treeView"))
        self.ui.goodsgridLayout.addWidget(self.ui.treeWidget, 0, 0, 7, 2)
        item_0 = QtGui.QTreeWidgetItem(self.ui.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.ui.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.ui.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.ui.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        self.ui.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Группы", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.ui.treeWidget.isSortingEnabled()
        self.ui.treeWidget.setSortingEnabled(False)
        self.ui.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "Все группы", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "Водонагреватели", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Проточные водонагреватели", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Накопительные водонагреватели", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(2).setText(0, QtGui.QApplication.translate("MainWindow", "Теплотехника", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(2).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Электрические конвекторы", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(2).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Маслонаполненные обогреватели", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(3).setText(0, QtGui.QApplication.translate("MainWindow", "Водоснабжение", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(3).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Погружные насосы", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(3).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Центробежные погружные насосы", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.topLevelItem(3).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Вибрационные погружные насосы", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.treeWidget.setSortingEnabled(__sortingEnabled)
        self.ui.treeWidget.setCurrentItem(self.ui.treeWidget.topLevelItem(0))# Устанавливаем активный элемент
        # << Дерево групп
        # Таблица товаров >>
        self.ui.tableWidget = QtGui.QTableWidget(self.ui.goods_tab)
        self.ui.tableWidget.setObjectName(_fromUtf8("tableView"))
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # Отключаем редактирование
        item = QtGui.QTableWidgetItem()
        self.ui.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ui.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.ui.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.ui.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.ui.tableWidget.setHorizontalHeaderItem(4, item)
        self.ui.goodsgridLayout.addWidget(self.ui.tableWidget, 0, 2, 7, 3)

        item = self.ui.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Артикул", None, QtGui.QApplication.UnicodeUTF8))
        item = self.ui.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Название", None, QtGui.QApplication.UnicodeUTF8))
        item = self.ui.tableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Цена", None, QtGui.QApplication.UnicodeUTF8))
        item = self.ui.tableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Бренд", None, QtGui.QApplication.UnicodeUTF8))
        item = self.ui.tableWidget.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Страна производства", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.tableWidget.setSortingEnabled(True)


        # << Таблица товаров

        #self.ui.tabWidget.addTab(self.ui.goods_tab, _fromUtf8(""))

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True) # Растягиваем по-ширине
        self.ui.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.ui.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows) # Выбор построчно

        #self.ui.tabWidget.tabCloseRequested.connect(self.ui.tabWidget.removeTab)
        QtCore.QObject.connect(self.ui.CloseGoodsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeCurrentTab)
        QtCore.QObject.connect(self.ui.addUnitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showaddUnitWindow)
        QtCore.QObject.connect(self.ui.ClearFilterButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ui.filter_lineEdit.clear)
        QtCore.QObject.connect(self.ui.deleteUnitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.deleteUnitDialog)
        QtCore.QObject.connect(self.ui.copyUnitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.copyUnit)
        QtCore.QObject.connect(self.ui.editUnitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.editUnit)



        self.ui.addGroupButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Добавить группу", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.addGroupButton.setText(QtGui.QApplication.translate("MainWindow", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.deleteGroupButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Удалить группу", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.deleteGroupButton.setText(QtGui.QApplication.translate("MainWindow", "Удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.copyUnitButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Копировать позицию", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.copyUnitButton.setText(QtGui.QApplication.translate("MainWindow", "Копировать", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.CloseGoodsButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Закрыть вкладку", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.CloseGoodsButton.setText(QtGui.QApplication.translate("MainWindow", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.addUnitButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Добавить позицию", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.addUnitButton.setText(QtGui.QApplication.translate("MainWindow", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.editUnitButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Изменить позицию", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.editUnitButton.setText(QtGui.QApplication.translate("MainWindow", "Изменить", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.deleteUnitButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Удалить позицию", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.deleteUnitButton.setText(QtGui.QApplication.translate("MainWindow", "Удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.goods_tab), QtGui.QApplication.translate("MainWindow", "Справочник товаров", None, QtGui.QApplication.UnicodeUTF8))
        #self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.filter_label.setText(QtGui.QApplication.translate("MainWindow", "Фильтр", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.ClearFilterButton.setText(QtGui.QApplication.translate("MainWindow", "Очистить", None, QtGui.QApplication.UnicodeUTF8))

        self.ui.tabWidget.setCurrentWidget(self.ui.goods_tab)


        # Загрузка данных из базы в таблицу>>

        __sortingEnabled = self.ui.tableWidget.isSortingEnabled()
        self.ui.tableWidget.setSortingEnabled(False)
        if db_filename:
            self.load_data('goodscatalog')
        else:
            err = QtGui.QMessageBox(self)
            err.setText('База данных не выбрана !')
            err.setIcon(2)
            err.show()
            self.ui.tabWidget.clear()

        self.ui.tableWidget.setSortingEnabled(__sortingEnabled)

        # << Загрузка данных из базы в таблицу


    def removeCurrentTab(self):
        self.ui.tabWidget.removeTab(self.ui.tabWidget.currentIndex())



    def showaddUnitWindow(self):
        addUnitWindow = addUnitDialog(self)
        addUnitWindow.show()

    def copyUnit(self):
        copyUnitWindow = copyUnitDialog(self)
        copyUnitWindow.setWindowTitle('Копирование позиции')
        copyUnitWindow.show()


    def editUnit(self):
        editUnitWindow = editUnitDialog(self)
        editUnitWindow.setWindowTitle('Редактирование позиции')
        editUnitWindow.show()



    def deleteUnitDialog(self):
        units = self.ui.tableWidget.selectedItems()

        # Второй вариант :
        #rows = set()
        #for item in units:
        #    rows.add(self.ui.tableWidget.row(item))

        reply = QtGui.QMessageBox.question(self, 'Подтвердите удаление',
            "Удалить выбранные элементы?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            __sortingEnabled = self.ui.tableWidget.isSortingEnabled()
            self.ui.tableWidget.setSortingEnabled(False)

            for item in units[::self.ui.tableWidget.columnCount()]:
                name = self.ui.tableWidget.item(self.ui.tableWidget.row(item), 1).text()
                conn = sqlite3.connect(db_filename)
                cur = conn.cursor()
                cur.execute('delete from goodscatalog where name=?', (name,))
                conn.commit()

                self.ui.tableWidget.removeRow(self.ui.tableWidget.row(item)) # Удаляем из таблицы

            self.ui.tableWidget.setSortingEnabled(__sortingEnabled)
        else:
            pass

    def open_db(self):
        global db_filename
        db_filename1 = QtGui.QFileDialog.getOpenFileName(self, 'Открыть файл базы данных', '/home')
        if db_filename1:
            db_filename = db_filename1
            f = open(config_file, 'w')
            f.write('last_db = ' + db_filename1 + '\n')
            f.close()

    def new_db(self):
        global db_filename
        db_filename1 = QtGui.QFileDialog.getSaveFileName(self, 'Сздать базу данных', '/home')
        if db_filename1 :
            db_filename = db_filename1
            conn=sqlite3.connect(str(db_filename))
            cur=conn.cursor()
            # Создание таблицы справочника товаров
            cur.execute('create table if not exists goodscatalog(article integer, name text, price real, brand text, country text, barcode0 integer, barcode1 integer, minimal integer, gruppa text, measure text, nds integer)')
            # Создание таблицы "Состояния склада"
            cur.execute('create table if not exists whsstate(article integer, name text, price real, instock integer, reserved integer, measure text, inpackage integer, packagesinstock integer)')
            # Создание таблицы "Приходы" на склад
            cur.execute('create table if not exists prihod(number integer, date integer, supplier text, fullname text, cause text, sum real)')
            # Создание таблицы "Уходы" со склада
            cur.execute('create table if not exists uhod(number integer, date integer, supplier text, fullname text, cause text, sum real)')
            # Создание таблицы "Контрагенты"
            #cur.execute('create table if not exists contragents(name text, fullname text, legaladdress text, factaddress text, .....)')
            conn.commit()
            f = open(config_file, 'w')
            f.write('last_db = ' + db_filename + '\n')
            f.close()
        #else:
        #    print ('Пусто !')

    def load_data(self, DbTable):# Переписать, как в chooseGoods (работа по столбцам)
        conn=sqlite3.connect(str(db_filename))
        cur=conn.cursor()
        query = ('select * from %s' % DbTable)
        cur.execute(query)
        rows = cur.fetchall()
        self.ui.tableWidget.setRowCount(len(rows))
        line = 0
        for row in rows:
            for i in range(self.ui.tableWidget.columnCount()):
                item = QtGui.QTableWidgetItem()
                self.ui.tableWidget.setItem(line, i, item)
                #item = self.ui.tableWidget.item(line, i)
                item.setText(str(row[i]))
                i += 1
            line += 1
        conn.commit()



# << Класс основного окна

#----------------------------------------------------------------------


# Класс вкладки "Приходы" >>

class PrihodTab(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.prihodWidget =  Ui_PrihodWidget()
        self.prihodWidget.setupUi(self)
        QtCore.QObject.connect(self.prihodWidget.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showAddPrihodWindow)


    def showAddPrihodWindow(self):
        addPrihodWindow = addPrihod(self)
        addPrihodWindow.setWindowTitle('Приход - Новый Документ')
        addPrihodWindow.show()


# <<  Класс вкладки "Приходы"


# Класс вкладки "Уходы" >>

class UhodTab(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.uhodWidget = Ui_PrihodWidget()
        self.uhodWidget.setupUi(self)
        QtCore.QObject.connect(self.uhodWidget.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showAddUhodWindow)

    def showAddUhodWindow(self):
        addUhodWindow = addUhod(self)
        addUhodWindow.setWindowTitle('Уход - Новый Документ')
        addUhodWindow.show()

# << Класс вкладки "Уходы"


# Класс вкладки "Состояние склада" >>

class WhsStateTab(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.whsStateWidget = Ui_WhsStateForm()
        self.whsStateWidget.setupUi(self)
        self.whsStateWidget.splitter.setSizes([150, 500])


# <<Класс вкладки "Состояние склада"



# Класс окна добавления товара >>

class addUnitDialog(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.addUnitWidget = Ui_addGoods()
        self.addUnitWidget.setupUi(self)
        QtCore.QObject.connect(self.addUnitWidget.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.save_unit)
        self.addUnitWidget.NdsEdit.setText(str(NDS))



    def save_unit(self):
        #print ("Сохранить позицию")
        #print (self.addUnitWidget.NameEdit.text())
        #print (type(self.addUnitWidget.NameEdit.text()))
        if db_filename:
            if self.addUnitWidget.NameEdit.text():
                conn = sqlite3.connect(str(db_filename))
                cur = conn.cursor()
# Для наглядности -
# goodscatalog(article integer, name text, price real, brand text, country text, barcode0 integer, barcode1 integer, minimal integer, gruppa text, measure text, nds integer)
                cur.execute('insert into goodscatalog values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (int(self.addUnitWidget.ArticleEdit.text()),
                    self.addUnitWidget.NameEdit.text(), float(self.addUnitWidget.PriceEdit.text()),
                    self.addUnitWidget.BrendEdit.text(), self.addUnitWidget.CountryEdit.text(), 0, 0,
                    int(self.addUnitWidget.MinimalEdit.text()), 'Группа', self.addUnitWidget.MeasureEdit.text(), int(self.addUnitWidget.NdsEdit.text())))

                conn.commit()
                self.close()
                myapp.load_data('goodscatalog')
            else:
                err = QtGui.QMessageBox(self)
                err.setText('Введите название !')
                err.setIcon(2)
                err.show()
        else:
            #print ("База данных не выбрана !")
            err = QtGui.QMessageBox(self)
            err.setText('База данных не выбрана !')
            err.setIcon(2)
            err.show()




# << Класс окна добавления товара

# Класс окна редактирования товара >>

class editUnitDialog(addUnitDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.editUnitWidget = Ui_addGoods()
        self.editUnitWidget.setupUi(self)
        QtCore.QObject.connect(self.editUnitWidget.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.save_unit)
        #self.editUnitWidget.addGoods.setWindowTitle(QtGui.QApplication.translate("addGoods", "Изменение позиции", None, QtGui.QApplication.UnicodeUTF8))

        self.units = myapp.ui.tableWidget.selectedItems()
        self.row = myapp.ui.tableWidget.row(self.units[0])
        self.name = myapp.ui.tableWidget.item(myapp.ui.tableWidget.row(self.units[0]), 1).text()
        #print (self.name)

        conn=sqlite3.connect(str(db_filename))
        cur=conn.cursor()
        row = cur.execute('select * from goodscatalog where name=?', (self.name,))
        keyss = tuple([d[0] for d in cur.description]) # Получаем имена полей

        conn.commit()

        # Создаём словарь из строки базы >>
        for field in row:
            #print (field)
            row1 = field
        #print ('Ключи ', keyss)
        #print('ROW1 = ', row1)

        self.dictionary = dict(zip(keyss, row1))
        #print (self.dictionary)

        # << Создаём словарь из строки базы

        # Вывод данных и словаря в форму >>

        self.editUnitWidget.ArticleEdit.setText(str(self.dictionary['article']))
        self.editUnitWidget.NameEdit.setText(str(self.dictionary['name']))
        self.editUnitWidget.PriceEdit.setText(str(self.dictionary['price']))
        self.editUnitWidget.BrendEdit.setText(str(self.dictionary['brand']))
        self.editUnitWidget.CountryEdit.setText(str(self.dictionary['country']))
        self.editUnitWidget.NdsEdit.setText(str(self.dictionary['nds']))

        # Дописать !!

        # <<Вывод данных и словаря в форму

    def save_unit(self):
        #print ('Схранить изменения')
        if db_filename:
            if self.editUnitWidget.NameEdit.text():
                conn = sqlite3.connect(str(db_filename))
                cur = conn.cursor()
# Для наглядности -
# goodscatalog(article integer, name text, price real, brand text, country text, barcode0 integer, barcode1 integer, minimal integer, gruppa text, measure text, nds integer)
                cur.execute('delete from goodscatalog where name=?', (self.dictionary['name'],))
                cur.execute('insert into goodscatalog values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (int(self.editUnitWidget.ArticleEdit.text()),
                    self.editUnitWidget.NameEdit.text(), float(self.editUnitWidget.PriceEdit.text()),
                    self.editUnitWidget.BrendEdit.text(), self.editUnitWidget.CountryEdit.text(), 0, 0,
                    int(self.editUnitWidget.MinimalEdit.text()), 'Группа', self.editUnitWidget.MeasureEdit.text(), int(self.editUnitWidget.NdsEdit.text())))

                conn.commit()

                self.close()
                myapp.load_data('goodscatalog')
            else:
                err = QtGui.QMessageBox(self)
                err.setText('Введите название !')
                err.setIcon(2)
                err.show()
        else:
            #print ("База данных не выбрана !")
            err = QtGui.QMessageBox(self)
            err.setText('База данных не выбрана !')
            err.setIcon(2)
            err.show()


        self.close()
        myapp.load_data('goodscatalog')

# << Класс окна редактирования товара

# Класс окна копирования товара >>

class copyUnitDialog(editUnitDialog):

    def save_unit(self):
        if db_filename:
            if self.editUnitWidget.NameEdit.text():
                conn = sqlite3.connect(str(db_filename))
                cur = conn.cursor()
# Для наглядности -
# goodscatalog(article integer, name text, price real, brand text, country text, barcode0 integer, barcode1 integer, minimal integer, gruppa text, measure text, nds integer)
                cur.execute('insert into goodscatalog values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (int(self.editUnitWidget.ArticleEdit.text()),
                    self.editUnitWidget.NameEdit.text(), float(self.editUnitWidget.PriceEdit.text()),
                    self.editUnitWidget.BrendEdit.text(), self.editUnitWidget.CountryEdit.text(), 0, 0,
                    int(self.editUnitWidget.MinimalEdit.text()), 'Группа', self.editUnitWidget.MeasureEdit.text(), int(self.editUnitWidget.NdsEdit.text())))

                conn.commit()

                self.close()
                myapp.load_data('goodscatalog')
            else:
                err = QtGui.QMessageBox(self)
                err.setText('Введите название !')
                err.setIcon(2)
                err.show()
        else:
            #print ("База данных не выбрана !")
            err = QtGui.QMessageBox(self)
            err.setText('База данных не выбрана !')
            err.setIcon(2)
            err.show()


        self.close()
        myapp.load_data('goodscatalog')

# << Класс окна копирования товара



# Класс окна добавления прихода >>

class addPrihod(QtGui.QDialog):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.addPrihodWidget = Ui_addPrihodForm()
        self.addPrihodWidget.setupUi(self)
        QtCore.QObject.connect(self.addPrihodWidget.goodsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showChooseGoodsWindow)


    def showChooseGoodsWindow(self):
        chooseGoodsWindow = chooseGoods(self)
        chooseGoodsWindow.setWindowTitle('Справочник товаров')
        chooseGoodsWindow.show()

# << Класс окна добавления прихода


# Класс окна добавления ухода >>

class addUhod(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.addUhodWidget = Ui_addPrihodForm()
        self.addUhodWidget.setupUi(self)
        QtCore.QObject.connect(self.addUhodWidget.goodsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showChooseGoodsWindow)

    def showChooseGoodsWindow(self):
        chooseGoodsWindow = chooseGoods(self)
        chooseGoodsWindow.setWindowTitle('Справочник товаров')
        chooseGoodsWindow.show()

# << Класс окна добавления ухода


# Класс окна выбора товара >>

class chooseGoods(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.chooseGoodsWidget = Ui_ChooseGoodsForm()
        self.chooseGoodsWidget.setupUi(self)
        self.chooseGoodsWidget.splitter.setSizes([150, 500])
        self.loadData()

    def loadData(self):  # Дописать словарь !!!!!!!!!!
        if db_filename:
            print ("Loading data...")
            __sortingEnabled = self.chooseGoodsWidget.goodsTableWidget.isSortingEnabled()
            self.chooseGoodsWidget.goodsTableWidget.setSortingEnabled(False)
            # Задаём соответствие между полями БД и заголовками столбцов
            # Сделать это глобально ?
            dictionary = {'name': 'Название', 'article': 'Артикул', 'measure': 'Ед. изм.'}
            conn = sqlite3.connect(str(db_filename))
            cur = conn.cursor()
            for key in dictionary:
                query = ('select %s from goodscatalog' % key)
                line = 0
                cur.execute(query)
                rows = cur.fetchall()
                self.chooseGoodsWidget.goodsTableWidget.setRowCount(len(rows))
                for row in rows:
                    item = QtGui.QTableWidgetItem()
                    for i in range(self.chooseGoodsWidget.goodsTableWidget.columnCount()):
                        if self.chooseGoodsWidget.goodsTableWidget.horizontalHeaderItem(i).text() == dictionary[key]:
                            self.chooseGoodsWidget.goodsTableWidget.setItem(line, i, item)
                            item.setText(str(row[0]))

                    line += 1
                    print (row[0], dictionary[key])

            conn.commit()
            self.chooseGoodsWidget.goodsTableWidget.setSortingEnabled(__sortingEnabled)

# << Класс окна выбора товара




if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())


