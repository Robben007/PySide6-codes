# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rhQuant_matplotlib_show.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 763, 571))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_show_dataPre = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_show_dataPre.sizePolicy().hasHeightForWidth())
        self.pushButton_show_dataPre.setSizePolicy(sizePolicy)
        self.pushButton_show_dataPre.setObjectName("pushButton_show_dataPre")
        self.horizontalLayout_2.addWidget(self.pushButton_show_dataPre)
        self.pushButton_show_trade_flow = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_show_trade_flow.sizePolicy().hasHeightForWidth())
        self.pushButton_show_trade_flow.setSizePolicy(sizePolicy)
        self.pushButton_show_trade_flow.setObjectName("pushButton_show_trade_flow")
        self.horizontalLayout_2.addWidget(self.pushButton_show_trade_flow)
        self.pushButton_show_money_flow = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_show_money_flow.sizePolicy().hasHeightForWidth())
        self.pushButton_show_money_flow.setSizePolicy(sizePolicy)
        self.pushButton_show_money_flow.setObjectName("pushButton_show_money_flow")
        self.horizontalLayout_2.addWidget(self.pushButton_show_money_flow)
        self.pushButton_hide_output = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_hide_output.sizePolicy().hasHeightForWidth())
        self.pushButton_hide_output.setSizePolicy(sizePolicy)
        self.pushButton_hide_output.setCheckable(True)
        self.pushButton_hide_output.setChecked(True)
        self.pushButton_hide_output.setObjectName("pushButton_hide_output")
        self.horizontalLayout_2.addWidget(self.pushButton_hide_output)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 210))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.matplotlibwidget_static = MatplotlibWidget(self.scrollAreaWidgetContents)
        self.matplotlibwidget_static.setMinimumSize(QtCore.QSize(0, 100))
        self.matplotlibwidget_static.setObjectName("matplotlibwidget_static")
        self.verticalLayout.addWidget(self.matplotlibwidget_static)
        self.matplotlibwidget_day = MatplotlibWidget(self.scrollAreaWidgetContents)
        self.matplotlibwidget_day.setMinimumSize(QtCore.QSize(0, 200))
        self.matplotlibwidget_day.setObjectName("matplotlibwidget_day")
        self.verticalLayout.addWidget(self.matplotlibwidget_day)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_hide_output.clicked['bool'].connect(self.tableWidget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_show_dataPre.setText(_translate("MainWindow", "查看数据处理(随机)"))
        self.pushButton_show_trade_flow.setText(_translate("MainWindow", "查看交易流水"))
        self.pushButton_show_money_flow.setText(_translate("MainWindow", "查看资金流水"))
        self.pushButton_hide_output.setText(_translate("MainWindow", "隐藏输出结果"))


try: # 为了模块引用
    from .rhMatplotlibWidget import MatplotlibWidget
except: # 为了直接运行
    from rhMatplotlibWidget import MatplotlibWidget
