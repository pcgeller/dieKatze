#Load the data into Python so it can be turned into a
#bunch object
import csv
import sys
import pandas as pd
import os
from os import listdir
from os.path import isfile, join


###############################################################333
# This ingest works for pulling data stored in indivdual files within
# a folder
def readfiles(path):
    d = {}
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print("File list: ", onlyfiles[0:4])
    for filename in onlyfiles:
        print('Filename: ', filename)
        filepath = os.path.join(path,filename)
        print("Filepath: ", filepath)
        try:
            with open(filepath, 'r') as f:
                d[filename] = f.read()
        except UnicodeDecodeError:
            with open(filepath,'r', encoding = "ISO-8859-1") as f:
                d[filename] = f.read()
    return(d)


############################################################
# This ingest works for pulling data from a spreadsheet

#Open up the data as and keep it as a list
def asList(filename):
    with open(filename, 'r') as f:
        try:
            reader = csv.reader(f)
            data = list(reader)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num,e))
        return(data)

#Open up the data as a pandas dataframe
def asDF(filename):
    data = pd.read_csv(filename)
    return(data)

#WORKSPACE
filename = './data/mors8.csv'
path = './data/mini_newsgroups/comp.graphics'

data = asDF(filename)
headers = lisdata(data.columns.values)

#file = onlyfiles[1]



# filename = './data/mors.csv'
# reader =' csv.reader(open(filename, 'rb'))
# try:
#     for row in reader:
#         print(row)
#     except csv.Error as e:
#         sys.exit('file %s, line %d: %s' % (filename, reader.line_num,e))

#Show the data
#filename = './data/mors8.csv'
# reader = csv.reader(open('./data/mors8.csv','r'))
# for row in reader:
#     print(row)
