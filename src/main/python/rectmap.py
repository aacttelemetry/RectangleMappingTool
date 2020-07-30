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
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1028, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.container_left = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container_left.sizePolicy().hasHeightForWidth())
        self.container_left.setSizePolicy(sizePolicy)
        self.container_left.setMinimumSize(QtCore.QSize(400, 300))
        self.container_left.setObjectName("container_left")
        self.gridLayout.addWidget(self.container_left, 0, 0, 1, 1)
        self.coord_label = QtWidgets.QLabel(self.centralwidget)
        self.coord_label.setAlignment(QtCore.Qt.AlignCenter)
        self.coord_label.setObjectName("coord_label")
        self.gridLayout.addWidget(self.coord_label, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 2, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMaximumSize(QtCore.QSize(599, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.current_selected_label = QtWidgets.QLabel(self.tab)
        self.current_selected_label.setWordWrap(True)
        self.current_selected_label.setObjectName("current_selected_label")
        self.verticalLayout_2.addWidget(self.current_selected_label)
        self.current_coordinates_label = QtWidgets.QLabel(self.tab)
        self.current_coordinates_label.setWordWrap(True)
        self.current_coordinates_label.setObjectName("current_coordinates_label")
        self.verticalLayout_2.addWidget(self.current_coordinates_label)
        self.current_overlaps_label = QtWidgets.QLabel(self.tab)
        self.current_overlaps_label.setWordWrap(True)
        self.current_overlaps_label.setObjectName("current_overlaps_label")
        self.verticalLayout_2.addWidget(self.current_overlaps_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.delete_rect_button = QtWidgets.QPushButton(self.tab)
        self.delete_rect_button.setObjectName("delete_rect_button")
        self.verticalLayout_3.addWidget(self.delete_rect_button)
        self.change_rect_color_button = QtWidgets.QPushButton(self.tab)
        self.change_rect_color_button.setObjectName("change_rect_color_button")
        self.verticalLayout_3.addWidget(self.change_rect_color_button)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.table_widget = QtWidgets.QTableWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy)
        self.table_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(5)
        self.table_widget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(4, item)
        self.table_widget.horizontalHeader().setDefaultSectionSize(110)
        self.verticalLayout_4.addWidget(self.table_widget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.conv_x1_edit = QtWidgets.QLineEdit(self.tab_2)
        self.conv_x1_edit.setObjectName("conv_x1_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.conv_x1_edit)
        self.conv_x1_label = QtWidgets.QLabel(self.tab_2)
        self.conv_x1_label.setObjectName("conv_x1_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.conv_x1_label)
        self.conv_y1_edit = QtWidgets.QLineEdit(self.tab_2)
        self.conv_y1_edit.setObjectName("conv_y1_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.conv_y1_edit)
        self.conv_y1_label = QtWidgets.QLabel(self.tab_2)
        self.conv_y1_label.setObjectName("conv_y1_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.conv_y1_label)
        self.conv_x2_edit = QtWidgets.QLineEdit(self.tab_2)
        self.conv_x2_edit.setObjectName("conv_x2_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.conv_x2_edit)
        self.conv_x2_label = QtWidgets.QLabel(self.tab_2)
        self.conv_x2_label.setObjectName("conv_x2_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.conv_x2_label)
        self.conv_y2_edit = QtWidgets.QLineEdit(self.tab_2)
        self.conv_y2_edit.setObjectName("conv_y2_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.conv_y2_edit)
        self.conv_y2_label = QtWidgets.QLabel(self.tab_2)
        self.conv_y2_label.setObjectName("conv_y2_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.conv_y2_label)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setWordWrap(False)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.converted_table_widget = QtWidgets.QTableWidget(self.tab_2)
        self.converted_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.converted_table_widget.setObjectName("converted_table_widget")
        self.converted_table_widget.setColumnCount(4)
        self.converted_table_widget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.converted_table_widget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.converted_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.converted_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.converted_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.converted_table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.converted_table_widget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.converted_table_widget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.converted_table_widget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.converted_table_widget.setItem(0, 3, item)
        self.converted_table_widget.horizontalHeader().setDefaultSectionSize(142)
        self.verticalLayout_5.addWidget(self.converted_table_widget)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.line_4 = QtWidgets.QFrame(self.tab_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.raw_radio_button = QtWidgets.QRadioButton(self.tab_4)
        self.raw_radio_button.setObjectName("raw_radio_button")
        self.horizontalLayout_2.addWidget(self.raw_radio_button)
        self.converted_radio_button = QtWidgets.QRadioButton(self.tab_4)
        self.converted_radio_button.setObjectName("converted_radio_button")
        self.horizontalLayout_2.addWidget(self.converted_radio_button)
        self.all_radio_button = QtWidgets.QRadioButton(self.tab_4)
        self.all_radio_button.setObjectName("all_radio_button")
        self.horizontalLayout_2.addWidget(self.all_radio_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.selection_label = QtWidgets.QLabel(self.tab_4)
        self.selection_label.setWordWrap(True)
        self.selection_label.setObjectName("selection_label")
        self.verticalLayout.addWidget(self.selection_label)
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.overlaps_checkbox = QtWidgets.QCheckBox(self.tab_4)
        self.overlaps_checkbox.setObjectName("overlaps_checkbox")
        self.horizontalLayout_3.addWidget(self.overlaps_checkbox)
        self.color_checkbox = QtWidgets.QCheckBox(self.tab_4)
        self.color_checkbox.setObjectName("color_checkbox")
        self.horizontalLayout_3.addWidget(self.color_checkbox)
        self.custom_checkbox = QtWidgets.QCheckBox(self.tab_4)
        self.custom_checkbox.setObjectName("custom_checkbox")
        self.horizontalLayout_3.addWidget(self.custom_checkbox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.export_csv_button = QtWidgets.QPushButton(self.tab_4)
        self.export_csv_button.setObjectName("export_csv_button")
        self.verticalLayout.addWidget(self.export_csv_button)
        self.line_5 = QtWidgets.QFrame(self.tab_4)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.vars_label = QtWidgets.QLabel(self.tab_4)
        self.vars_label.setWordWrap(True)
        self.vars_label.setObjectName("vars_label")
        self.verticalLayout.addWidget(self.vars_label)
        self.fstring_edit = QtWidgets.QPlainTextEdit(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.fstring_edit.setFont(font)
        self.fstring_edit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.fstring_edit.setObjectName("fstring_edit")
        self.verticalLayout.addWidget(self.fstring_edit)
        self.open_external_fstring = QtWidgets.QPushButton(self.tab_4)
        self.open_external_fstring.setObjectName("open_external_fstring")
        self.verticalLayout.addWidget(self.open_external_fstring)
        self.export_txt_button = QtWidgets.QPushButton(self.tab_4)
        self.export_txt_button.setObjectName("export_txt_button")
        self.verticalLayout.addWidget(self.export_txt_button)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_3)
        self.formLayout_2.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_2.setObjectName("formLayout_2")
        self.active_redraw_checkbox = QtWidgets.QCheckBox(self.tab_3)
        self.active_redraw_checkbox.setText("")
        self.active_redraw_checkbox.setObjectName("active_redraw_checkbox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.active_redraw_checkbox)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.active_table_checkbox = QtWidgets.QCheckBox(self.tab_3)
        self.active_table_checkbox.setText("")
        self.active_table_checkbox.setObjectName("active_table_checkbox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.active_table_checkbox)
        self.check_overlaps_checkbox = QtWidgets.QCheckBox(self.tab_3)
        self.check_overlaps_checkbox.setText("")
        self.check_overlaps_checkbox.setObjectName("check_overlaps_checkbox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.check_overlaps_checkbox)
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.set_color_button = QtWidgets.QPushButton(self.tab_3)
        self.set_color_button.setObjectName("set_color_button")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.set_color_button)
        self.set_width_button = QtWidgets.QPushButton(self.tab_3)
        self.set_width_button.setObjectName("set_width_button")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.set_width_button)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.label_11)
        self.active_overlaps_checkbox = QtWidgets.QCheckBox(self.tab_3)
        self.active_overlaps_checkbox.setEnabled(True)
        self.active_overlaps_checkbox.setText("")
        self.active_overlaps_checkbox.setObjectName("active_overlaps_checkbox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.active_overlaps_checkbox)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_12)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 2, 1, 1)
        self.line.raise_()
        self.coord_label.raise_()
        self.container_left.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
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
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionGitHub_Repository)
        self.menuSettings.addAction(self.actionPen_Color)
        self.menuSettings.addAction(self.actionPen_Width)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionUndo_toolbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.coord_label.setText(_translate("MainWindow", "x: 0 y: 0"))
        self.current_selected_label.setText(_translate("MainWindow", "Currently selected: Rectangle 1"))
        self.current_coordinates_label.setText(_translate("MainWindow", "Coordinates: x1, y1, x2, y2"))
        self.current_overlaps_label.setText(_translate("MainWindow", "Overlaps with: 1, 2, 3"))
        self.delete_rect_button.setText(_translate("MainWindow", "Delete"))
        self.change_rect_color_button.setText(_translate("MainWindow", "Change color"))
        item = self.table_widget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x1"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y1"))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "x2"))
        item = self.table_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "y2"))
        item = self.table_widget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Overlaps with:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Coordinate Table"))
        self.label_2.setText(_translate("MainWindow", "You can define the equivalent points for the top-left and bottom-right corners of the drawing area, which will allow you to convert the pixel-based coordinates of a rectangle into a different numerical format (such as GPS bounding coordinates)."))
        self.conv_x1_label.setText(_translate("MainWindow", "Top-left, x (x = 0 px)"))
        self.conv_y1_label.setText(_translate("MainWindow", "Top-left, y (y = 0 px)"))
        self.conv_x2_label.setText(_translate("MainWindow", "Bottom-right, x (x = ... px)"))
        self.conv_y2_label.setText(_translate("MainWindow", "Bottom-right, y (y = ... px)"))
        self.label_19.setText(_translate("MainWindow", "The converted coordinates will be shown below (read-only):"))
        item = self.converted_table_widget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.converted_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x1"))
        item = self.converted_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y1"))
        item = self.converted_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "x2"))
        item = self.converted_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "y2"))
        __sortingEnabled = self.converted_table_widget.isSortingEnabled()
        self.converted_table_widget.setSortingEnabled(False)
        self.converted_table_widget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Conversion"))
        self.label_3.setText(_translate("MainWindow", "You can export the coordinates (raw or converted) into a .csv; alternatively, you can also define an f-string to use, which will export the data to a .txt file."))
        self.label_13.setText(_translate("MainWindow", "Export: .csv"))
        self.raw_radio_button.setText(_translate("MainWindow", "Raw coordinates"))
        self.converted_radio_button.setText(_translate("MainWindow", "Converted coordinates"))
        self.all_radio_button.setText(_translate("MainWindow", "Both"))
        self.selection_label.setText(_translate("MainWindow", "Selection description... Export the raw coordinates of the drawn rectangles, pixel based. The format is ...."))
        self.label.setText(_translate("MainWindow", "You can also add the following fields:"))
        self.overlaps_checkbox.setText(_translate("MainWindow", "Overlaps"))
        self.color_checkbox.setText(_translate("MainWindow", "Color"))
        self.custom_checkbox.setText(_translate("MainWindow", "Custom fields"))
        self.export_csv_button.setText(_translate("MainWindow", "Export to .csv"))
        self.label_15.setText(_translate("MainWindow", "Export: f-string"))
        self.label_16.setText(_translate("MainWindow", "The below will be passed directly through an eval() statement and will be executed for each rectangle, with results newline separated. The available values are defined by the columns in the coordinate table, and are shown below."))
        self.vars_label.setText(_translate("MainWindow", "Available variables: x1, y1, x2, y2, x1_conv, y1_conv, x2_conv, y2_conv, overlaps, color"))
        self.fstring_edit.setPlainText(_translate("MainWindow", "if {x1_conv} <= {x2_conv} and {y1_conv} <= {y2_conv}:\n"
"    pass"))
        self.open_external_fstring.setText(_translate("MainWindow", "Open f-string edit in new window"))
        self.export_txt_button.setText(_translate("MainWindow", "Export to .txt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Export Data"))
        self.label_4.setText(_translate("MainWindow", "Redraw rectangles in real-time (during mousedown)."))
        self.set_color_button.setText(_translate("MainWindow", "Set default color"))
        self.set_width_button.setText(_translate("MainWindow", "Set default pen width"))
        self.label_8.setText(_translate("MainWindow", "Optimization"))
        self.label_9.setText(_translate("MainWindow", "Update table in real-time."))
        self.label_10.setText(_translate("MainWindow", "Calculate overlapping rectangles."))
        self.label_11.setText(_translate("MainWindow", "Appearance"))
        self.label_12.setText(_translate("MainWindow", "Calculate overlapping rectangles in real-time."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
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
