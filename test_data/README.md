# Test Data

This data was collected for the purpose of quick testing the 
[final model](https://github.com/CT15/dance-moves-prediction/blob/master/test_model/__init__.py), which
can be a combination of both Random Forest and Support Vector Machine (SVM), after each individual model training 
is done. The person who danced for the test data collection was randomly chosen. Each `.csv` file contains data collected
across a span of 30 seconds.

Note that the training process also involves measuring each model's (Random Forest and SVM) accuracy with respect 
to the test data. However, that test data is obtained from partitioning the 
[train data](https://github.com/CT15/dance-moves-prediction/tree/master/train_data).
