# Identify Fraud from Enron Email

## Using Machine Learning to Identify Persons of Interest in Fraud Investigations

| File                    | Description     |
| :---------------------- | :-------------- |
| startup.py              | Checks for dependencies and downloads and unzips the email dataset |
| poi_id.py               | Main file (builds and trains the classifier); generates the pickle files |
| process_email.py        | Processes the emails of the Enron email dataset and generates a vocabulary for TF-IDF |
| parse_out_email_text.py | Parses and stems email text data using the Snowball Stemmer |
| tester.py               | Evaluates model for accuracy, precision, and recall |
| my_classifier.pkl       | Trained classifier as pickle file |
| my_dataset.pkl          | Data set used to train classifier (only contains selected features) |
| my_feature_list.pkl     | Selected feature keys for dataset |
| tools                   | Contains starter code for project |
| experiments             | Contains experimental code for feature and algorithm selection |

##### Dependencies

- nltk
- scipy
- numpy
- sklearn

##### Usage

Download the dataset (This takes a while to complete.)

```
python startup.py
```

To re-build and train the model<br/>
(NOTE: During the initial run, the email text data is processed to generate email_word.pkl. Currently, this takes a while (hours) to complete.)

```
python poi_id.py
```

To evaluate the trained model

```
python tester.py
```

### Introduction

The goal of this project is to use machine learning to find a way to identify persons of
interest in fraud investigations. We will use the public dataset from the Enron scandal
and build an algorithm to identify Enron employees who may have committed fraud. This
dataset includes the financial and email data from the time the crimes were being
committed. Persons of interest in this case refer to anyone who was indicted, reached a
settlement or plea deal with the government, or testified in exchange for prosecution
immunity.

### Enron Dataset

We need to determine if there is adequate data for this task and then identify the
important features for the algorithm. While exploring the data and investigating the
outliers, there was one outlier that needed to be removed from the dataset. That data
point represented the sum totals of the financial data. We only want to consider the
employees in this investigation so The Travel Agency in the Park data was removed as well.
The other outliers found were actual people and some were persons of interest in the
scandal. We can't remove those persons of interest from the data, but the fact that they
are outliers may be useful in classification. The resulting dataset contained 144 people,
18 of whom were persons of interest. Of the 144 people, 86 had email data to be reviewed
and 14 of those people were persons of interest in this case.

### Feature Selection

The financial features (in US dollars) of the dataset are 'salary', 'deferral_payments',
'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred',
'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other',
'long_term_incentive', 'restricted_stock', and 'director_fees.' The email features are
'to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages',
'from_this_person_to_poi', and 'shared_receipt_with_poi.' The email text data was
converted to term frequency-inverse document frequency representation, and the eight most
important features were selected for building the algorithm. These keywords were found
using the feature importances of a decision tree algorithm; perhaps they could be
potential flags in fraud investigations in the future. Table 1 shows the accuracy,
precision, and recall metrics of different feature combinations. We are looking for the
feature combination that can be used to train a classifier with greater than 0.3 precision
and recall.<br/>
<br/>
##### TABLE 1 - EVALUATION METRICS FOR SELECTED FEATURE COMBINATIONS

| Feature                    | Trial 1 | Trial 2 | Trial 3 | Trial 4 | Trial 5 | Trial 6 | Trial 7 |
| :------------------------- |:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| salary                     | &#10003;| &#10003;| &#10003;|         |         | &#10003;|         |
| deferral_payments          | &#10003;| &#10003;|         |         |         |         |         |
| total_payments             | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
| loan_advances              | &#10003;| &#10003;|         |         |         |         |         |
| bonus                      | &#10003;| &#10003;|         |         |         |         |         |
| restricted_stock_deferred  | &#10003;| &#10003;|         |         |         |         |         |
| deferred_income            | &#10003;| &#10003;|         |         |         |         |         |
| total_stock_value          | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
| expenses                   | &#10003;| &#10003;|         |         |         |         |         |
| exercised_stock_options    | &#10003;| &#10003;| &#10003;| &#10003;|         | &#10003;| &#10003;|
| other                      | &#10003;| &#10003;|         | &#10003;|         |         |         |
| long_term_incentive        | &#10003;| &#10003;|         |         |         |         |         |
| restricted_stock           | &#10003;| &#10003;|         |         |         |         |         |
| director_fees              | &#10003;| &#10003;|         |         |         |         |         |
| to_messages                | &#10003;| &#10003;|         |         |         |         |         |
| from_poi_to_this_person    | &#10003;| &#10003;| &#10003;|         | &#10003;|         |         |
| from_messages              | &#10003;| &#10003;|         |         |         |         |         |
| from_this_person_to_poi    | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|         |
| shared_receipt_with_poi    | &#10003;| &#10003;| &#10003;|         | &#10003;|         |         |
| audit_tfidf                |         | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
| keeper_tfidf               |         | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
| allegheni_tfidf            |         | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
| messr_tfidf                |         | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
| blown_tfidf                |         | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
| blockbust_tfidf            |         | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
| ascrib_tfidf               |         | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
| x31770_tfidf               |         | &#10003;| &#10003;| &#10003;| &#10003;| &#10003;| &#10003;|
|                            |         |         |         |         |         |         |         |
| ***Accuracy***             | 0.81087 | 0.81567 | 0.83347 | 0.83280 | 0.83147 | 0.83027 | 0.85147 |
| ***Precision***            | 0.24528 | 0.28738 | 0.36642 | 0.35006 | 0.36134 | 0.32787 | 0.43230 |
| ***Recall***               | 0.22125 | 0.25850 | 0.34150 | 0.29650 | 0.34400 | 0.26000 | 0.36400 |

<br/>
Feature scaling was not necessary because decision trees do not depend on standardization
of data. Features would still split in the same manner even with different scales.
Although this is suitable for this investigation, scaling would need to be revisited for
other investigations because their financials and thereby the thresholds could be very
different. Table 2 shows the selected features and their feature importances in a decision
tree. The features with the '_tfidf' suffix are the keywords selected from the email text
data. <br/>
<br/>
##### TABLE 2 - DECISION TREE IMPORTANCES OF THE SELECTED FEATURES

| Feature                    | Importance |
| :------------------------- |:----------:|
| exercised_stock_options    |   0.17304  |
| total_payments             |   0.15315  |
| total_stock_value          |   0.13378  |
| audit_tfidf                |   0.10959  |
| keeper_tfidf               |   0.09822  |
| allegheni_tfidf            |   0.09132  |
| messr_tfidf                |   0.08577  |
| blown_tfidf                |   0.07968  |
| blockbust_tfidf            |   0.03981  |
| ascrib_tfidf               |   0.02362  |
| x31770_tfidf               |   0.01203  |

<br/>

### Model Selection

The final algorithm used was an AdaBoost classifier with a decision tree classifier as the
base estimator. Table 3 shows the different algorithms tested and the performance of each.
For the comparison I used grid search to tune the parameters of each algorithm, where
applicable.<br/>
<br/>
##### TABLE 3 - EVALUATION METRICS BY ALGORITHM

| Algorithm                         | Accuracy  | Precision | Recall   |  
| :-------------------------------- |:---------:|:---------:|:--------:|
| Gaussian Naive Bayes              | 0.84780   | 0.37642   | 0.21550  |
| Decision Tree                     | 0.88027   | 0.62000   | 0.26350  |
| k-Nearest Neighbors               | 0.87980   | 0.63662   | 0.22950  |
| AdaBoost                          | 0.87007   | 0.51936   | 0.34200  |
| AdaBoost (w/ tuned Decision Tree) | 0.88813   | 0.64478   | 0.35850  |

<br/>
Tuning the parameters of an algorithm is finding the parameters of a given classifier that
optimize the algorithm's performance.  Ideally, overfitting will not occur in the
resulting model. Otherwise, the model will not perform well on an independent data set.
Grid search was used to tune the parameters of the AdaBoost classifier and its decision
tree base estimator. The following the parameters were removed from the search so that the
desired metrics would be repeatable: the base estimator's split criterion, split strategy,
and maximum tree depth.

### Validation

Validation is a method of evaluating how well a model performs on an independent data set.
In cross-validation a dataset is split into training and test sets, with the test set
representing the unknown data. If validation is not done well, a classifier could suffer
from overfitting and fail to accurately classify not yet seen data. The classifier would
just repeat what it learned from the training data. And depending on how the data is split
in cross-validation, it is possible that the training or test sets could lack instances of
one or more of the classes being learned. Then you could not be certain the classifier had
the desired performance.<br/>
<br/>
A shuffle split was used to generate six random permutations of training and test data.
The average accuracy, precision, and recall of the model's performance on each permutation
were computed. Both the model's precision and recall were greater than 0.3 as desired.

### Evaluation

The AdaBoost classifier successfully labeled the Enron employees as persons of interest
with 88.8% accuracy on average with a precision of 0.64 and 0.36 recall on average. This
means the model erroneously classifies 11.2% of the employees. The precision is a measure
of how confident we can be that employees identified as persons of interest need to be
scrutinized further. The recall score means that we may miss a lot of employees that
require further investigation.<br/>
<br/>
We found out that machine learning can be used to identify persons of interest in fraud
investigations. 64% of the people identified as persons of interest in a fraud
investigation may actually be guilty and the investigation is heading in the right
direction. Unfortunately, 64% of the people not flagged as persons of interest are flying
under the model’s radar. Perhaps there exists some kind of relationship between these
people and the positively identified. That is an area of future exploration and model
building.

<br/>
***I hereby confirm that this submission is my work. I have cited above the origins
of any parts of the submission that were taken from Websites, books, forums,
blog posts, github repositories, etc.***