# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_stg_form(object):
    def setupUi(self, stg_form):
        if not stg_form.objectName():
            stg_form.setObjectName(u"stg_form")
        stg_form.resize(863, 594)
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

        self.line = QFrame(stg_form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.widget_4 = QWidget(stg_form)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cbox_clear_shopify_tags = QCheckBox(self.widget_6)
        self.cbox_clear_shopify_tags.setObjectName(u"cbox_clear_shopify_tags")

        self.horizontalLayout_4.addWidget(self.cbox_clear_shopify_tags)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cbox_unwrap_without_class = QCheckBox(self.widget_5)
        self.cbox_unwrap_without_class.setObjectName(u"cbox_unwrap_without_class")

        self.horizontalLayout_3.addWidget(self.cbox_unwrap_without_class)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.ledit_r_class_tags = QLineEdit(self.widget_5)
        self.ledit_r_class_tags.setObjectName(u"ledit_r_class_tags")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_r_class_tags.sizePolicy().hasHeightForWidth())
        self.ledit_r_class_tags.setSizePolicy(sizePolicy)
        self.ledit_r_class_tags.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_3.addWidget(self.ledit_r_class_tags)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cbox_remove_attributes = QCheckBox(self.widget_7)
        self.cbox_remove_attributes.setObjectName(u"cbox_remove_attributes")

        self.horizontalLayout_5.addWidget(self.cbox_remove_attributes)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.ledit_r_attributes_tags = QLineEdit(self.widget_7)
        self.ledit_r_attributes_tags.setObjectName(u"ledit_r_attributes_tags")
        sizePolicy.setHeightForWidth(self.ledit_r_attributes_tags.sizePolicy().hasHeightForWidth())
        self.ledit_r_attributes_tags.setSizePolicy(sizePolicy)
        self.ledit_r_attributes_tags.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_5.addWidget(self.ledit_r_attributes_tags)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.cbox_unwrap_no_content = QCheckBox(self.widget_8)
        self.cbox_unwrap_no_content.setObjectName(u"cbox_unwrap_no_content")

        self.horizontalLayout_6.addWidget(self.cbox_unwrap_no_content)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.ledit_no_content_tags = QLineEdit(self.widget_8)
        self.ledit_no_content_tags.setObjectName(u"ledit_no_content_tags")
        sizePolicy.setHeightForWidth(self.ledit_no_content_tags.sizePolicy().hasHeightForWidth())
        self.ledit_no_content_tags.setSizePolicy(sizePolicy)
        self.ledit_no_content_tags.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_6.addWidget(self.ledit_no_content_tags)


        self.verticalLayout_3.addWidget(self.widget_8)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget = QWidget(stg_form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
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
        self.label_2.setText(QCoreApplication.translate("stg_form", u"Pre-processing", None))
        self.cbox_clear_shopify_tags.setText(QCoreApplication.translate("stg_form", u"Remove Shopify useless <strong> tags", None))
        self.cbox_unwrap_without_class.setText(QCoreApplication.translate("stg_form", u"Remove tags without classes                         ", None))
        self.label_3.setText(QCoreApplication.translate("stg_form", u"Affected tags:", None))
        self.cbox_remove_attributes.setText(QCoreApplication.translate("stg_form", u"Remove HTML attributes (other then class)", None))
        self.label_4.setText(QCoreApplication.translate("stg_form", u"Affected tags:", None))
        self.cbox_unwrap_no_content.setText(QCoreApplication.translate("stg_form", u"Remove tags without content                        ", None))
        self.label_5.setText(QCoreApplication.translate("stg_form", u"Affected tags:", None))
        self.btn_ok.setText(QCoreApplication.translate("stg_form", u"Ok", None))
        self.btn_cancel.setText(QCoreApplication.translate("stg_form", u"Cancel", None))
    # retranslateUi

