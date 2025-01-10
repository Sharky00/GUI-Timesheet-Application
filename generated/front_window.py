# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TimeshseetUIYncRSn.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_DialogTimeSheet(object):
    def setupUi(self, DialogTimeSheet):
        if not DialogTimeSheet.objectName():
            DialogTimeSheet.setObjectName(u"DialogTimeSheet")
        DialogTimeSheet.resize(415, 155)
        DialogTimeSheet.setMinimumSize(QSize(415, 155))
        DialogTimeSheet.setMaximumSize(QSize(415, 155))
        self.gridLayout = QGridLayout(DialogTimeSheet)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_pay_period_start_title = QLabel(DialogTimeSheet)
        self.label_pay_period_start_title.setObjectName(u"label_pay_period_start_title")

        self.gridLayout.addWidget(self.label_pay_period_start_title, 2, 0, 1, 1)

        self.label_file_path_title = QLabel(DialogTimeSheet)
        self.label_file_path_title.setObjectName(u"label_file_path_title")

        self.gridLayout.addWidget(self.label_file_path_title, 3, 0, 1, 1)

        self.label_emp_name_title = QLabel(DialogTimeSheet)
        self.label_emp_name_title.setObjectName(u"label_emp_name_title")

        self.gridLayout.addWidget(self.label_emp_name_title, 0, 0, 1, 1)

        self.label_sup_name_title = QLabel(DialogTimeSheet)
        self.label_sup_name_title.setObjectName(u"label_sup_name_title")

        self.gridLayout.addWidget(self.label_sup_name_title, 1, 0, 1, 1)

        self.lineEdit_sup_name_input = QLineEdit(DialogTimeSheet)
        self.lineEdit_sup_name_input.setObjectName(u"lineEdit_sup_name_input")

        self.gridLayout.addWidget(self.lineEdit_sup_name_input, 1, 1, 1, 1)

        self.dateEdit_date_input = QDateEdit(DialogTimeSheet)
        self.dateEdit_date_input.setObjectName(u"dateEdit_date_input")

        self.gridLayout.addWidget(self.dateEdit_date_input, 2, 1, 1, 1)

        self.lineEdit_emp_name_input = QLineEdit(DialogTimeSheet)
        self.lineEdit_emp_name_input.setObjectName(u"lineEdit_emp_name_input")

        self.gridLayout.addWidget(self.lineEdit_emp_name_input, 0, 1, 1, 1)

        self.pushButton_finish = QDialogButtonBox(DialogTimeSheet)
        self.pushButton_finish.setObjectName(u"pushButton_finish")
        self.pushButton_finish.setOrientation(Qt.Orientation.Horizontal)
        self.pushButton_finish.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.pushButton_finish, 4, 1, 2, 2)

        self.pushButton_path_picker = QPushButton(DialogTimeSheet)
        self.pushButton_path_picker.setObjectName(u"pushButton_path_picker")

        self.gridLayout.addWidget(self.pushButton_path_picker, 3, 1, 1, 1)

        self.label_path_title = QLabel(DialogTimeSheet)
        self.label_path_title.setObjectName(u"label_path_title")

        self.gridLayout.addWidget(self.label_path_title, 5, 0, 1, 1)


        self.retranslateUi(DialogTimeSheet)
        self.pushButton_finish.rejected.connect(DialogTimeSheet.reject)
        self.pushButton_finish.accepted.connect(DialogTimeSheet.accept)

        QMetaObject.connectSlotsByName(DialogTimeSheet)
    # setupUi

    def retranslateUi(self, DialogTimeSheet):
        DialogTimeSheet.setWindowTitle(QCoreApplication.translate("DialogTimeSheet", u"Dialog", None))
        self.label_pay_period_start_title.setText(QCoreApplication.translate("DialogTimeSheet", u"Select Pay Period Start", None))
        self.label_file_path_title.setText(QCoreApplication.translate("DialogTimeSheet", u"File Path", None))
        self.label_emp_name_title.setText(QCoreApplication.translate("DialogTimeSheet", u"Emter Employe Name", None))
        self.label_sup_name_title.setText(QCoreApplication.translate("DialogTimeSheet", u"Enter Supervisor Name", None))
        self.pushButton_path_picker.setText(QCoreApplication.translate("DialogTimeSheet", u"PushButton", None))
        self.label_path_title.setText(QCoreApplication.translate("DialogTimeSheet", u"TextLabel", None))
    # retranslateUi

