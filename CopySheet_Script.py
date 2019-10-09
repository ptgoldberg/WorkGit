import xlsxwriter
import csv
from win32com.client import Dispatch

#dialect here refers to how csv will process your MID file, in this case, it's comma delimited
csv.register_dialect('myDialect',
delimiter=',',
quoting=csv.QUOTE_NONE,
skipinitialspace=True
)

#creates empty array/list as MID_list, then the With function opens the csv file, iterates through, strips all spaces, commas, etc and appends it to MID_list, each MID is saved as an integer, which isn't entirely necessary
mid_list = []

with open('curr_MID.csv') as csv_file:
    reader = csv.reader(csv_file, dialect='myDialect')
    for row in reader:
        mid_list.append(int(row[0].strip()))

#name this path to where ever your template file is saved
sourcePath = "C:\\Users\\paugoldb\\Desktop\\Script Stuff\\PythonTemp\\MAIN_TEMPLATE.xlsx"

#creates a command to open an excel document
x1 = Dispatch("Excel.Application")
#this setting just changes whether or not the excel documents pop up on your screen, I leave it off as it basically shuts your ability to use your computer while this script runs
#x1.Visible = True

#opens the template file as WB1 and each worksheet as ws1 and ws2
wb1 = x1.Workbooks.Open(Filename=sourcePath)
ws1 = wb1.Worksheets(1)
ws2 = wb1.Worksheets(2)

#iterates through MID_list, for each MID, create a new excel file named "2019_10_05_*CURRENT MID*_Sherlock_Errors.xlsx"
for i in mid_list :
    workbook = xlsxwriter.Workbook("2019_10_05_" + str(i) + "_Sherlock_Errors.xlsx")
    workbook.close()

    #opens the file that was created, copies ws1 and ws2 from the template file to the created file and saves the created file
    currPath = "C:\\Users\\paugoldb\\Desktop\\Script Stuff\\PythonTemp\\2019_09_21_" + str(i) + "_Sherlock_Errors.xlsx"
    wb2 = x1.Workbooks.Open(Filename=currPath)
    ws2.Copy(Before=wb2.Worksheets(1))
    ws1.Copy(Before=wb2.Worksheets(1))

    wb2.Close(SaveChanges=True)
     
#quits "running" excel and the program is complete
x1.Quit()