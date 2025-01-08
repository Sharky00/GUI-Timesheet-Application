import generated.front_window as front_window
import sys
from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import QDate
from datetime import datetime
from openpyxl import load_workbook


# Class to incorperate functions for  
class My_App:

    def __init__(self):
        self.generate_data()

    # Loads in data for GUI, if pre existing data exists
    def generate_data(self):
        
        wb = load_workbook('Excel Test File.xlsx',keep_vba=True, data_only=True)
        sheet = wb.active   
        cell_value = sheet['G17'].value
        
        that = cell_value
        print("Cell val here:",that)
        
        wb.save('Excel Test File.xlsx')
        date_str = "1/6/2025"
        date = QDate.fromString(date_str, "M/d/yyyy") # Convert the string to a QDate object

        self.current_date = datetime.now().strftime("%m/%d/%Y")

        ui.lineEdit_emp_name_input.setText("Sharik Mahmood")
        ui.lineEdit_sup_name_input.setText("Omar Gonzales")
        ui.lineEdit_file_path_input.setText("Testing :)")
        ui.dateEdit_date_input.setDate(date)


        # Pay period can be calculated using the calender
        # File path will be given from the user, can re-use previous location
    

    # writes desired data to excel file
    def write_to_file(self):
        wb = load_workbook('Excel Test File.xlsx')
        sheet = wb.active     

        self.current_pay_period = ui.dateEdit_date_input.text()
        self.emp_name = ui.lineEdit_emp_name_input.text()
        self.sup_name = ui.lineEdit_sup_name_input.text()   

        sheet['G11'] = self.emp_name    # Employee name
        sheet['G12'] = self.sup_name    # Supervisor name
        sheet['G16'] = self.current_pay_period # Pay Period start date
        sheet['I41'] = self.emp_name    # Employee signature
        sheet['E41'] = self.current_date # Current date
        
        wb.save('Excel Test File.xlsx')

    # Outputs user input, from the GUI window
    def Output_Gui(self):
        print("Employee name:", self.emp_name) 
        print("Supervisor name:", self.sup_name) 
        print("Pay Period Date:", ui.dateEdit_date_input.text()) 
        print("File Path:", ui.lineEdit_file_path_input.text())


if __name__ == "__main__":

    app = QApplication(sys.argv)  # Create the application instance
    Dialog = QDialog()  # Create the dialog instance
    ui = front_window.Ui_DialogTimeSheet()  # Instantiate the UI class

    ui.setupUi(Dialog)  # Set up the UI for the dialog

    my_app = My_App() # Creates instance of this class

    Dialog.show()  # Show the dialog
    ui.pushButton_finish.clicked.connect(lambda: my_app.write_to_file()) #if clicked on 'OK' we write to file

    sys.exit(app.exec())  # Run the application

