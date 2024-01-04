# This is an interactive demo, so feel free to change the code and click the 'Run' button.

# Simple classification on a subset of the standard machine learning covertype dataset.
# We'll first split the dataset into a training set and a testing set, then we'll train
# an mlpack Random Forest on the training data, and finally we'll print the accuracy of
# the random forest on the test dataset.

import mlpack
import pandas as pd
import numpy as np

# Load the dataset from an online URL.  Replace with "covertype.csv.gz" if you
# want to use on the full dataset.
df = pd.read_csv("https://www.mlpack.org/datasets/covertype-small.csv.gz")
#print(df)

# Split the labels.
labels = df["label"]
# print(labels)
dataset = df.drop("label", axis=1)
#print(dataset)

# Split the dataset using mlpack.  The output comes back as a dictionary,
# which we will unpack for clarity of code.
output = mlpack.preprocess_split(input_=dataset, input_labels=labels, test_ratio=0.3)
#print(output)

training_set = output["training"]
# print(training_set)
training_labels = output["training_labels"]
test_set = output["test"]
test_labels = output["test_labels"]

# Train a random forest.
output = mlpack.random_forest(training=training_set,
                              labels=training_labels,
                              print_training_accuracy=True,
                              num_trees=10,
                              minimum_leaf_size=3)
random_forest = output["output_model"]

# Predict the labels of the test points.
output = mlpack.random_forest(input_model=random_forest,
                              test=test_set)

# Now print the accuracy.  The "probabilities" output could also be used
# to generate an ROC curve.
correct = np.sum(
    output["predictions"] == np.reshape(test_labels, (test_labels.shape[0],)))
print(str(correct) + " correct out of " + str(len(test_labels)) + " (" + 
    str(100 * float(correct) / float(len(test_labels))) + "%).")
