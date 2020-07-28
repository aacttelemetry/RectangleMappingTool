# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kisun\Desktop\RectangleMappingTool\src\main\resources\base\rectmap.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(908, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 4)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setText("")
        self.toolButton.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 5, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(400, 300))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 1, 0, 2, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setEnabled(True)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 6, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.gridLayout.addWidget(self.tableWidget, 0, 3, 4, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionUndo_toolbar = QtWidgets.QAction(MainWindow)
        self.actionUndo_toolbar.setObjectName("actionUndo_toolbar")
        self.actionOpen_image = QtWidgets.QAction(MainWindow)
        self.actionOpen_image.setObjectName("actionOpen_image")
        self.actionSave_image_as = QtWidgets.QAction(MainWindow)
        self.actionSave_image_as.setObjectName("actionSave_image_as")
        self.actionExport_coordinates = QtWidgets.QAction(MainWindow)
        self.actionExport_coordinates.setObjectName("actionExport_coordinates")
        self.actionExport_coordinates_2 = QtWidgets.QAction(MainWindow)
        self.actionExport_coordinates_2.setObjectName("actionExport_coordinates_2")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGitHub_Repository = QtWidgets.QAction(MainWindow)
        self.actionGitHub_Repository.setObjectName("actionGitHub_Repository")
        self.actionPen_Color = QtWidgets.QAction(MainWindow)
        self.actionPen_Color.setObjectName("actionPen_Color")
        self.actionPen_Width = QtWidgets.QAction(MainWindow)
        self.actionPen_Width.setObjectName("actionPen_Width")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.menuFile.addAction(self.actionOpen_image)
        self.menuFile.addAction(self.actionSave_image_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_coordinates)
        self.menuFile.addAction(self.actionExport_coordinates_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuSettings.addAction(self.actionPen_Color)
        self.menuSettings.addAction(self.actionPen_Width)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionGitHub_Repository)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionUndo_toolbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "add table row"))
        self.pushButton_2.setText(_translate("MainWindow", "delete table row"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "x2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "y2"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "200"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "300"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "400"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionUndo_toolbar.setText(_translate("MainWindow", "Undo"))
        self.actionUndo_toolbar.setToolTip(_translate("MainWindow", "Undo the last drawn rectangle."))
        self.actionOpen_image.setText(_translate("MainWindow", "Open image..."))
        self.actionOpen_image.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_image_as.setText(_translate("MainWindow", "Save image as..."))
        self.actionExport_coordinates.setText(_translate("MainWindow", "Save coordinates..."))
        self.actionExport_coordinates_2.setText(_translate("MainWindow", "Export coordinates..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionGitHub_Repository.setText(_translate("MainWindow", "GitHub Repository"))
        self.actionPen_Color.setText(_translate("MainWindow", "Pen Color"))
        self.actionPen_Width.setText(_translate("MainWindow", "Pen Width"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
