import os
from niaaml import PipelineOptimizer, Pipeline
from niaaml.data import CSVDataReader

"""
In this example, we show how to use the PipelineOptimizer class. This example is using an instance of CSVDataReader.
The instantiated PipelineOptimizer will try and assemble the best pipeline with the components that are specified in its constructor.
We use a dataset with 1 categorical feature to demonstrate a use of PipelineOptimizer instance with automatic feature encoding.
"""

# prepare data reader using csv file
data_reader = CSVDataReader(src=os.path.dirname(os.path.abspath(__file__)) + '/example_files/dataset_categorical.csv', has_header=False, contains_classes=True)

# instantiate PipelineOptimizer that chooses among specified classifiers, feature selection algorithms and feature transform algorithms
# OneHotEncoder is used for encoding categorical features in this example
pipeline_optimizer = PipelineOptimizer(
    data=data_reader,
    classifiers=['AdaBoost', 'Bagging', 'MultiLayerPerceptron', 'RandomForest', 'ExtremelyRandomizedTrees', 'LinearSVC'],
    feature_selection_algorithms=['SelectKBest', 'SelectPercentile', 'ParticleSwarmOptimization', 'VarianceThreshold'],
    feature_transform_algorithms=['Normalizer', 'StandardScaler'],
    categorical_features_encoder='OneHotEncoder'
)

# runs the optimization process
# one of the possible pipelines in this case is: SelectPercentile -> Normalizer -> RandomForest
# returns the best found pipeline
# the chosen fitness function and optimization algorithm are Accuracy and Particle Swarm Algorithm
pipeline = pipeline_optimizer.run('Accuracy', 20, 20, 400, 400, 'ParticleSwarmAlgorithm', 'ParticleSwarmAlgorithm')

# pipeline variable contains Pipeline object that can be used for further classification, exported as an object (that can be later loaded and used) or exported as text file