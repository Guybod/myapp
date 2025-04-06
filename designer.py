# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designer.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(686, 633)
        self.horizontalLayout_10 = QHBoxLayout(Form)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tab1_ipframe = QFrame(self.tabWidgetPage1)
        self.tab1_ipframe.setObjectName(u"tab1_ipframe")
        self.tab1_ipframe.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.tab1_ipframe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.IPlabel = QLabel(self.tab1_ipframe)
        self.IPlabel.setObjectName(u"IPlabel")

        self.horizontalLayout.addWidget(self.IPlabel)

        self.IPEdit = QLineEdit(self.tab1_ipframe)
        self.IPEdit.setObjectName(u"IPEdit")
        self.IPEdit.setMaximumSize(QSize(300, 25))

        self.horizontalLayout.addWidget(self.IPEdit)

        self.connect = QPushButton(self.tab1_ipframe)
        self.connect.setObjectName(u"connect")
        self.connect.setMinimumSize(QSize(75, 25))
        self.connect.setMaximumSize(QSize(75, 25))

        self.horizontalLayout.addWidget(self.connect)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.tab1_ipframe)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.state_label = QLabel(self.tab1_ipframe)
        self.state_label.setObjectName(u"state_label")

        self.horizontalLayout.addWidget(self.state_label)


        self.verticalLayout_3.addWidget(self.tab1_ipframe)

        self.tab1_btnframe = QFrame(self.tabWidgetPage1)
        self.tab1_btnframe.setObjectName(u"tab1_btnframe")
        self.tab1_btnframe.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.tab1_btnframe)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.on_btn = QPushButton(self.tab1_btnframe)
        self.on_btn.setObjectName(u"on_btn")
        self.on_btn.setMinimumSize(QSize(75, 25))
        self.on_btn.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_2.addWidget(self.on_btn)

        self.off_btn = QPushButton(self.tab1_btnframe)
        self.off_btn.setObjectName(u"off_btn")
        self.off_btn.setMinimumSize(QSize(75, 25))
        self.off_btn.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_2.addWidget(self.off_btn)

        self.to_hand_btn = QPushButton(self.tab1_btnframe)
        self.to_hand_btn.setObjectName(u"to_hand_btn")
        self.to_hand_btn.setMinimumSize(QSize(75, 25))
        self.to_hand_btn.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_2.addWidget(self.to_hand_btn)

        self.to_auto_btn = QPushButton(self.tab1_btnframe)
        self.to_auto_btn.setObjectName(u"to_auto_btn")
        self.to_auto_btn.setMinimumSize(QSize(75, 25))
        self.to_auto_btn.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_2.addWidget(self.to_auto_btn)

        self.on_safety_btn = QPushButton(self.tab1_btnframe)
        self.on_safety_btn.setObjectName(u"on_safety_btn")
        self.on_safety_btn.setMinimumSize(QSize(95, 25))
        self.on_safety_btn.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_2.addWidget(self.on_safety_btn)

        self.release = QPushButton(self.tab1_btnframe)
        self.release.setObjectName(u"release")
        self.release.setMinimumSize(QSize(75, 25))
        self.release.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_2.addWidget(self.release)


        self.verticalLayout_3.addWidget(self.tab1_btnframe)

        self.tab1_logframe = QFrame(self.tabWidgetPage1)
        self.tab1_logframe.setObjectName(u"tab1_logframe")
        self.tab1_logframe.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.tab1_logframe)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.logTextEdit = QPlainTextEdit(self.tab1_logframe)
        self.logTextEdit.setObjectName(u"logTextEdit")

        self.horizontalLayout_3.addWidget(self.logTextEdit)

        self.logframe_btnframe = QFrame(self.tab1_logframe)
        self.logframe_btnframe.setObjectName(u"logframe_btnframe")
        self.logframe_btnframe.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(self.logframe_btnframe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(self.logframe_btnframe)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.logframe_btnframe)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.logframe_btnframe)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.logframe_btnframe)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.logframe_btnframe)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.logframe_btnframe)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.logframe_btnframe)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.logframe_btnframe)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_10 = QPushButton(self.logframe_btnframe)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout.addWidget(self.pushButton_10)


        self.horizontalLayout_3.addWidget(self.logframe_btnframe)


        self.verticalLayout_3.addWidget(self.tab1_logframe)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_7 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tab2_socketconnectframe = QFrame(self.tabWidgetPage2)
        self.tab2_socketconnectframe.setObjectName(u"tab2_socketconnectframe")
        self.tab2_socketconnectframe.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.tab2_socketconnectframe)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.tab2_socketconnectframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(21, 21))
        self.label_3.setMidLineWidth(4)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.tab2_socketconnectframe)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(121, 20))

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addWidget(self.tab2_socketconnectframe)

        self.tab2_socketclientframe1 = QFrame(self.tabWidgetPage2)
        self.tab2_socketclientframe1.setObjectName(u"tab2_socketclientframe1")
        self.tab2_socketclientframe1.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.tab2_socketclientframe1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.socketportframe1 = QFrame(self.tab2_socketclientframe1)
        self.socketportframe1.setObjectName(u"socketportframe1")
        self.socketportframe1.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.socketportframe1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.socketportframe1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.socketclientport1 = QLineEdit(self.socketportframe1)
        self.socketclientport1.setObjectName(u"socketclientport1")
        self.socketclientport1.setMinimumSize(QSize(113, 20))
        self.socketclientport1.setMaximumSize(QSize(113, 20))

        self.horizontalLayout_4.addWidget(self.socketclientport1)

        self.socketclientconnectbtn1 = QPushButton(self.socketportframe1)
        self.socketclientconnectbtn1.setObjectName(u"socketclientconnectbtn1")

        self.horizontalLayout_4.addWidget(self.socketclientconnectbtn1)

        self.socketclientsendbtn1 = QPushButton(self.socketportframe1)
        self.socketclientsendbtn1.setObjectName(u"socketclientsendbtn1")

        self.horizontalLayout_4.addWidget(self.socketclientsendbtn1)


        self.verticalLayout_4.addWidget(self.socketportframe1)

        self.socketclient1Edit = QPlainTextEdit(self.tab2_socketclientframe1)
        self.socketclient1Edit.setObjectName(u"socketclient1Edit")

        self.verticalLayout_4.addWidget(self.socketclient1Edit)


        self.verticalLayout_7.addWidget(self.tab2_socketclientframe1)

        self.tab2_socketclientframe2 = QFrame(self.tabWidgetPage2)
        self.tab2_socketclientframe2.setObjectName(u"tab2_socketclientframe2")
        self.tab2_socketclientframe2.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.tab2_socketclientframe2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.socketportframe2 = QFrame(self.tab2_socketclientframe2)
        self.socketportframe2.setObjectName(u"socketportframe2")
        self.socketportframe2.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.socketportframe2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.socketportframe2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.socketclientport2 = QLineEdit(self.socketportframe2)
        self.socketclientport2.setObjectName(u"socketclientport2")
        self.socketclientport2.setMinimumSize(QSize(113, 20))
        self.socketclientport2.setMaximumSize(QSize(113, 20))

        self.horizontalLayout_6.addWidget(self.socketclientport2)

        self.socketclientconnectbtn2 = QPushButton(self.socketportframe2)
        self.socketclientconnectbtn2.setObjectName(u"socketclientconnectbtn2")

        self.horizontalLayout_6.addWidget(self.socketclientconnectbtn2)

        self.socketclientsendbtn2 = QPushButton(self.socketportframe2)
        self.socketclientsendbtn2.setObjectName(u"socketclientsendbtn2")

        self.horizontalLayout_6.addWidget(self.socketclientsendbtn2)


        self.verticalLayout_5.addWidget(self.socketportframe2)

        self.socketclient2Edit = QPlainTextEdit(self.tab2_socketclientframe2)
        self.socketclient2Edit.setObjectName(u"socketclient2Edit")

        self.verticalLayout_5.addWidget(self.socketclient2Edit)


        self.verticalLayout_7.addWidget(self.tab2_socketclientframe2)

        self.tab2_socketserverframe = QFrame(self.tabWidgetPage2)
        self.tab2_socketserverframe.setObjectName(u"tab2_socketserverframe")
        self.tab2_socketserverframe.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.tab2_socketserverframe)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.socketserverportframe = QFrame(self.tab2_socketserverframe)
        self.socketserverportframe.setObjectName(u"socketserverportframe")
        self.socketserverportframe.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.socketserverportframe)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.socketserverportframe)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.socketserverport = QLineEdit(self.socketserverportframe)
        self.socketserverport.setObjectName(u"socketserverport")
        self.socketserverport.setMinimumSize(QSize(113, 20))
        self.socketserverport.setMaximumSize(QSize(113, 20))

        self.horizontalLayout_7.addWidget(self.socketserverport)

        self.socketserverlistenbtn = QPushButton(self.socketserverportframe)
        self.socketserverlistenbtn.setObjectName(u"socketserverlistenbtn")

        self.horizontalLayout_7.addWidget(self.socketserverlistenbtn)

        self.socketserversendbtn = QPushButton(self.socketserverportframe)
        self.socketserversendbtn.setObjectName(u"socketserversendbtn")

        self.horizontalLayout_7.addWidget(self.socketserversendbtn)


        self.verticalLayout_6.addWidget(self.socketserverportframe)

        self.socketserverEdit = QPlainTextEdit(self.tab2_socketserverframe)
        self.socketserverEdit.setObjectName(u"socketserverEdit")

        self.verticalLayout_6.addWidget(self.socketserverEdit)


        self.verticalLayout_7.addWidget(self.tab2_socketserverframe)

        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QWidget()
        self.tabWidgetPage3.setObjectName(u"tabWidgetPage3")
        self.verticalLayout_9 = QVBoxLayout(self.tabWidgetPage3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tab3_wsconnectframe = QFrame(self.tabWidgetPage3)
        self.tab3_wsconnectframe.setObjectName(u"tab3_wsconnectframe")
        self.tab3_wsconnectframe.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.tab3_wsconnectframe)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.tab3_wsconnectframe)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.tab3_wsconnectframe)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.ws_connect_btn = QPushButton(self.tab3_wsconnectframe)
        self.ws_connect_btn.setObjectName(u"ws_connect_btn")

        self.horizontalLayout_8.addWidget(self.ws_connect_btn)


        self.verticalLayout_9.addWidget(self.tab3_wsconnectframe)

        self.tab3_wssendframe = QFrame(self.tabWidgetPage3)
        self.tab3_wssendframe.setObjectName(u"tab3_wssendframe")
        self.tab3_wssendframe.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.tab3_wssendframe)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.wssendbtn_frame = QFrame(self.tab3_wssendframe)
        self.wssendbtn_frame.setObjectName(u"wssendbtn_frame")
        self.wssendbtn_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.wssendbtn_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.wssendbtn_frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.pushButton_11 = QPushButton(self.wssendbtn_frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(121, 31))

        self.horizontalLayout_9.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.wssendbtn_frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(121, 31))

        self.horizontalLayout_9.addWidget(self.pushButton_12)

        self.ws_send_btn = QPushButton(self.wssendbtn_frame)
        self.ws_send_btn.setObjectName(u"ws_send_btn")
        self.ws_send_btn.setMinimumSize(QSize(81, 31))

        self.horizontalLayout_9.addWidget(self.ws_send_btn)


        self.verticalLayout_8.addWidget(self.wssendbtn_frame)

        self.plainTextEdit = QPlainTextEdit(self.tab3_wssendframe)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_8.addWidget(self.plainTextEdit)


        self.verticalLayout_9.addWidget(self.tab3_wssendframe)

        self.wsrecvedit = QPlainTextEdit(self.tabWidgetPage3)
        self.wsrecvedit.setObjectName(u"wsrecvedit")

        self.verticalLayout_9.addWidget(self.wsrecvedit)

        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QWidget()
        self.tabWidgetPage4.setObjectName(u"tabWidgetPage4")
        self.tabWidget.addTab(self.tabWidgetPage4, "")

        self.horizontalLayout_10.addWidget(self.tabWidget)


        self.retranslateUi(Form)
        self.connect.clicked.connect(self.logTextEdit.clear)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.IPlabel.setText(QCoreApplication.translate("Form", u"IP\uff1a", None))
        self.IPEdit.setText(QCoreApplication.translate("Form", u"192.168.101.100", None))
        self.connect.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u72b6\u6001\uff1a", None))
        self.state_label.setText(QCoreApplication.translate("Form", u"\u672a\u77e5", None))
        self.on_btn.setText(QCoreApplication.translate("Form", u"\u4e0a\u7535", None))
        self.off_btn.setText(QCoreApplication.translate("Form", u"\u4e0b\u7535", None))
        self.to_hand_btn.setText(QCoreApplication.translate("Form", u"\u624b\u52a8\u6a21\u5f0f", None))
        self.to_auto_btn.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6a21\u5f0f", None))
        self.on_safety_btn.setText(QCoreApplication.translate("Form", u"\u6551\u63f4\u6a21\u5f0f\u4e0a\u7535", None))
        self.release.setText(QCoreApplication.translate("Form", u"\u5f85\u5b9a", None))
        self.logTextEdit.setPlainText(QCoreApplication.translate("Form", u"sadasd", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), "")
        self.label_3.setText(QCoreApplication.translate("Form", u"IP:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u7aef       \u7aef\u53e3\u53f7\uff1a", None))
        self.socketclientconnectbtn1.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5", None))
        self.socketclientsendbtn1.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u7aef       \u7aef\u53e3\u53f7\uff1a", None))
        self.socketclientconnectbtn2.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5", None))
        self.socketclientsendbtn2.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u7aef       \u7aef\u53e3\u53f7\uff1a", None))
        self.socketserverlistenbtn.setText(QCoreApplication.translate("Form", u"\u76d1\u542c", None))
        self.socketserversendbtn.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), "")
        self.label_6.setText(QCoreApplication.translate("Form", u"url:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"192.168.101.100:9000", None))
        self.ws_connect_btn.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u53d1\u9001\u533a", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"\u9009\u62e9json\u6587\u4ef6", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u53d1\u9001\u533a\u5185\u5bb9", None))
        self.ws_send_btn.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), "")
    # retranslateUi

