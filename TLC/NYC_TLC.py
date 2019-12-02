import csv
import os
import time

""" file_name = input('Paste file name here: ')
data_name = input('Input what column data name you are looking for: ')
search_name = input('Input the search data for ' + data_name + ': ') """

file_name = 'For_Hire_Vehicles__FHV__-_Active.csv'
data_name = 'DMV License Plate Number'
search_name = 'BMC11'

cwd = os.path.dirname(os.path.realpath(__file__))
input_file = csv.DictReader(open(cwd + '\\' + file_name))

search_list = []

with open(data_name + '_output_' + str(int(time.time())) + '.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    data_titles = ['Vehicle License Number', 'DMV License Plate Number', 'Vehicle VIN Number', 'Base Number']
    wr.writerow(data_titles)
#i = 0
    for row in input_file:
        if row[data_name] == search_name:
            for title in data_titles:
                wr.writerow([row[title]])
            #wr.writerow([row[data_titles[0]], row[data_titles[1]], row[data_titles[2]], row[data_titles[3]]])


#print(search_list) 