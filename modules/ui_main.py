# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWcODQG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 960)
        MainWindow.setMinimumSize(QSize(1440, 960))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        # font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(self.styleSheet)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        # font1.setWeight(8)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        # font2.setWeight(50)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        # font3.setWeight(50)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(45)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.btn_start = QPushButton(self.home)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy3)
        self.btn_start.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_12.addWidget(self.btn_start)

        self.btn_start_now = QPushButton(self.home)
        self.btn_start_now.setObjectName(u"btn_start_now")
        self.btn_start_now.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_12.addWidget(self.btn_start_now)

        self.btn_stop = QPushButton(self.home)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_12.addWidget(self.btn_stop)

        self.btn_close_all = QPushButton(self.home)
        self.btn_close_all.setObjectName(u"btn_close_all")
        self.btn_close_all.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_12.addWidget(self.btn_close_all)


        self.gridLayout.addLayout(self.horizontalLayout_12, 3, 0, 1, 2)

        self.chart_build = QWidget(self.home)
        self.chart_build.setObjectName(u"chart_build")
        self.chart_build.setMinimumSize(QSize(1000, 620))

        self.gridLayout.addWidget(self.chart_build, 0, 0, 1, 1)

        self.output_positions = QLabel(self.home)
        self.output_positions.setObjectName(u"output_positions")
        self.output_positions.setMinimumSize(QSize(0, 100))
        self.output_positions.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.output_positions.setMargin(10)

        self.gridLayout.addWidget(self.output_positions, 1, 0, 1, 2)

        self.command_status = QLabel(self.home)
        self.command_status.setObjectName(u"command_status")

        self.gridLayout.addWidget(self.command_status, 2, 0, 1, 1)

        self.info_label = QLabel(self.home)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.info_label.setScaledContents(False)
        self.info_label.setMargin(10)

        self.gridLayout.addWidget(self.info_label, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.label_2 = QLabel(self.widgets)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 20, 341, 29))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.widgets)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 70, 131, 21))
        self.label_4 = QLabel(self.widgets)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 70, 67, 17))
        self.label_5 = QLabel(self.widgets)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 70, 67, 17))
        self.btn_save_params = QPushButton(self.widgets)
        self.btn_save_params.setObjectName(u"btn_save_params")
        self.btn_save_params.setGeometry(QRect(610, 360, 261, 41))
        self.btn_save_params.setMinimumSize(QSize(0, 40))
        self.btn_save_params.setFont(font)
        self.btn_save_params.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayoutWidget = QWidget(self.widgets)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 100, 91, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Binance_2 = QLabel(self.verticalLayoutWidget)
        self.Binance_2.setObjectName(u"Binance_2")

        self.verticalLayout.addWidget(self.Binance_2)

        self.Bybit_2 = QLabel(self.verticalLayoutWidget)
        self.Bybit_2.setObjectName(u"Bybit_2")

        self.verticalLayout.addWidget(self.Bybit_2)

        self.Huobi_2 = QLabel(self.verticalLayoutWidget)
        self.Huobi_2.setObjectName(u"Huobi_2")

        self.verticalLayout.addWidget(self.Huobi_2)

        self.Kucoin_2 = QLabel(self.verticalLayoutWidget)
        self.Kucoin_2.setObjectName(u"Kucoin_2")

        self.verticalLayout.addWidget(self.Kucoin_2)

        self.verticalLayoutWidget_2 = QWidget(self.widgets)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(190, 100, 101, 311))
        self.verticalLayout_16 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.binance_symbol_1 = QLineEdit(self.verticalLayoutWidget_2)
        self.binance_symbol_1.setObjectName(u"binance_symbol_1")

        self.verticalLayout_16.addWidget(self.binance_symbol_1)

        self.binance_symbol_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.binance_symbol_2.setObjectName(u"binance_symbol_2")

        self.verticalLayout_16.addWidget(self.binance_symbol_2)

        self.bybit_symbol_1 = QLineEdit(self.verticalLayoutWidget_2)
        self.bybit_symbol_1.setObjectName(u"bybit_symbol_1")

        self.verticalLayout_16.addWidget(self.bybit_symbol_1)

        self.bybit_symbol_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.bybit_symbol_2.setObjectName(u"bybit_symbol_2")

        self.verticalLayout_16.addWidget(self.bybit_symbol_2)

        self.huobi_symbol_1 = QLineEdit(self.verticalLayoutWidget_2)
        self.huobi_symbol_1.setObjectName(u"huobi_symbol_1")

        self.verticalLayout_16.addWidget(self.huobi_symbol_1)

        self.huobi_symbol_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.huobi_symbol_2.setObjectName(u"huobi_symbol_2")

        self.verticalLayout_16.addWidget(self.huobi_symbol_2)

        self.kucoin_symbol_1 = QLineEdit(self.verticalLayoutWidget_2)
        self.kucoin_symbol_1.setObjectName(u"kucoin_symbol_1")

        self.verticalLayout_16.addWidget(self.kucoin_symbol_1)

        self.kucoin_symbol_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.kucoin_symbol_2.setObjectName(u"kucoin_symbol_2")

        self.verticalLayout_16.addWidget(self.kucoin_symbol_2)

        self.verticalLayoutWidget_3 = QWidget(self.widgets)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(100, 100, 91, 311))
        self.verticalLayout_17 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pair_1_1 = QLabel(self.verticalLayoutWidget_3)
        self.pair_1_1.setObjectName(u"pair_1_1")

        self.verticalLayout_17.addWidget(self.pair_1_1)

        self.pair_1_2 = QLabel(self.verticalLayoutWidget_3)
        self.pair_1_2.setObjectName(u"pair_1_2")

        self.verticalLayout_17.addWidget(self.pair_1_2)

        self.pair_1_4 = QLabel(self.verticalLayoutWidget_3)
        self.pair_1_4.setObjectName(u"pair_1_4")

        self.verticalLayout_17.addWidget(self.pair_1_4)

        self.pair_1_3 = QLabel(self.verticalLayoutWidget_3)
        self.pair_1_3.setObjectName(u"pair_1_3")

        self.verticalLayout_17.addWidget(self.pair_1_3)

        self.pair_1_5 = QLabel(self.verticalLayoutWidget_3)
        self.pair_1_5.setObjectName(u"pair_1_5")

        self.verticalLayout_17.addWidget(self.pair_1_5)

        self.pair_1_6 = QLabel(self.verticalLayoutWidget_3)
        self.pair_1_6.setObjectName(u"pair_1_6")

        self.verticalLayout_17.addWidget(self.pair_1_6)

        self.pair_1_7 = QLabel(self.verticalLayoutWidget_3)
        self.pair_1_7.setObjectName(u"pair_1_7")

        self.verticalLayout_17.addWidget(self.pair_1_7)

        self.pair_1_8 = QLabel(self.verticalLayoutWidget_3)
        self.pair_1_8.setObjectName(u"pair_1_8")

        self.verticalLayout_17.addWidget(self.pair_1_8)

        self.verticalLayoutWidget_4 = QWidget(self.widgets)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(300, 100, 101, 311))
        self.verticalLayout_18 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.binance_qty_1 = QLineEdit(self.verticalLayoutWidget_4)
        self.binance_qty_1.setObjectName(u"binance_qty_1")

        self.verticalLayout_18.addWidget(self.binance_qty_1)

        self.binance_qty_2 = QLineEdit(self.verticalLayoutWidget_4)
        self.binance_qty_2.setObjectName(u"binance_qty_2")

        self.verticalLayout_18.addWidget(self.binance_qty_2)

        self.bybit_qty_1 = QLineEdit(self.verticalLayoutWidget_4)
        self.bybit_qty_1.setObjectName(u"bybit_qty_1")

        self.verticalLayout_18.addWidget(self.bybit_qty_1)

        self.bybit_qty_2 = QLineEdit(self.verticalLayoutWidget_4)
        self.bybit_qty_2.setObjectName(u"bybit_qty_2")

        self.verticalLayout_18.addWidget(self.bybit_qty_2)

        self.huobi_qty_1 = QLineEdit(self.verticalLayoutWidget_4)
        self.huobi_qty_1.setObjectName(u"huobi_qty_1")

        self.verticalLayout_18.addWidget(self.huobi_qty_1)

        self.huobi_qty_2 = QLineEdit(self.verticalLayoutWidget_4)
        self.huobi_qty_2.setObjectName(u"huobi_qty_2")

        self.verticalLayout_18.addWidget(self.huobi_qty_2)

        self.kucoin_qty_1 = QLineEdit(self.verticalLayoutWidget_4)
        self.kucoin_qty_1.setObjectName(u"kucoin_qty_1")

        self.verticalLayout_18.addWidget(self.kucoin_qty_1)

        self.kucoin_qty_2 = QLineEdit(self.verticalLayoutWidget_4)
        self.kucoin_qty_2.setObjectName(u"kucoin_qty_2")

        self.verticalLayout_18.addWidget(self.kucoin_qty_2)

        self.verticalLayoutWidget_5 = QWidget(self.widgets)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(410, 100, 111, 308))
        self.verticalLayout_19 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.binance_side_1 = QComboBox(self.verticalLayoutWidget_5)
        self.binance_side_1.addItem("")
        self.binance_side_1.addItem("")
        self.binance_side_1.setObjectName(u"binance_side_1")
        self.binance_side_1.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.binance_side_1)

        self.binance_side_2 = QComboBox(self.verticalLayoutWidget_5)
        self.binance_side_2.addItem("")
        self.binance_side_2.addItem("")
        self.binance_side_2.setObjectName(u"binance_side_2")
        self.binance_side_2.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.binance_side_2)

        self.bybit_side_1 = QComboBox(self.verticalLayoutWidget_5)
        self.bybit_side_1.addItem("")
        self.bybit_side_1.addItem("")
        self.bybit_side_1.setObjectName(u"bybit_side_1")
        self.bybit_side_1.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.bybit_side_1)

        self.bybit_side_2 = QComboBox(self.verticalLayoutWidget_5)
        self.bybit_side_2.addItem("")
        self.bybit_side_2.addItem("")
        self.bybit_side_2.setObjectName(u"bybit_side_2")
        self.bybit_side_2.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.bybit_side_2)

        self.huobi_side_1 = QComboBox(self.verticalLayoutWidget_5)
        self.huobi_side_1.addItem("")
        self.huobi_side_1.addItem("")
        self.huobi_side_1.setObjectName(u"huobi_side_1")
        self.huobi_side_1.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.huobi_side_1)

        self.huobi_side_2 = QComboBox(self.verticalLayoutWidget_5)
        self.huobi_side_2.addItem("")
        self.huobi_side_2.addItem("")
        self.huobi_side_2.setObjectName(u"huobi_side_2")
        self.huobi_side_2.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.huobi_side_2)

        self.kucoin_side_1 = QComboBox(self.verticalLayoutWidget_5)
        self.kucoin_side_1.addItem("")
        self.kucoin_side_1.addItem("")
        self.kucoin_side_1.setObjectName(u"kucoin_side_1")
        self.kucoin_side_1.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.kucoin_side_1)

        self.kucoin_side_2 = QComboBox(self.verticalLayoutWidget_5)
        self.kucoin_side_2.addItem("")
        self.kucoin_side_2.addItem("")
        self.kucoin_side_2.setObjectName(u"kucoin_side_2")
        self.kucoin_side_2.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.kucoin_side_2)

        self.horizontalLayoutWidget = QWidget(self.widgets)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(560, 100, 361, 35))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_time_work = QLabel(self.horizontalLayoutWidget)
        self.label_time_work.setObjectName(u"label_time_work")

        self.horizontalLayout_6.addWidget(self.label_time_work)

        self.time_work = QComboBox(self.horizontalLayoutWidget)
        self.time_work.addItem("")
        self.time_work.addItem("")
        self.time_work.addItem("")
        self.time_work.setObjectName(u"time_work")
        self.time_work.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.time_work)

        self.horizontalLayoutWidget_2 = QWidget(self.widgets)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(560, 140, 361, 35))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_time_update = QLabel(self.horizontalLayoutWidget_2)
        self.label_time_update.setObjectName(u"label_time_update")

        self.horizontalLayout_7.addWidget(self.label_time_update)

        self.time_update = QComboBox(self.horizontalLayoutWidget_2)
        self.time_update.addItem("")
        self.time_update.addItem("")
        self.time_update.addItem("")
        self.time_update.addItem("")
        self.time_update.addItem("")
        self.time_update.setObjectName(u"time_update")
        self.time_update.setStyleSheet(u"selection-color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.time_update)

        self.horizontalLayoutWidget_3 = QWidget(self.widgets)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(560, 180, 361, 35))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_distance_num = QLabel(self.horizontalLayoutWidget_3)
        self.label_distance_num.setObjectName(u"label_distance_num")

        self.horizontalLayout_8.addWidget(self.label_distance_num)

        self.distance_num = QLineEdit(self.horizontalLayoutWidget_3)
        self.distance_num.setObjectName(u"distance_num")

        self.horizontalLayout_8.addWidget(self.distance_num)

        self.horizontalLayoutWidget_4 = QWidget(self.widgets)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(560, 220, 361, 35))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_coefficient = QLabel(self.horizontalLayoutWidget_4)
        self.label_coefficient.setObjectName(u"label_coefficient")

        self.horizontalLayout_9.addWidget(self.label_coefficient)

        self.coefficient = QLineEdit(self.horizontalLayoutWidget_4)
        self.coefficient.setObjectName(u"coefficient")

        self.horizontalLayout_9.addWidget(self.coefficient)

        self.horizontalLayoutWidget_5 = QWidget(self.widgets)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(560, 260, 361, 35))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_profit = QLabel(self.horizontalLayoutWidget_5)
        self.label_profit.setObjectName(u"label_profit")

        self.horizontalLayout_10.addWidget(self.label_profit)

        self.profit = QLineEdit(self.horizontalLayoutWidget_5)
        self.profit.setObjectName(u"profit")

        self.horizontalLayout_10.addWidget(self.profit)

        self.horizontalLayoutWidget_6 = QWidget(self.widgets)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(560, 300, 361, 35))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_loss = QLabel(self.horizontalLayoutWidget_6)
        self.label_loss.setObjectName(u"label_loss")

        self.horizontalLayout_11.addWidget(self.label_loss)

        self.loss = QLineEdit(self.horizontalLayoutWidget_6)
        self.loss.setObjectName(u"loss")

        self.horizontalLayout_11.addWidget(self.loss)

        self.stackedWidget.addWidget(self.widgets)
        self.connection_page = QWidget()
        self.connection_page.setObjectName(u"connection_page")
        self.label = QLabel(self.connection_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 10, 329, 29))
        self.label.setFont(font)
        self.save_keys = QPushButton(self.connection_page)
        self.save_keys.setObjectName(u"save_keys")
        self.save_keys.setGeometry(QRect(100, 370, 261, 51))
        self.save_keys.setFont(font)
        self.save_keys.setCursor(QCursor(Qt.PointingHandCursor))
        self.layoutWidget = QWidget(self.connection_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 70, 891, 282))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(20)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 5)
        self.api_key = QLabel(self.layoutWidget)
        self.api_key.setObjectName(u"api_key")

        self.gridLayout_3.addWidget(self.api_key, 0, 1, 1, 1)

        self.api_secret = QLabel(self.layoutWidget)
        self.api_secret.setObjectName(u"api_secret")
        self.api_secret.setCursor(QCursor(Qt.ArrowCursor))
        self.api_secret.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.api_secret, 0, 2, 1, 1)

        self.Binance = QLabel(self.layoutWidget)
        self.Binance.setObjectName(u"Binance")

        self.gridLayout_3.addWidget(self.Binance, 1, 0, 1, 1)

        self.binance_key = QLineEdit(self.layoutWidget)
        self.binance_key.setObjectName(u"binance_key")
        self.binance_key.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_3.addWidget(self.binance_key, 1, 1, 1, 1)

        self.binance_secret = QLineEdit(self.layoutWidget)
        self.binance_secret.setObjectName(u"binance_secret")
        self.binance_secret.setCursor(QCursor(Qt.ArrowCursor))
        self.binance_secret.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.binance_secret, 1, 2, 1, 1)

        self.Bybit = QLabel(self.layoutWidget)
        self.Bybit.setObjectName(u"Bybit")

        self.gridLayout_3.addWidget(self.Bybit, 2, 0, 1, 1)

        self.bybit_key = QLineEdit(self.layoutWidget)
        self.bybit_key.setObjectName(u"bybit_key")
        self.bybit_key.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_3.addWidget(self.bybit_key, 2, 1, 1, 1)

        self.bybit_secret = QLineEdit(self.layoutWidget)
        self.bybit_secret.setObjectName(u"bybit_secret")
        self.bybit_secret.setCursor(QCursor(Qt.ArrowCursor))
        self.bybit_secret.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.bybit_secret, 2, 2, 1, 1)

        self.Huobi = QLabel(self.layoutWidget)
        self.Huobi.setObjectName(u"Huobi")

        self.gridLayout_3.addWidget(self.Huobi, 3, 0, 1, 1)

        self.huobi_key = QLineEdit(self.layoutWidget)
        self.huobi_key.setObjectName(u"huobi_key")
        self.huobi_key.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_3.addWidget(self.huobi_key, 3, 1, 1, 1)

        self.huobi_secret = QLineEdit(self.layoutWidget)
        self.huobi_secret.setObjectName(u"huobi_secret")
        self.huobi_secret.setCursor(QCursor(Qt.ArrowCursor))
        self.huobi_secret.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.huobi_secret, 3, 2, 1, 1)

        self.Kucoin = QLabel(self.layoutWidget)
        self.Kucoin.setObjectName(u"Kucoin")

        self.gridLayout_3.addWidget(self.Kucoin, 4, 0, 1, 1)

        self.kucoin_key = QLineEdit(self.layoutWidget)
        self.kucoin_key.setObjectName(u"kucoin_key")
        self.kucoin_key.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_3.addWidget(self.kucoin_key, 4, 1, 1, 1)

        self.kucoin_secret = QLineEdit(self.layoutWidget)
        self.kucoin_secret.setObjectName(u"kucoin_secret")
        self.kucoin_secret.setCursor(QCursor(Qt.ArrowCursor))
        self.kucoin_secret.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.kucoin_secret, 4, 2, 1, 1)

        self.kucoin_uid = QLineEdit(self.layoutWidget)
        self.kucoin_uid.setObjectName(u"kucoin_uid")
        self.kucoin_uid.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_3.addWidget(self.kucoin_uid, 5, 1, 1, 1)

        self.kucoin_passphrase = QLineEdit(self.layoutWidget)
        self.kucoin_passphrase.setObjectName(u"kucoin_passphrase")
        self.kucoin_passphrase.setCursor(QCursor(Qt.ArrowCursor))
        self.kucoin_passphrase.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.kucoin_passphrase, 5, 2, 1, 1)

        self.stackedWidget.addWidget(self.connection_page)
        self.balances = QWidget()
        self.balances.setObjectName(u"balances")
        self.gridLayout_4 = QGridLayout(self.balances)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.balances)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.chart_build_2 = QWidget(self.balances)
        self.chart_build_2.setObjectName(u"chart_build_2")
        self.chart_build_2.setMinimumSize(QSize(0, 600))
        self.chart_build_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.chart_build_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.balances)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setBold(False)
        font4.setItalic(False)
        # font4.setWeight(50)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.gridLayout_2.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Futures trade", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"test app", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"API conect", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Futures order", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Some page</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">with some text</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Futures trade (test)", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u0410\u0420\u0422 \u041f\u041e \u0412\u0420\u0415\u041c\u0415\u041d\u0418", None))
        self.btn_start_now.setText(QCoreApplication.translate("MainWindow", u"C\u0422\u0410\u0420\u0422 \u0421\u0415\u0419\u0427\u0410\u0421", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u041e\u041f", None))
        self.btn_close_all.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u041a\u0420\u042b\u0422\u042c \u0412\u0421\u0415", None))
        self.output_positions.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TextLabel<br>TextLabel<br>TextLabel<br>TextLabel</p></body></html>", None))
        self.command_status.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0433\u043e\u0442\u043e\u0432\u0430", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432 - | </span><span style=\" font-size:12pt; font-weight:600;\">80</span><span style=\" font-size:12pt;\"> |</span></p><p><span style=\" font-size:12pt;\">\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u044f (\u0438\u0437 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432) - 20</span></p><p>\u041e\u0431\u0449\u0438\u0435 \u0441\u0443\u043c\u043c\u044b \u043c\u0435\u043d\u044f\u044e\u0442\u0441\u044f \u043f\u0440\u0438 \u0441\u043e\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u0438 <br/>\u0443\u0441\u043b\u043e\u0432\u0438\u0439 ( \u043c\u043e\u0434\u0443\u043b\u044c \u043e\u0431\u0449\u0435\u0439 \u0441\u0443\u043c\u043c\u044b \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432<br/>\u0431\u043e\u043b\u044c\u0448\u0435 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438) \u0438 \u0435\u0441\u043b\u0438 \u043d\u0435\u0442<br/>\u043e\u0442\u043a"
                        "\u0440\u044b\u0442\u044b\u0445 \u043f\u043e\u0437\u0438\u0446\u0438\u0439</p><p><span style=\" font-size:12pt;\">\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 #1 Binance: -3</span><br/><span style=\" font-size:8pt;\">\u043e\u0431\u044a\u0435\u043c \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u043c \u043d\u0430 3, \u0441\u0442\u043e\u0440\u043e\u043d\u0430 SELL</span></p><p><span style=\" font-size:12pt;\">\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 #1 Kucoin: -3</span><br/><span style=\" font-size:8pt;\">\u043e\u0431\u044a\u0435\u043c \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u043c \u043d\u0430 3, \u0441\u0442\u043e\u0440\u043e\u043d\u0430 SELL</span></p><p><span style=\" font-size:12pt;\">\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 #1 Huobi: -3</span><br/><span style=\" font-size:8pt;\">\u043e\u0431\u044a\u0435\u043c \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u043c \u043d\u0430 3, \u0441\u0442\u043e\u0440\u043e"
                        "\u043d\u0430 SELL</span></p><p><span style=\" font-size:12pt;\">\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 #1 Bybit: -3</span><br/><span style=\" font-size:8pt;\">\u043e\u0431\u044a\u0435\u043c \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u043c \u043d\u0430 3, \u0441\u0442\u043e\u0440\u043e\u043d\u0430 SELL</span></p><p><span style=\" font-size:12pt;\">\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 #2 Binance: -3</span><br/><span style=\" font-size:8pt;\">\u043e\u0431\u044a\u0435\u043c \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u043c \u043d\u0430 3, \u0441\u0442\u043e\u0440\u043e\u043d\u0430 SELL</span></p><p><span style=\" font-size:12pt;\">\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 #2 Kucoin: -3</span><br/><span style=\" font-size:8pt;\">\u043e\u0431\u044a\u0435\u043c \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u043c \u043d\u0430 3, \u0441\u0442\u043e\u0440\u043e\u043d\u0430 SELL</span></p><p><span style=\""
                        " font-size:12pt;\">\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 #2 Huobi: -3</span><br/><span style=\" font-size:8pt;\">\u043e\u0431\u044a\u0435\u043c \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u043c \u043d\u0430 3, \u0441\u0442\u043e\u0440\u043e\u043d\u0430 SELL</span></p><p><span style=\" font-size:12pt;\">\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 #2 Bybit: -3</span><br/><span style=\" font-size:8pt;\">\u043e\u0431\u044a\u0435\u043c \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u043c \u043d\u0430 3, \u0441\u0442\u043e\u0440\u043e\u043d\u0430 SELL</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">\u0412\u0432\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0442\u0438\u043a\u0435\u0440 (BTC, ETH ...)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0431\u044a\u0435\u043c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u043e\u0440\u043e\u043d\u0430", None))
        self.btn_save_params.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u0432\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.Binance_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">Binance</span></p></body></html>", None))
        self.Bybit_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">Bybit</span></p></body></html>", None))
        self.Huobi_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">Huobi</span></p></body></html>", None))
        self.Kucoin_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">Kucoin</span></p></body></html>", None))
        self.pair_1_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u0430\u0440\u0430 \u21161</p></body></html>", None))
        self.pair_1_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u0430\u0440\u0430 \u21162</p></body></html>", None))
        self.pair_1_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u0430\u0440\u0430 \u21161</p></body></html>", None))
        self.pair_1_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u0430\u0440\u0430 \u21162</p></body></html>", None))
        self.pair_1_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u0430\u0440\u0430 \u21161</p></body></html>", None))
        self.pair_1_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u0430\u0440\u0430 \u21162</p></body></html>", None))
        self.pair_1_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u0430\u0440\u0430 \u21161</p></body></html>", None))
        self.pair_1_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u0430\u0440\u0430 \u21162</p></body></html>", None))
        self.binance_side_1.setItemText(0, QCoreApplication.translate("MainWindow", u"BUY", None))
        self.binance_side_1.setItemText(1, QCoreApplication.translate("MainWindow", u"SELL", None))

        self.binance_side_1.setCurrentText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.binance_side_2.setItemText(0, QCoreApplication.translate("MainWindow", u"BUY", None))
        self.binance_side_2.setItemText(1, QCoreApplication.translate("MainWindow", u"SELL", None))

        self.binance_side_2.setCurrentText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.bybit_side_1.setItemText(0, QCoreApplication.translate("MainWindow", u"BUY", None))
        self.bybit_side_1.setItemText(1, QCoreApplication.translate("MainWindow", u"SELL", None))

        self.bybit_side_1.setCurrentText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.bybit_side_2.setItemText(0, QCoreApplication.translate("MainWindow", u"BUY", None))
        self.bybit_side_2.setItemText(1, QCoreApplication.translate("MainWindow", u"SELL", None))

        self.bybit_side_2.setCurrentText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.huobi_side_1.setItemText(0, QCoreApplication.translate("MainWindow", u"BUY", None))
        self.huobi_side_1.setItemText(1, QCoreApplication.translate("MainWindow", u"SELL", None))

        self.huobi_side_1.setCurrentText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.huobi_side_2.setItemText(0, QCoreApplication.translate("MainWindow", u"BUY", None))
        self.huobi_side_2.setItemText(1, QCoreApplication.translate("MainWindow", u"SELL", None))

        self.huobi_side_2.setCurrentText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.kucoin_side_1.setItemText(0, QCoreApplication.translate("MainWindow", u"BUY", None))
        self.kucoin_side_1.setItemText(1, QCoreApplication.translate("MainWindow", u"SELL", None))

        self.kucoin_side_1.setCurrentText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.kucoin_side_2.setItemText(0, QCoreApplication.translate("MainWindow", u"BUY", None))
        self.kucoin_side_2.setItemText(1, QCoreApplication.translate("MainWindow", u"SELL", None))

        self.kucoin_side_2.setCurrentText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.label_time_work.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0444\u0440\u0435\u0439\u043c, \u043c\u0438\u043d", None))
        self.time_work.setItemText(0, QCoreApplication.translate("MainWindow", u"15", None))
        self.time_work.setItemText(1, QCoreApplication.translate("MainWindow", u"30", None))
        self.time_work.setItemText(2, QCoreApplication.translate("MainWindow", u"60", None))

        self.time_work.setCurrentText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_time_update.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0439, \u0441\u0435\u043a", None))
        self.time_update.setItemText(0, QCoreApplication.translate("MainWindow", u"0.5", None))
        self.time_update.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.time_update.setItemText(2, QCoreApplication.translate("MainWindow", u"1.5", None))
        self.time_update.setItemText(3, QCoreApplication.translate("MainWindow", u"2", None))
        self.time_update.setItemText(4, QCoreApplication.translate("MainWindow", u"3", None))

        self.time_update.setCurrentText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_distance_num.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u044f                         ", None))
        self.label_coefficient.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0438\u0446\u0438\u0435\u043d\u0442                      ", None))
        self.label_profit.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u0442                              ", None))
        self.label_loss.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u044b\u0442\u043e\u043a                              ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">API \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0431\u0438\u0440\u0436</span></p></body></html>", None))
        self.save_keys.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043b\u044e\u0447\u0438", None))
        self.api_key.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">API KEY</p></body></html>", None))
        self.api_secret.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">API SECRET</p><p align=\"center\"><br/></p></body></html>", None))
        self.Binance.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">Binance</span></p></body></html>", None))
        self.binance_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input api key here", None))
        self.binance_secret.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input api secret here", None))
        self.Bybit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">Bybit</span></p></body></html>", None))
        self.bybit_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input api key here", None))
        self.bybit_secret.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input api secret here", None))
        self.Huobi.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">Huobi</span></p></body></html>", None))
        self.huobi_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input api key here", None))
        self.huobi_secret.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input api secret here", None))
        self.Kucoin.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">Kucoin</span></p></body></html>", None))
        self.kucoin_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input api key here", None))
        self.kucoin_secret.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input api secret here", None))
        self.kucoin_uid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input uid from Kucoin", None))
        self.kucoin_passphrase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input api passphrase from Kucoin", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">\u0411\u0430\u043b\u0430\u043d\u0441\u044b \u0431\u0438\u0440\u0436</span></p></body></html>", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"test app", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

