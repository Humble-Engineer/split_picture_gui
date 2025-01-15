# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 820)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1500, 820))
        MainWindow.setMaximumSize(QSize(1500, 825))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setIconSize(QSize(48, 48))
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.result_img = QLabel(self.centralwidget)
        self.result_img.setObjectName(u"result_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.result_img.sizePolicy().hasHeightForWidth())
        self.result_img.setSizePolicy(sizePolicy1)
        self.result_img.setMinimumSize(QSize(1200, 800))
        self.result_img.setMaximumSize(QSize(1200, 800))
        self.result_img.setFrameShape(QFrame.Shape.Panel)

        self.gridLayout.addWidget(self.result_img, 0, 0, 3, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.load_button.sizePolicy().hasHeightForWidth())
        self.load_button.setSizePolicy(sizePolicy2)
        self.load_button.setMinimumSize(QSize(90, 50))
        self.load_button.setMaximumSize(QSize(9999999, 16777215))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.load_button.setFont(font1)

        self.gridLayout_2.addWidget(self.load_button, 1, 0, 1, 1)

        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy2.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy2)
        self.reset_button.setMinimumSize(QSize(90, 50))
        self.reset_button.setMaximumSize(QSize(9999999, 16777215))
        self.reset_button.setFont(font1)

        self.gridLayout_2.addWidget(self.reset_button, 3, 0, 1, 1)

        self.capture_button = QPushButton(self.centralwidget)
        self.capture_button.setObjectName(u"capture_button")
        self.capture_button.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.capture_button.sizePolicy().hasHeightForWidth())
        self.capture_button.setSizePolicy(sizePolicy2)
        self.capture_button.setMinimumSize(QSize(90, 50))
        self.capture_button.setMaximumSize(QSize(9999999, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.capture_button.setFont(font2)

        self.gridLayout_2.addWidget(self.capture_button, 2, 0, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setMaximumSize(QSize(285, 25))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_14.setFont(font3)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 2)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        sizePolicy2.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy2)
        self.save_button.setMinimumSize(QSize(90, 50))
        self.save_button.setMaximumSize(QSize(9999999, 16777215))
        self.save_button.setFont(font1)

        self.gridLayout_2.addWidget(self.save_button, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.blur_layout = QVBoxLayout()
        self.blur_layout.setSpacing(0)
        self.blur_layout.setObjectName(u"blur_layout")
        self.blur_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setMaximumSize(QSize(285, 25))
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.blur_layout.addWidget(self.label_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.rows_label_2 = QLabel(self.centralwidget)
        self.rows_label_2.setObjectName(u"rows_label_2")
        self.rows_label_2.setMaximumSize(QSize(78, 53))

        self.horizontalLayout_9.addWidget(self.rows_label_2)

        self.rows_Slider = QSlider(self.centralwidget)
        self.rows_Slider.setObjectName(u"rows_Slider")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(30)
        sizePolicy4.setHeightForWidth(self.rows_Slider.sizePolicy().hasHeightForWidth())
        self.rows_Slider.setSizePolicy(sizePolicy4)
        self.rows_Slider.setMaximumSize(QSize(185, 9999999))
        self.rows_Slider.setMinimum(1)
        self.rows_Slider.setMaximum(10)
        self.rows_Slider.setPageStep(1)
        self.rows_Slider.setValue(3)
        self.rows_Slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_9.addWidget(self.rows_Slider)

        self.rows_label = QLabel(self.centralwidget)
        self.rows_label.setObjectName(u"rows_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(30)
        sizePolicy5.setHeightForWidth(self.rows_label.sizePolicy().hasHeightForWidth())
        self.rows_label.setSizePolicy(sizePolicy5)
        self.rows_label.setMinimumSize(QSize(30, 0))
        self.rows_label.setMaximumSize(QSize(24, 53))
        self.rows_label.setMidLineWidth(4)

        self.horizontalLayout_9.addWidget(self.rows_label)


        self.blur_layout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cols_label_2 = QLabel(self.centralwidget)
        self.cols_label_2.setObjectName(u"cols_label_2")
        self.cols_label_2.setMaximumSize(QSize(78, 52))

        self.horizontalLayout_10.addWidget(self.cols_label_2)

        self.cols_Slider = QSlider(self.centralwidget)
        self.cols_Slider.setObjectName(u"cols_Slider")
        sizePolicy4.setHeightForWidth(self.cols_Slider.sizePolicy().hasHeightForWidth())
        self.cols_Slider.setSizePolicy(sizePolicy4)
        self.cols_Slider.setMaximumSize(QSize(185, 9999999))
        self.cols_Slider.setMinimum(1)
        self.cols_Slider.setMaximum(12)
        self.cols_Slider.setPageStep(1)
        self.cols_Slider.setValue(4)
        self.cols_Slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_10.addWidget(self.cols_Slider)

        self.cols_label = QLabel(self.centralwidget)
        self.cols_label.setObjectName(u"cols_label")
        sizePolicy5.setHeightForWidth(self.cols_label.sizePolicy().hasHeightForWidth())
        self.cols_label.setSizePolicy(sizePolicy5)
        self.cols_label.setMinimumSize(QSize(30, 0))
        self.cols_label.setMaximumSize(QSize(24, 53))
        self.cols_label.setMidLineWidth(4)

        self.horizontalLayout_10.addWidget(self.cols_label)


        self.blur_layout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.r_label_2 = QLabel(self.centralwidget)
        self.r_label_2.setObjectName(u"r_label_2")
        self.r_label_2.setMaximumSize(QSize(77, 53))

        self.horizontalLayout_11.addWidget(self.r_label_2)

        self.r_Slider = QSlider(self.centralwidget)
        self.r_Slider.setObjectName(u"r_Slider")
        sizePolicy4.setHeightForWidth(self.r_Slider.sizePolicy().hasHeightForWidth())
        self.r_Slider.setSizePolicy(sizePolicy4)
        self.r_Slider.setMaximumSize(QSize(185, 9999999))
        self.r_Slider.setMinimum(1)
        self.r_Slider.setMaximum(8)
        self.r_Slider.setSingleStep(1)
        self.r_Slider.setPageStep(1)
        self.r_Slider.setValue(5)
        self.r_Slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_11.addWidget(self.r_Slider)

        self.r_label = QLabel(self.centralwidget)
        self.r_label.setObjectName(u"r_label")
        sizePolicy5.setHeightForWidth(self.r_label.sizePolicy().hasHeightForWidth())
        self.r_label.setSizePolicy(sizePolicy5)
        self.r_label.setMinimumSize(QSize(30, 0))
        self.r_label.setMaximumSize(QSize(24, 53))
        self.r_label.setMidLineWidth(4)

        self.horizontalLayout_11.addWidget(self.r_label)


        self.blur_layout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.blur_layout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.r_label_3 = QLabel(self.centralwidget)
        self.r_label_3.setObjectName(u"r_label_3")
        self.r_label_3.setMaximumSize(QSize(77, 53))

        self.horizontalLayout_12.addWidget(self.r_label_3)

        self.precision_Slider = QSlider(self.centralwidget)
        self.precision_Slider.setObjectName(u"precision_Slider")
        sizePolicy4.setHeightForWidth(self.precision_Slider.sizePolicy().hasHeightForWidth())
        self.precision_Slider.setSizePolicy(sizePolicy4)
        self.precision_Slider.setMaximumSize(QSize(185, 9999999))
        self.precision_Slider.setMinimum(3)
        self.precision_Slider.setMaximum(5)
        self.precision_Slider.setSingleStep(1)
        self.precision_Slider.setPageStep(1)
        self.precision_Slider.setValue(4)
        self.precision_Slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_12.addWidget(self.precision_Slider)

        self.precision_label = QLabel(self.centralwidget)
        self.precision_label.setObjectName(u"precision_label")
        sizePolicy5.setHeightForWidth(self.precision_label.sizePolicy().hasHeightForWidth())
        self.precision_label.setSizePolicy(sizePolicy5)
        self.precision_label.setMinimumSize(QSize(30, 0))
        self.precision_label.setMaximumSize(QSize(24, 53))
        self.precision_label.setMidLineWidth(4)

        self.horizontalLayout_12.addWidget(self.precision_label)


        self.blur_layout.addLayout(self.horizontalLayout_12)


        self.gridLayout.addLayout(self.blur_layout, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.default_button = QPushButton(self.centralwidget)
        self.default_button.setObjectName(u"default_button")
        sizePolicy2.setHeightForWidth(self.default_button.sizePolicy().hasHeightForWidth())
        self.default_button.setSizePolicy(sizePolicy2)
        self.default_button.setMinimumSize(QSize(90, 50))
        self.default_button.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.default_button.setFont(font4)

        self.verticalLayout.addWidget(self.default_button)

        self.MatLayout = QVBoxLayout()
        self.MatLayout.setObjectName(u"MatLayout")
        self.MatLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.MatLayout.setContentsMargins(-1, 0, 0, 0)

        self.verticalLayout.addLayout(self.MatLayout)

        self.count_button = QPushButton(self.centralwidget)
        self.count_button.setObjectName(u"count_button")
        sizePolicy2.setHeightForWidth(self.count_button.sizePolicy().hasHeightForWidth())
        self.count_button.setSizePolicy(sizePolicy2)
        self.count_button.setMinimumSize(QSize(90, 50))
        self.count_button.setMaximumSize(QSize(16777215, 16777215))
        self.count_button.setFont(font4)

        self.verticalLayout.addWidget(self.count_button)


        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"split picture", None))
        self.result_img.setText("")
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u56fe\u50cf", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u539f\u56fe", None))
        self.capture_button.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u6355\u83b7", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u64cd\u4f5c", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u56fe\u50cf", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5272\u53c2\u6570", None))
        self.rows_label_2.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5272\u884c\u6570\uff1a", None))
        self.rows_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cols_label_2.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5272\u5217\u6570\uff1a", None))
        self.cols_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r_label_2.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u534a\u5f84\uff1a", None))
        self.r_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r_label_3.setText(QCoreApplication.translate("MainWindow", u"\u6709\u6548\u6570\u5b57\uff1a", None))
        self.precision_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.default_button.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u53c2\u6570", None))
        self.count_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8ba1\u6570", None))
    # retranslateUi

