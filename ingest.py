#Load the data into Python so it can be turned into a
#bunch object
import csv
import sys
import pandas as pd

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

data = asDF(filename)
headers = list(data.columns.values)


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
