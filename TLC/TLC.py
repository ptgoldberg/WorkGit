import csv
import os
import time


def TLCLookUp():
    #this allows for this script to run with direct user input and minimizing the actual need to modify the script itself. 
    file_name = input('Paste file name here: ')
    data_name = input('Input what column data name you are looking for: ')
    search_name = input('Input the search data for ' + data_name + ': ')

    #I left this section here for ease of testing the script, it will be commented out in production
    """ file_name = 'For_Hire_Vehicles__FHV__-_Active.csv'
    data_name = 'DMV License Plate Number'
    search_name = '05REGION' """

    #this section makes sure the current directory is where the actual python file is, this is to aid in ease of setup for non technical people using this script
    #without redefining the chdir, the output file was popping up in the file above this current one
    absolute_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(absolute_path)
    os.chdir(dir_name)

    #this section opens the input file based on the file_name input 
    input_file = csv.DictReader(open(dir_name + '\\' + file_name))

    #this creates a new csv file for the output of this script
    #I used the timestamp as a way to ensure that files aren't being overwritten
    with open(search_name + '_output_' + str(int(time.time())) + '.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)

        #this is basically the only hard coded section of the script as I assumed that these are the common data points being pulled. 
        #if there was a rising need for people to pull different column data, I could create an option to input a separate csv file name for all the column names that a user would want
        #and it would replace this data_titles list with the data from the input file. 
        data_titles = ['Vehicle License Number', 'DMV License Plate Number', 'Vehicle VIN Number', 'Base Number']

        #this writes the data titles to the first row of the output CSV
        wr.writerow(data_titles)

        for row in input_file:
            if row[data_name] == search_name:
                wr.writerow([row[data_titles[0]], row[data_titles[1]], row[data_titles[2]], row[data_titles[3]]])

    print('File Created!')

if __name__ == '__main__':
    TLCLookUp()