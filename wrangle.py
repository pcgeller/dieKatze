# Create a munch object for sci-kit learn
from ingest import *
from munch import *
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
import os
from os import listdir
from os.path import isfile, join


##################################################
#For pulling the data from files (that only contain blobs of text)

filedata = readfiles(path)
def fMunch(dict):
    fm = Munch()
    fm.files = dict.keys()
    fm.text = dict.values()
    fm.target = []
    return(fm)

##################################################
#For pulling the data from a spreadsheet

# de-duplicate titles - this will mean that each abstract is assigned to a
# pseudo correct working group

subset = data[['EventID','ED_Track', 'Abstract Text','Title']]
dedup = subset.drop_duplicates(subset='Title')
df = dedup.dropna()

#Encode targets
le = preprocessing.LabelEncoder()
le.fit(df['ED_Track'])
df = df.assign(target=le.transform(df['ED_Track']))

#def clean(dfcolumn):
##Split to train and test
dftrain, dftest = train_test_split(df, test_size = .2)

def mkMunch(df):
    m = Munch()
    m.titles = list(df['Title'].values)
    m.text = list(df['Abstract Text'].values)
    m.WG = list(df['ED_Track'].values)
    m.target = list(df['target'].values)
    return(m)

#Polished data set for modeling
dataset = mkMunch(df)
train = mkMunch(dftrain)
test = mkMunch(dftest)

len(dftrain) + len(dftest)

#WORKSPACE
path = './data/mini_newsgroups/comp.graphics'
