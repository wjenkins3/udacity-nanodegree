#!/usr/bin/python

import sys
import pickle
import numpy as np
sys.path.append("../tools/")
sys.path.append("../choose_your_own")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from process_email import retrieve_emails, vectorize_text

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','exercised_stock_options','total_payments','total_stock_value']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
data_dict.pop("TOTAL")
data_dict.pop("THE TRAVEL AGENCY IN THE PARK")

### Task 3: Create new feature(s)
### Load email data
try:
	with open("email_word_data.pkl","r") as f:
		enron_email_data = pickle.load(f)
# if it doesn't already exist, generate it
except IOError as e:
	enron_email_data = {}
	
	for name in data_dict.keys():
		if data_dict[name]["from_messages"] != 'NaN':
			person = {}
			person["poi"] = data_dict[name]["poi"]
			email_path = "./emails_by_address/"
			email = data_dict[name]["email_address"]
			from_word_data = retrieve_emails(email_path + "from_" + email + ".txt")
			to_word_data = retrieve_emails(email_path + "to_" + email + ".txt")
			person["combined"] = from_word_data[0] + to_word_data[0]
			enron_email_data[name] = person
		
		with open("email_word_data.pkl","w") as f:
			pickle.dump(enron_email_data,f)
	pass

### keywords found from vectorizing text and selecting important features
### feature_words = vectorize_text(enron_email_data)
feature_words = ['allegheni','ascrib','audit','blockbust','blown','keeper','messr','x31770']
word_data = []

names = data_dict.keys()

for name in names:
	if data_dict[name]["from_messages"] == 'NaN':
		word_data.append("")
	else:
		word_data.append(enron_email_data[name]["combined"])
		
from sklearn.feature_extraction.text import TfidfVectorizer
### TfIdf vectorization
vectorizer = TfidfVectorizer(sublinear_tf=True, vocabulary=feature_words, stop_words='english')
vectorizer.fit(word_data)
values = vectorizer.transform(word_data).todense()

email_features = []
for word in feature_words:
	name = word + "_tfidf"
	email_features.append(name.encode('UTF-8'))
	 
features_list.extend(email_features)

for i in range(len(names)):
	tfidf = {}
	for j in range(len(email_features)):
		tfidf[email_features[j]] = values[i,j]
	data_dict[names[i]].update(tfidf)

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html
from sklearn import metrics
from sklearn.cross_validation import cross_val_score, ShuffleSplit
from tester import test_classifier	

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
from sklearn import tree, ensemble

dtc = tree.DecisionTreeClassifier(criterion='entropy',
                             max_features=None,
                             max_leaf_nodes=None,
                             min_samples_leaf=3,
                             min_samples_split=1,
                             min_weight_fraction_leaf=0.001)

clf = ensemble.AdaBoostClassifier(base_estimator=dtc,
                                  n_estimators=70,
                                  learning_rate=0.675)

clf.fit(features_train,labels_train)

cv = ShuffleSplit(len(labels),n_iter=6,test_size=0.15)
score = cross_val_score(clf,features,labels,cv=cv,scoring='accuracy').mean()
print "Accuracy:", score
score = cross_val_score(clf,features,labels,scoring='precision',cv=6).mean()
print "Precision:", score
score = cross_val_score(clf,features,labels,scoring='recall',cv=6).mean()
print "Recall:", score

print "From tester.py:"
test_classifier(clf,my_dataset,features_list)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)