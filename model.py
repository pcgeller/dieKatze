#Full training pipeline
#Take munch and create train and test subset - MOVED to WRANGLE
#Fit model
#Test model
import sklearn as sk
from sklearn.feature_extraction.text import CountVectorizer
countVec = CountVectorizer()
trCount = countVec.fit_transform(train.text)
