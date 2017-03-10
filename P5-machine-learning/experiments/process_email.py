#!/usr/bin/python
import os
import pickle
import re
import sys
import numpy as np
import pprint
from parse_out_email_text import parseOutText
	
	
def retrieve_emails(email_list):
	"""
		Process the emails in the email list to extract words and
		and get the documents ready for TF-IDF.
 
		The actual documents are in the Enron email dataset.
		
		Return the data stored as a list
	"""
	### name of everyone in the dataset, plus some other biased words
	bad_words = ['izzo', 'thomas', 'piper', 'gold', 'lewis', 'buchanan', 'charles', \
	             'soon', 'murray', 'roderick', 'scott', 'colleen', 'charlene', 'blake',\
	             'cumberland', 'louise', 'lavorato', 'elizabeth', 'jim', 'mcconnell',\
	             'stabler', 'dodson', 'diomedes', 'hermann', 'wrobel', 'rice', 'eugene',\
	             'piro', 'jere', 'mordaunt', 'wakeham', 'walls', 'christopher',\
	             'colwell', 'haug', 'rebecca', 'fugh', 'gray', 'gareth', 'james',\
	             'frank', 'michael', 'herbert', 'metts', 'martin', 'causey', 'pereira',\
	             'amanda', 'fallon', 'baxter', 'shapiro', 'fastow', 'carter', 'shankman',\
	             'gary', 'bhatnagar', 'brian', 'yeap', 'gahn', 'stanley', 'bay',\
	             'bannantine', 'wincenty', 'calger', 'koenig', 'rex', 'jeremy',\
	             'mcmahon', 'robert', 'hickerson', 'hannon', 'foy', 'sunde', 'sherriff',\
	             'mendelsohn', 'noles', 'daniel', 'jerome', 'wendy', 'kopper', 'donahue',\
	             'prentice', 'bibi', 'philippe', 'harold', 'janet', 'lawrence',\
	             'bergsieker', 'berberian', 'gathmann', 'jr', 'butts', 'wesley', 'joe',\
	             'skilling', 'sanjay', 'philip', 'overdyke', 'mccarty', 'muller', \
	             'kitchen', 'winokur', 'deffner', 'beck', 'cox', 'duncan', 'david', \
	             'mcdonald', 'franklin', 'cindy', 'gregory', 'gene', 'umanoff', 'julia', \
	             'terence', 'rieker', 'kristina', 'moran', 'steven', 'george', 'timothy',\
	             'whaley', 'dimichele', 'wodraska', 'keith', 'hayslett', 'haedicke', \
	             'mark', 'kishkill', 'detmering', 'joseph', 'olson', 'lou', 'white', \
	             'john', 'tod', 'buy', 'redmond', 'bowen', 'chan', 'peggy', 'andrew', \
	             'belfer', 'ferraz', 'rodney', 'badum', 'meyer', 'rockford', 'hughes', \
	             'kaminski', 'hirko', 'phillip', 'sullivanshaklovitz', 'lemaistre', \
	             'westfahl', 'hayes', 'ben', 'duran', 'wasaff', 'jay', 'norman', \
	             'powers', 'dana', 'bazelides', 'taylor', 'kenneth', 'brown', \
	             'scrimshaw', 'whalley', 'lowry', 'lindholm', 'echols', 'mitchell', \
	             'blachman', 'sharp', 'jaedicke', 'allen', 'frevert', 'reynolds', \
	             'kevin', 'walters', 'shelby', 'fitzgerald', 'mcclellan', 'paulo', \
	             'matthew', 'pickering', 'cline', 'gibbs', 'pai', 'elliott', 'horton', \
	             'ronnie', 'paula', 'jeffrey', 'delainey', 'raymond', 'garland', \
	             'savage', 'bruce', 'urquhart', 'dietrich', 'kean', 'cordes', \
	             'victoria', 'william', 'lay', 'jackson', 'gillis', 'christodoulou', \
	             'sally', 'humphrey', 'danny', 'belden', 'richard', 'yeager', 'sherrick',\
	             'thorn', 'leff', 'glisan', 'derrick', 'adam', 'fowler', 'gramm', \
	             'lockhart', 'tilney',\
	             'jskillin', 'wes', 'despain', 'dan', 'sheila']
	             
	word_data = ""
	
	with open(email_list, "r") as f:
		for path in f:
			path = path.replace("enron_mail_20110402/","")
			path = os.path.join('..',path[:-1])
			print path
			try:
				email = open(path,"r")
				### use parseOutText to extract the text from the opened email
				words = parseOutText(email)
				
				### use str.replace() to remove any instances of the words
				for word in bad_words:
					words = words.replace(word,"")
					
				### append the text to word_data
				#word_data.append(words)
				word_data += words
				
				email.close()
				
			except IOError as e:
				pass
				
	return [word_data]

from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import tree, grid_search		
from sklearn import ensemble
	
def vectorize_text(email_data):
	word_data = []
	poi_data = []
	
	for name in email_data.keys():
		poi = email_data[name]["poi"]
		word_data.extend(email_data[name]["from"])
		word_data.extend(email_data[name]["to"])
		pois = [poi] * 2
		poi_data.extend(pois)
	
	"""
	172 emails to read from  86 people, 14 of which are POIs.
	They have 28 emails.
	"""
	i = 1
	keywords = {}
	vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.95, stop_words='english') #max_df=0.35, min_df=2
	cv = cross_validation.StratifiedShuffleSplit(poi_data, 100, random_state = 42)
	for train_idx, test_idx in cv:
		print "processing fold..." 
		features_train = []
		features_test  = []
		labels_train   = []
		labels_test    = []
		for ii in train_idx:
			features_train.append( word_data[ii] )
			labels_train.append( poi_data[ii] )
		
		### fit the classifier using training set, and test on test set
		features_train = vectorizer.fit_transform(features_train)
		vocabulary = vectorizer.get_feature_names()
		
		clf = tree.DecisionTreeClassifier(criterion='entropy',random_state=39)
		clf.fit(features_train, labels_train)
		
		num_important = np.sum(clf.feature_importances_ > 0)        
		important = np.argsort(clf.feature_importances_)[-num_important:]
		from operator import itemgetter        
		features = list(itemgetter(*important)(vocabulary) )
		importances = list( itemgetter(*important)(clf.feature_importances_))
		for i in range(num_important):
			feature = features[i]
			if feature in keywords.keys():
				keywords[feature]["count"] += 1
				keywords[feature]["importance"].append(importances[i])
			else:
				keywords[feature] = {}
				keywords[feature]["count"] = 1
				keywords[feature]["importance"] = [importances[i]]
		i += 1
	
	for keyword in keywords.keys():
		if keywords[keyword]["count"] < 10:
			keywords.pop(keyword)
		else:
			keywords[keyword]["importance"] = np.mean(keywords[keyword]["importance"])
	
	pprint.pprint( keywords)
	
	return keywords.keys()

	"""	
	features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, poi_data, test_size=0.1, random_state=81)

	### TfIdf vectorization
	vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.95, stop_words='english') #max_df=0.35, min_df=2
	features_train = vectorizer.fit_transform(features_train)
	features_test = vectorizer.transform(features_test)
	vocabulary = vectorizer.get_feature_names()
	print len(vocabulary), "words in vocabulary"
	
	
	### a classic way to overfit is to use a small number
	### of data points and a large number of features;
	### train on only 150 events to put ourselves in this regime
	#features_train = features_train[:20]
	#labels_train   = labels_train[:20]
	print "DecisionTreeClassifier(criterion='entropy')"
	
	clf = tree.DecisionTreeClassifier(criterion='entropy',random_state=39)
	clf.fit(features_train,labels_train)
	
	pred = clf.predict(features_test)
	
	print "r^2 on training data:",clf.score(features_train,labels_train)
	print "r^2 on test data:",clf.score(features_test,labels_test)
	
	num_important = np.sum(clf.feature_importances_ > 0)
	important = np.argsort(clf.feature_importances_)[-num_important:]
	from operator import itemgetter
	print itemgetter(*important)(vocabulary)
	print itemgetter(*important)(clf.feature_importances_)	
	print vectorizer.stop_words_
	
	selection = set(important)
	
	dt = tree.DecisionTreeClassifier(criterion='entropy')
	
	params = {'n_estimators':[3, 6, 12, 25, 50, 100, 150],'learning_rate':[0.0625, 0.125, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0]}
	clf = ensemble.AdaBoostClassifier(base_estimator=dt, random_state=16)
	gs = grid_search.GridSearchCV(clf,params)
	gs.fit(features_train, labels_train)
	
	params = gs.best_params_
	print "GridSearchCV"
	print "AdaBoostClassifer(base_estimator=DecisionTreeClassifier(criterion='entropy'),",params,")"
	
	clf = ensemble.AdaBoostClassifier(base_estimator=dt,
						n_estimators=params['n_estimators'],
						learning_rate=params['learning_rate'],
						random_state=82)
	clf.fit(features_train, labels_train)
	
	print "r^2 on training data:",clf.score(features_train,labels_train)
	print "r^2 on test data:",clf.score(features_test,labels_test)
	
	num_important = np.sum(clf.feature_importances_ > 0)
	important = np.argsort(clf.feature_importances_)[-num_important:]
	from operator import itemgetter
	print itemgetter(*important)(vocabulary)
	print itemgetter(*important)(clf.feature_importances_)
		
	selection = selection.union(set(important))
	
	selection = list(selection)
	
	return list(itemgetter(*selection)(vocabulary))
	"""