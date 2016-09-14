#Full training pipeline
#Take munch and create train and test subset - MOVED to WRANGLE
#Fit model
#Test model
import time
from analysis import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


from sklearn import metrics
from sklearn import cross_validation
from sklearn.cross_validation import KFold

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline
#Tokenize
countVec = CountVectorizer()
trCount = countVec.fit_transform(train.text)

#Convert tokenized occurances to frequencies
tfTrans = TfidfTransformer(use_idf=False).fit(trCount)
trTF = tfTrans.transform(trCount)

tfidfTrans = TfidfTransformer()
trTFIDF = tfidfTrans.fit_transform(trCount)

#Model Naive Bayes
clf = MultinomialNB().fit(trTFIDF, train.target)
test = ['The military is using data science']
testCount = countVec.transform(test)
testTFIDF = tfidfTrans.transform(testCount)

predicted = clf.predict(testTFIDF)

##build pipeline
text_clf = Pipeline([('vect',CountVectorizer()),
('tfidf',TfidfTransformer()),
('clf',MultinomialNB()),
])
#Test Set Performance

def fit_and_evaluate(dataset, model, label, **kwargs):
    '''Function to run multiple models easily.'''
    start = time.time()
    scores = {'precision':[], 'recall':[], 'accuracy':[], 'f1':[]}

    for train, test in KFold(dataset.data.shape[0], n_folds=12, shuffle=True):
        Xtrain, Xtest = dataset.data[train], dataset.data[test]
        Ytrain, Ytest = dataset.target[train], dataset.target[test]

        estimator = model(**kwargs)
        estimator.fit(Xtrain, Ytrain)

        expected = Ytest
        predicted = estimator.predict(Xtest)

        #Save scores in dictionary
        scores['precision'].append(metrics.precision_score(expected, predicted, average="weighted"))
        scores['recall'].append(metrics.recall_score(expected, predicted, average="weighted"))
        scores['accuracy'].append(metrics.accuracy_score(expected, predicted))
        scores['f1'].append(metrics.f1_score(expected, predicted, average="weighted"))

    # Report
    print "Build and Validation of {} took {:0.3f} seconds".format(label, time.time()-start)
    print "Validation scores are as follows:\n"
    print pd.DataFrame(scores).mean()

    #Write the trained estimator to disc
    estimator = model(**kwargs)
    estimator.fit(dataset.data, dataset.target)

    outpath = label.lower().replace(" ", "-") + ".pickle"
    with open(outpath, 'w') as f:
        pickle.dump(estimator, f)

    print "\nFitted model written to:\n{}".format(os.path.abspath(outpath))

def decoder(codedarray, le = le):
    decoded = le.inverse_transform(codedarray)
    return(list(decoded))
