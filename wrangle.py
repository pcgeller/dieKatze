# Create a bunch object for sci-kit learn
from ingest import *

# de-duplicate titles - this will mean that each abstract is assigned to a
# pseudo correct working group

dedup = data.drop_duplicates(subset='Title')

b = Bunch

b.titles = dedup['Title']
b.text = dedup['Abstract Text']
b.WG = dedup['ED_Track']
