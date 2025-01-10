import generated.front_window as front_window
import sys
import shutil
import os
import json
import tkinter
from tkinter import filedialog
from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import QDate
from datetime import datetime
from openpyxl import load_workbook


# Class to incorperate functions for  
class My_App:


    # Global vars for needed cells
    EMPLOYE_NAME = "G11"
    SUPERVI_NAME = "G12"
    PAY_STA_NAME = "G16"
    PAY_END_NAME = "G17"
    E_SIGNATURE  = "I41"
    CURRENT_DATE = "E41"
    FILE_PATH   = "A101"
    PATH = " "
    
    def __init__(self):


        # Get default values
        # Def read_default_json()
        # This function checks to see if defualt.json exist. 
        # if it exist load json file into a dictionary
        # load defaults dict.get("Key", defualt="")
        self.generate_data()



    # Loads in data for GUI, if pre existing data exists
    def generate_data(self):

        # get to needed directory and saves it
        os.chdir("Timesheet Template")  
        curr_path = os.getcwd() 


        # gets file we will read from
        file_path_default = os.path.join(curr_path, "default.json") 


        # reads in .json to an object
        if not os.path.isfile(file_path_default):
            raise FileNotFoundError(f"Error: The file '{file_path_default}' does not exist.") # Check to see if file exist and if it doesnt error out. 
            exit()
        with open(file_path_default, 'r') as file:
            data = json.load(file)
        
        
        #loads Workbook
        wb = load_workbook('Excel Test File.xlsx',keep_vba=True, data_only=True)  


        # Convert the string to a QDate object
        date = QDate.fromString(data["Pay Period Start"], "M/d/yyyy") 
        self.current_date = datetime.now().strftime("%m/%d/%Y")


        # this block of code sets the texts for the GUI
        ui.dateEdit_date_input.setDate(date)
        ui.lineEdit_emp_name_input.setText(data["Employee Name"])
        ui.lineEdit_sup_name_input.setText(data["Supervisor Name"])
        if data["File Path"] == " ":
            data["File Path"] = os.path.join(os.path.expanduser("~"), "Documents")
        self.PATH = data["File Path"]
        ui.label_path_title.setText(data["File Path"])


        # Saving and closing workbook :)
        try:
            wb.save('Excel Test File.xlsx')
        except:
            print("This workbook is open, please close it")
            exit()
    


    # writes desired data to excel file
    def write_to_file(self):

        # gets path for the file we are going to write to
        myFile = 'Excel Test File.xlsx'
       
       # opens workbook to write to
        try:
            wb = load_workbook(myFile)
        except:
            print("this workbook is already open, please close it")
            wb.save(myFile)
            exit()

        
        # activates workbook
        sheet = wb.active     


        # creates JSON object and Saves all inputed GUI Items into the a JSON file
        json_obj = {
            "Employee Name": ui.lineEdit_emp_name_input.text(),
            "Supervisor Name": ui.lineEdit_sup_name_input.text(),
            "Pay Period Start":  ui.dateEdit_date_input.text(), 
            "File Path": self.PATH
        }
        with open('default.json', 'w') as outfile:
            json.dump(json_obj, outfile, sort_keys=True, indent=4)


        # Writes inputed values on to the workbook
        sheet[self.EMPLOYE_NAME] = ui.lineEdit_emp_name_input.text()    # Employee name
        sheet[self.SUPERVI_NAME] = ui.lineEdit_sup_name_input.text()   # Supervisor name
        sheet[self.PAY_STA_NAME] =  ui.dateEdit_date_input.text() # Pay Period start date
        sheet[self.E_SIGNATURE] = ui.lineEdit_emp_name_input.text()    # Employee signature
        sheet[self.CURRENT_DATE] = self.current_date # Current date
        sheet[self.FILE_PATH] = self.PATH # FilePath that we used
        

        # saves and closes the workbook :)
        try:
            wb.save(myFile)
        except:
            print("this workbook is already open, please close it")
            wb.save(myFile)
            exit()


        # Copys the completed workbook, creates a copy of it, than moves it to the desired location
        shutil.copy(myFile, self.PATH)
        cur_path = self.PATH + "\\" + myFile
        copy = self.PATH + "moving" + ".xlsx"
        new_path = self.PATH + "\\" + ui.lineEdit_emp_name_input.text() + " Timesheet  " +datetime.now().strftime("%Y-%m-%d %H.%M.%S")  + ".xlsx"
        os.rename(cur_path, copy)
        try:
            shutil.move(copy, new_path)
        except:
            print("File path error, check if the path you gave exists")

        


    # Opens file explorer and saves the file path we choose
    def set_output_path(self):

        
        tkinter.Tk().withdraw() 
        folder_path = filedialog.askdirectory()

        # sets folder path into GUI, if it is empty we default to the current working directory
        if folder_path == " ":
            folder_path = os.path.join(os.path.expanduser("~"), "Documents")


        self.PATH = folder_path
        ui.label_path_title.setText(self.PATH)
        



        
if __name__ == "__main__":

    app = QApplication(sys.argv)  # Create the application instance
    Dialog = QDialog()  # Create the dialog instance
    ui = front_window.Ui_DialogTimeSheet()  # Instantiate the UI class
    ui.setupUi(Dialog)  # Set up the UI for the dialog

    my_app = My_App() # Creates instance of this class
    Dialog.show()  # Show the dialog

    # actions if we click a button
    ui.pushButton_finish.clicked.connect(lambda: my_app.write_to_file())
    ui.pushButton_path_picker.clicked.connect(lambda: my_app.set_output_path())

    sys.exit(app.exec())  # Run the application

