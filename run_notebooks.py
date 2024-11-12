"""This is the master script to ensure that all notebooks are ran in a sequential order
for the most accurate results."""

import papermill as pm

# Paths to each script

# 1. Data Cleaning
data_cleaning = 'Task1DataCleaning.ipynb'

# 2. Encoding, Scaling, PCA, and K-Means
data_analysis = 'Task1DataAnalysis.ipynb'

# 3. Feature Importance
data_feature_importance = 'Task1FeatureImportance.ipynb'


# Run each script in order
pm.execute_notebook((data_cleaning), 'Task1DataCleaningOutput.ipynb')
pm.execute_notebook((data_analysis), 'Task1DataAnalysisOutput.ipynb')
pm.execute_notebook((data_feature_importance), 'Task1FeatureImportanceOutput.ipynb')
