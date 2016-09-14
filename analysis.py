from wrangle import *
from pandas.tools.plotting import scatter_matrix

scatter_matrix(df, alpha=0.2, figsize = (12,12), diagonal = 'kde')
