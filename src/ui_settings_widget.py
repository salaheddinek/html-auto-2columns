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
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_stg_form(object):
    def setupUi(self, stg_form):
        if not stg_form.objectName():
            stg_form.setObjectName(u"stg_form")
        stg_form.resize(721, 505)
        self.verticalLayout_2 = QVBoxLayout(stg_form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(stg_form)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cbox_save_stg = QCheckBox(self.widget_2)
        self.cbox_save_stg.setObjectName(u"cbox_save_stg")
        self.cbox_save_stg.setChecked(True)
        self.cbox_save_stg.setTristate(False)

        self.verticalLayout.addWidget(self.cbox_save_stg)

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

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.sbox_indent_length = QSpinBox(self.widget_9)
        self.sbox_indent_length.setObjectName(u"sbox_indent_length")
        self.sbox_indent_length.setMinimum(0)
        self.sbox_indent_length.setMaximum(12)
        self.sbox_indent_length.setValue(4)

        self.horizontalLayout_7.addWidget(self.sbox_indent_length)

        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.widget_9)


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

        self.widget_10 = QWidget(self.widget_4)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_2 = QGridLayout(self.widget_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)

        self.ledit_r_class_tags = QLineEdit(self.widget_10)
        self.ledit_r_class_tags.setObjectName(u"ledit_r_class_tags")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_r_class_tags.sizePolicy().hasHeightForWidth())
        self.ledit_r_class_tags.setSizePolicy(sizePolicy)
        self.ledit_r_class_tags.setMinimumSize(QSize(300, 0))

        self.gridLayout_2.addWidget(self.ledit_r_class_tags, 1, 2, 1, 1)

        self.cbox_remove_attributes = QCheckBox(self.widget_10)
        self.cbox_remove_attributes.setObjectName(u"cbox_remove_attributes")

        self.gridLayout_2.addWidget(self.cbox_remove_attributes, 2, 0, 1, 1)

        self.cbox_clear_shopify_tags = QCheckBox(self.widget_10)
        self.cbox_clear_shopify_tags.setObjectName(u"cbox_clear_shopify_tags")

        self.gridLayout_2.addWidget(self.cbox_clear_shopify_tags, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget_10)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)

        self.cbox_unwrap_without_class = QCheckBox(self.widget_10)
        self.cbox_unwrap_without_class.setObjectName(u"cbox_unwrap_without_class")

        self.gridLayout_2.addWidget(self.cbox_unwrap_without_class, 1, 0, 1, 1)

        self.ledit_r_attributes_tags = QLineEdit(self.widget_10)
        self.ledit_r_attributes_tags.setObjectName(u"ledit_r_attributes_tags")
        sizePolicy.setHeightForWidth(self.ledit_r_attributes_tags.sizePolicy().hasHeightForWidth())
        self.ledit_r_attributes_tags.setSizePolicy(sizePolicy)
        self.ledit_r_attributes_tags.setMinimumSize(QSize(300, 0))

        self.gridLayout_2.addWidget(self.ledit_r_attributes_tags, 2, 2, 1, 1)

        self.ledit_no_content_tags = QLineEdit(self.widget_10)
        self.ledit_no_content_tags.setObjectName(u"ledit_no_content_tags")
        sizePolicy.setHeightForWidth(self.ledit_no_content_tags.sizePolicy().hasHeightForWidth())
        self.ledit_no_content_tags.setSizePolicy(sizePolicy)
        self.ledit_no_content_tags.setMinimumSize(QSize(300, 0))

        self.gridLayout_2.addWidget(self.ledit_no_content_tags, 3, 2, 1, 1)

        self.cbox_unwrap_no_content = QCheckBox(self.widget_10)
        self.cbox_unwrap_no_content.setObjectName(u"cbox_unwrap_no_content")

        self.gridLayout_2.addWidget(self.cbox_unwrap_no_content, 3, 0, 1, 1)

        self.label_5 = QLabel(self.widget_10)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 1, 1, 1)

        self.cbox_group_consecutive = QCheckBox(self.widget_10)
        self.cbox_group_consecutive.setObjectName(u"cbox_group_consecutive")

        self.gridLayout_2.addWidget(self.cbox_group_consecutive, 4, 0, 1, 1)

        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 4, 1, 1, 1)

        self.ledit_group_consecutive = QLineEdit(self.widget_10)
        self.ledit_group_consecutive.setObjectName(u"ledit_group_consecutive")

        self.gridLayout_2.addWidget(self.ledit_group_consecutive, 4, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_10)


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


        self.retranslateUi(stg_form)

        QMetaObject.connectSlotsByName(stg_form)
    # setupUi

    def retranslateUi(self, stg_form):
        stg_form.setWindowTitle(QCoreApplication.translate("stg_form", u"Form", None))
        self.cbox_save_stg.setText(QCoreApplication.translate("stg_form", u"Save settings for next time use", None))
        self.cbox_clear_elements.setText(QCoreApplication.translate("stg_form", u"Clear previously generated HTML elements before processing", None))
        self.cbox_save_origins.setText(QCoreApplication.translate("stg_form", u"Save original text before processing", None))
        self.label.setText(QCoreApplication.translate("stg_form", u"Saved HTML file path:", None))
        self.btn_change.setText(QCoreApplication.translate("stg_form", u"Change", None))
        self.label_6.setText(QCoreApplication.translate("stg_form", u"Indent length: ", None))
        self.label_7.setText(QCoreApplication.translate("stg_form", u"spaces", None))
        self.label_2.setText(QCoreApplication.translate("stg_form", u"Pre-processing", None))
        self.label_4.setText(QCoreApplication.translate("stg_form", u"Affected tags:", None))
        self.cbox_remove_attributes.setText(QCoreApplication.translate("stg_form", u"Remove HTML attributes (other then class)", None))
        self.cbox_clear_shopify_tags.setText(QCoreApplication.translate("stg_form", u"Remove Shopify useless <strong> tags", None))
        self.label_3.setText(QCoreApplication.translate("stg_form", u"Affected tags:", None))
        self.cbox_unwrap_without_class.setText(QCoreApplication.translate("stg_form", u"Remove tags without classes                         ", None))
        self.cbox_unwrap_no_content.setText(QCoreApplication.translate("stg_form", u"Remove tags without content                        ", None))
        self.label_5.setText(QCoreApplication.translate("stg_form", u"Affected tags:", None))
        self.cbox_group_consecutive.setText(QCoreApplication.translate("stg_form", u"Group consecutive tags", None))
        self.label_8.setText(QCoreApplication.translate("stg_form", u"Affected tags:", None))
        self.btn_ok.setText(QCoreApplication.translate("stg_form", u"Ok", None))
        self.btn_cancel.setText(QCoreApplication.translate("stg_form", u"Cancel", None))
    # retranslateUi

