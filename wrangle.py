# Create a bunch object for sci-kit learn
from ingest import *
from bunch import *

# de-duplicate titles - this will mean that each abstract is assigned to a
# pseudo correct working group


subset = data[['EventID','ED_Track', 'Abstract Text','Title']]
dedup = subset.drop_duplicates(subset='Title')
dropNaN = dedup.dropna()

def mkBunch(df):
    b = Bunch()
    b.titles = df['Title']
    b.text = df['Abstract Text']
    b.WG = df['ED_Track']
    return(b)
