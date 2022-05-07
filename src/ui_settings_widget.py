# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_stg_form(object):
    def setupUi(self, stg_form):
        if not stg_form.objectName():
            stg_form.setObjectName(u"stg_form")
        stg_form.resize(830, 481)
        self.verticalLayout_2 = QVBoxLayout(stg_form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 118, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget_2 = QWidget(stg_form)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cbox_clear_elements = QCheckBox(self.widget_2)
        self.cbox_clear_elements.setObjectName(u"cbox_clear_elements")
        self.cbox_clear_elements.setChecked(True)

        self.verticalLayout.addWidget(self.cbox_clear_elements)

        self.cbox_save_origins = QCheckBox(self.widget_2)
        self.cbox_save_origins.setObjectName(u"cbox_save_origins")

        self.verticalLayout.addWidget(self.cbox_save_origins)

        self.wid_save_path = QWidget(self.widget_2)
        self.wid_save_path.setObjectName(u"wid_save_path")
        self.horizontalLayout_2 = QHBoxLayout(self.wid_save_path)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.wid_save_path)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.ledit_save_path = QLineEdit(self.wid_save_path)
        self.ledit_save_path.setObjectName(u"ledit_save_path")

        self.horizontalLayout_2.addWidget(self.ledit_save_path)

        self.btn_change = QPushButton(self.wid_save_path)
        self.btn_change.setObjectName(u"btn_change")

        self.horizontalLayout_2.addWidget(self.btn_change)


        self.verticalLayout.addWidget(self.wid_save_path)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(stg_form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_ok = QPushButton(self.widget_3)
        self.btn_ok.setObjectName(u"btn_ok")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_ok, 0, 0, 1, 1)

        self.btn_cancel = QPushButton(self.widget_3)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.gridLayout.addWidget(self.btn_cancel, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 117, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(stg_form)

        QMetaObject.connectSlotsByName(stg_form)
    # setupUi

    def retranslateUi(self, stg_form):
        stg_form.setWindowTitle(QCoreApplication.translate("stg_form", u"Form", None))
        self.cbox_clear_elements.setText(QCoreApplication.translate("stg_form", u"Clear previously generated HTML elements before processing", None))
        self.cbox_save_origins.setText(QCoreApplication.translate("stg_form", u"Save original text before processing", None))
        self.label.setText(QCoreApplication.translate("stg_form", u"Saved HTML file path:", None))
        self.btn_change.setText(QCoreApplication.translate("stg_form", u"Change", None))
        self.btn_ok.setText(QCoreApplication.translate("stg_form", u"Ok", None))
        self.btn_cancel.setText(QCoreApplication.translate("stg_form", u"Cancel", None))
    # retranslateUi

