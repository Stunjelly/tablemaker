# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nic/workspace/tablessplitter/basic.ui'
#
# Created: Mon Apr 30 15:57:30 2012
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
        self.webView.setObjectName(_fromUtf8("webView"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.split1x = QtGui.QSpinBox(self.widget)
        self.split1x.setObjectName(_fromUtf8("split1x"))
        self.horizontalLayout.addWidget(self.split1x)
        self.split1y = QtGui.QSpinBox(self.widget)
        self.split1y.setObjectName(_fromUtf8("split1y"))
        self.horizontalLayout.addWidget(self.split1y)
        self.include1 = QtGui.QCheckBox(self.widget)
        self.include1.setText(QtGui.QApplication.translate("MainWindow", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.include1.setChecked(True)
        self.include1.setObjectName(_fromUtf8("include1"))
        self.horizontalLayout.addWidget(self.include1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.split2x = QtGui.QSpinBox(self.widget)
        self.split2x.setObjectName(_fromUtf8("split2x"))
        self.horizontalLayout_2.addWidget(self.split2x)
        self.split2y = QtGui.QSpinBox(self.widget)
        self.split2y.setObjectName(_fromUtf8("split2y"))
        self.horizontalLayout_2.addWidget(self.split2y)
        self.include2 = QtGui.QCheckBox(self.widget)
        self.include2.setText(QtGui.QApplication.translate("MainWindow", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.include2.setChecked(True)
        self.include2.setObjectName(_fromUtf8("include2"))
        self.horizontalLayout_2.addWidget(self.include2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.split3x = QtGui.QSpinBox(self.widget)
        self.split3x.setObjectName(_fromUtf8("split3x"))
        self.horizontalLayout_3.addWidget(self.split3x)
        self.split3y = QtGui.QSpinBox(self.widget)
        self.split3y.setObjectName(_fromUtf8("split3y"))
        self.horizontalLayout_3.addWidget(self.split3y)
        self.include3 = QtGui.QCheckBox(self.widget)
        self.include3.setText(QtGui.QApplication.translate("MainWindow", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.include3.setChecked(True)
        self.include3.setObjectName(_fromUtf8("include3"))
        self.horizontalLayout_3.addWidget(self.include3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.previous = QtGui.QPushButton(self.widget)
        self.previous.setText(QtGui.QApplication.translate("MainWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.previous.setObjectName(_fromUtf8("previous"))
        self.horizontalLayout_4.addWidget(self.previous)
        self.next = QtGui.QPushButton(self.widget)
        self.next.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.next.setObjectName(_fromUtf8("next"))
        self.horizontalLayout_4.addWidget(self.next)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.makehtml = QtGui.QPushButton(self.widget)
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
