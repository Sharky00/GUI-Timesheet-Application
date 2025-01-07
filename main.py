# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup0iTaXAn.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import QApplication, QDateEdit, QDialog, QDialogButtonBox, QGridLayout, QLabel, QLineEdit, QWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Timesheet")

        #sets size of the GUI window
        Dialog.resize(415, 155)
        Dialog.setMinimumSize(QSize(415, 155))
        Dialog.setMaximumSize(QSize(415, 155))

        #Istantiates self.gridLayout
        self.gridLayout = QGridLayout(Dialog)

        #Formats Employee name input box
        self.emp_name_2 = QLineEdit(Dialog)
        self.gridLayout.addWidget(self.emp_name_2, 0, 2, 1, 1)

        #Formats Employee name text box
        self.emp_name = QLabel(Dialog)
        self.gridLayout.addWidget(self.emp_name, 0, 0, 1, 1)

        #Formats Employee pay period text box
        self.pay_period_start = QLabel(Dialog)
        self.gridLayout.addWidget(self.pay_period_start, 2, 0, 1, 1)

        #Formats Employee pay period date input box
        self.dateEdit = QDateEdit(Dialog)
        self.gridLayout.addWidget(self.dateEdit, 2, 2, 1, 1)

        #Formats Employee File Path Text
        self.file_path = QLabel(Dialog)
        self.gridLayout.addWidget(self.file_path, 3, 0, 1, 1)

        #Formats employee file path input box
        self.file_path_2 = QLineEdit(Dialog)
        self.gridLayout.addWidget(self.file_path_2, 3, 2, 1, 1)

        #Formats Supervisor name text box
        self.sup_name = QLabel(Dialog)
        self.gridLayout.addWidget(self.sup_name, 1, 0, 1, 1)

        #Formats Supervisor name input box
        self.sup_name_2 = QLineEdit(Dialog)
        self.gridLayout.addWidget(self.sup_name_2, 1, 2, 1, 1)

        #creates and formats 'finish' buttons
        self.finish_button = QDialogButtonBox(Dialog)
        self.finish_button.setOrientation(Qt.Orientation.Horizontal)
        self.finish_button.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.gridLayout.addWidget(self.finish_button, 4, 2, 2, 2)

        #function call, grabs 
        self.retranslateUi(Dialog)
        self.finish_button.accepted.connect(self.on_finish_button_clicked)
        self.finish_button.rejected.connect(Dialog.reject)


        QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):

        #Sets the names of the Textboxes in the GUI
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Timesheet", None))
        self.emp_name.setText(QCoreApplication.translate("Dialog", u"Enter Employe Name", None))
        self.sup_name.setText(QCoreApplication.translate("Dialog", u"Enter Supervisor Name", None))
        self.pay_period_start.setText(QCoreApplication.translate("Dialog", u"Select Pay Period Start", None))
        self.file_path.setText(QCoreApplication.translate("Dialog", u"File Path", None))

        employee_name = self.emp_name_2.text()
    
    def on_finish_button_clicked(self):
        employee_name = self.emp_name_2.text()
        supervisor_name = self.sup_name_2.text()
        file_path = self.file_path_2.text()
        date = self.dateEdit.text()

        print(f"Employee Name: {employee_name}")
        print(f"supervisor_name: {supervisor_name}")
        print(f"date: {date}")
        print(f"file_path: {file_path}")



if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application instance
    Dialog = QDialog()  # Create the dialog instance
    ui = Ui_Dialog()  # Instantiate the UI class
    ui.setupUi(Dialog)  # Set up the UI for the dialog
    Dialog.show()  # Show the dialog
    sys.exit(app.exec())  # Run the application