#Load the data into Python so it can be turned into a
#bunch object
import csv
import sys
import pandas as pd
# with open('./data/mors.csv','rb') as f:
#     reader = csv.reader(f)
#     try:
#         for row in reader:
#             print(row)
#     except csv.Error as e:
#         sys.exit('File %s, line %d: %s' % (filename, reader.line_num, e))

#!!!! File encoding problems.  KLUDGE!

#filename = './data/mors8.csv'
reader = csv.reader(open('./data/mors8.csv','r'))
for row in reader:
    print(row)

with open('./data/mors8.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = pd.read_csv('./data/mors8.csv')
headers = list(data.columns.values)


# filename )= './data/mors.csv'
# reader =' csv.reader(open(filename, 'rb'))
# try:
#     for row in reader:
#         print(row)
#     except csv.Error as e:
#         sys.exit('file %s, line %d: %s' % (filename, reader.line_num,e))
>>>>>>> 4fc67a443e017ea2890facfbc75a45c562b6e5e7
