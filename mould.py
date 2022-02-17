# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mould.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QUndoView, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(800, 600)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.checkdbconn = QPushButton(self.centralwidget)
        self.checkdbconn.setObjectName(u"checkdbconn")
        self.checkdbconn.setGeometry(QRect(470, 0, 191, 101))
        self.checkdbconn.setCursor(QCursor(Qt.ArrowCursor))
        self.checkdbconn.setMouseTracking(False)
        self.checkdbconn.setCheckable(True)
        self.checkdbconn.setChecked(False)
        self.undoView = QUndoView(self.centralwidget)
        self.undoView.setObjectName(u"undoView")
        self.undoView.setGeometry(QRect(0, 0, 271, 421))
        self.instruction = QLabel(self.centralwidget)
        self.instruction.setObjectName(u"instruction")
        self.instruction.setGeometry(QRect(70, 0, 131, 31))
        self.instruction.setLayoutDirection(Qt.LeftToRight)
        self.instruction.setAlignment(Qt.AlignCenter)
        self.instruction.setOpenExternalLinks(False)
        self.firstcheck = QLabel(self.centralwidget)
        self.firstcheck.setObjectName(u"firstcheck")
        self.firstcheck.setGeometry(QRect(10, 40, 171, 31))
        self.dbcheckbox = QCheckBox(self.centralwidget)
        self.dbcheckbox.setObjectName(u"dbcheckbox")
        self.dbcheckbox.setEnabled(True)
        self.dbcheckbox.setGeometry(QRect(220, 40, 21, 31))
        self.dbcheckbox.setIconSize(QSize(16, 16))
        self.dbcheckbox.setCheckable(False)
        self.dbcheckbox.setChecked(False)
        self.dbcheckinfolabel = QLabel(self.centralwidget)
        self.dbcheckinfolabel.setObjectName(u"dbcheckinfolabel")
        self.dbcheckinfolabel.setEnabled(False)
        self.dbcheckinfolabel.setGeometry(QRect(20, 70, 211, 31))
        self.secondcheck = QLabel(self.centralwidget)
        self.secondcheck.setObjectName(u"secondcheck")
        self.secondcheck.setGeometry(QRect(10, 120, 171, 31))
        self.filecheckbox = QCheckBox(self.centralwidget)
        self.filecheckbox.setObjectName(u"filecheckbox")
        self.filecheckbox.setEnabled(True)
        self.filecheckbox.setGeometry(QRect(220, 120, 81, 31))
        self.filecheckbox.setCheckable(False)
        self.filecheckinfolabel = QLabel(self.centralwidget)
        self.filecheckinfolabel.setObjectName(u"filecheckinfolabel")
        self.filecheckinfolabel.setEnabled(False)
        self.filecheckinfolabel.setGeometry(QRect(20, 160, 211, 31))
        self.filecheck = QPushButton(self.centralwidget)
        self.filecheck.setObjectName(u"filecheck")
        self.filecheck.setGeometry(QRect(470, 120, 191, 101))
        self.thirdcheck = QLabel(self.centralwidget)
        self.thirdcheck.setObjectName(u"thirdcheck")
        self.thirdcheck.setGeometry(QRect(10, 200, 171, 31))
        self.startinputing = QPushButton(self.centralwidget)
        self.startinputing.setObjectName(u"startinputing")
        self.startinputing.setGeometry(QRect(470, 240, 191, 101))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QRect(10, 290, 241, 21))
        self.progressBar.setValue(24)
        self.startinputinginfolabel = QLabel(self.centralwidget)
        self.startinputinginfolabel.setObjectName(u"startinputinginfolabel")
        self.startinputinginfolabel.setEnabled(False)
        self.startinputinginfolabel.setGeometry(QRect(20, 240, 211, 31))
        self.fileaddr = QLabel(self.centralwidget)
        self.fileaddr.setObjectName(u"fileaddr")
        self.fileaddr.setEnabled(False)
        self.fileaddr.setGeometry(QRect(120, 210, 53, 16))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u6848\u4f8b\u5e93\u5feb\u901f\u5bfc\u5165\uff08QT)", None))
        self.checkdbconn.setText(QCoreApplication.translate("mainWindow", u"\u68c0\u67e5\u6570\u636e\u5e93\u8fde\u63a5", None))
        self.instruction.setText(QCoreApplication.translate("mainWindow", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.firstcheck.setText(QCoreApplication.translate("mainWindow", u"1\u3001\u6570\u636e\u5e93\u8fde\u63a5\u662f\u5426\u5df2\u8fde\u63a5", None))
        self.dbcheckbox.setText("")
        self.dbcheckinfolabel.setText("")
        self.secondcheck.setText(QCoreApplication.translate("mainWindow", u"2\u3001\u68c0\u67e5\u5bfc\u5165\u6587\u4ef6\u683c\u5f0f\u662f\u5426\u6b63\u786e", None))
        self.filecheckbox.setText("")
        self.filecheckinfolabel.setText("")
        self.filecheck.setText(QCoreApplication.translate("mainWindow", u"\u68c0\u67e5\u6587\u4ef6\u683c\u5f0f", None))
        self.thirdcheck.setText(QCoreApplication.translate("mainWindow", u"3\u3001\u5f00\u59cb\u5bfc\u5165", None))
        self.startinputing.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u59cb\u5bfc\u5165", None))
        self.startinputinginfolabel.setText("")
        self.fileaddr.setText("")
    # retranslateUi

