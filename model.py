#Full training pipeline
#Take munch and create train and test subset - MOVED to WRANGLE
#Fit model
#Test model
import os.path
import time
import pickle as pkl
from analysis import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


from sklearn import metrics
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn.metrics import f1_score
from sklearn import grid_search

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier

from sklearn.pipeline import Pipeline
#Tokenize
countVec = CountVectorizer(stop_words = 'english', ngram_range=(1,3))
trCount = countVec.fit_transform(train.text)

fullCount = countVec.fit_transform(dataset.text)
fullTrans = TfidfTransformer(use_idf=False).fit(fullCount)
fullTF = fullTrans.transform(fullCount)

#Convert tokenized occurances to frequencies
tfTrans = TfidfTransformer(use_idf=False).fit(trCount)
trTF = tfTrans.transform(trCount)

tfidfTrans = TfidfTransformer()
trTFIDF = tfidfTrans.fit_transform(trCount)

fullTFIDF = tfidfTrans.fit_transform(fullCount)

#Model Naive Bayes
clf = MultinomialNB().fit(trTFIDF, train.target)
test = ['The military is using data science']
testCount = countVec.transform(test)
testTFIDF = tfidfTrans.transform(testCount)

# predicted = clf.predict(test)

##build pipeline
text_clf = Pipeline([('vect',CountVectorizer()),
('tfidf',TfidfTransformer()),
('clf',MultinomialNB()),
])
#Test Set Performance

dataset.features = fullTFIDF
dataset.target = np.asarray(dataset.target)
def fit_and_evaluate(dataset, model, label, **kwargs):
    '''Function to run multiple models easily.'''
    start = time.time()
    scores = {'precision':[], 'recall':[], 'accuracy':[], 'f1':[]}

    for train, test in KFold(dataset.features.shape[0], n_folds=12, shuffle=True):
        Xtrain, Xtest = dataset.features[train], dataset.features[test]
        Ytrain, Ytest = dataset.target[train], dataset.target[test]

        estimator = model(**kwargs)
        estimator.fit(Xtrain, Ytrain)

        expected = Ytest
        predicted = estimator.predict(Xtest)
        #print(predicted)

        #Save scores in dictionary
        scores['precision'].append(metrics.precision_score(expected, predicted, average="weighted"))
        scores['recall'].append(metrics.recall_score(expected, predicted, average="weighted"))
        scores['accuracy'].append(metrics.accuracy_score(expected, predicted))
        scores['f1'].append(metrics.f1_score(expected, predicted, average="weighted"))

    # Report
    #print("Build and Validation of {} took {:0.3f} seconds".format(label, time.time()-start))
    print("Validation scores are as follows:\n")
    print(pd.DataFrame(scores).mean())

    #Write the trained estimator to disc
    estimator = model(**kwargs)
    estimator.fit(dataset.features, dataset.target)

    outpath = label.lower().replace(" ", "-") + ".pickle"
    with open(outpath, 'wb') as f:
        pkl.dump(estimator, f)

    print("\nFitted model written to:\n{}".format(os.path.abspath(outpath)))

def decoder(codedarray, le = le):
    decoded = le.inverse_transform(codedarray)
    return(list(decoded))

fit_and_evaluate(dataset,SVC,"Support Vector")
fit_and_evaluate(dataset, KNeighborsClassifier,"KNN", n_neighbors=12)
fit_and_evaluate(dataset, RandomForestClassifier, "Random Forest")
fit_and_evaluate(dataset, SGDClassifier, "SGD", loss = 'hinge', penalty = 'l2',alpha=1e-3, n_iter=5, random_state=4)
fit_and_evaluate(dataset, MultinomialNB, "Naive Bayes")

SVparam = {'kernel':('linear','poly','rbf','sigmoid'), 'degree':range(1,10)}
