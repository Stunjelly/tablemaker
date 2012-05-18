# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created: Fri May 18 19:11:35 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(879, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.webView = QtWebKit.QWebView(self.splitter)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setZoomFactor(1.0)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rulerBox = QtGui.QGroupBox(self.layoutWidget)
        self.rulerBox.setTitle(QtGui.QApplication.translate("MainWindow", "Rulers", None, QtGui.QApplication.UnicodeUTF8))
        self.rulerBox.setObjectName(_fromUtf8("rulerBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.rulerBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout.addWidget(self.rulerBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.addRuler = QtGui.QPushButton(self.layoutWidget)
        self.addRuler.setText(QtGui.QApplication.translate("MainWindow", "Add Ruler", None, QtGui.QApplication.UnicodeUTF8))
        self.addRuler.setObjectName(_fromUtf8("addRuler"))
        self.verticalLayout.addWidget(self.addRuler)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.zoomOut = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomOut.sizePolicy().hasHeightForWidth())
        self.zoomOut.setSizePolicy(sizePolicy)
        self.zoomOut.setMaximumSize(QtCore.QSize(30, 16777215))
        self.zoomOut.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOut.setObjectName(_fromUtf8("zoomOut"))
        self.horizontalLayout_4.addWidget(self.zoomOut)
        self.zoomIn = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomIn.sizePolicy().hasHeightForWidth())
        self.zoomIn.setSizePolicy(sizePolicy)
        self.zoomIn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.zoomIn.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomIn.setObjectName(_fromUtf8("zoomIn"))
        self.horizontalLayout_4.addWidget(self.zoomIn)
        self.previous = QtGui.QPushButton(self.layoutWidget)
        self.previous.setText(QtGui.QApplication.translate("MainWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.previous.setObjectName(_fromUtf8("previous"))
        self.horizontalLayout_4.addWidget(self.previous)
        self.next = QtGui.QPushButton(self.layoutWidget)
        self.next.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.next.setObjectName(_fromUtf8("next"))
        self.horizontalLayout_4.addWidget(self.next)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.chopPage = QtGui.QPushButton(self.layoutWidget)
        self.chopPage.setText(QtGui.QApplication.translate("MainWindow", "Chop", None, QtGui.QApplication.UnicodeUTF8))
        self.chopPage.setObjectName(_fromUtf8("chopPage"))
        self.verticalLayout.addWidget(self.chopPage)
        self.makehtml = QtGui.QPushButton(self.layoutWidget)
        self.makehtml.setText(QtGui.QApplication.translate("MainWindow", "Make HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.makehtml.setObjectName(_fromUtf8("makehtml"))
        self.verticalLayout.addWidget(self.makehtml)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

from PyQt4 import QtWebKit
