import test_data
import pandas as pd
import preprocess as prep
from test_model import MLModel
from sklearn.metrics import accuracy_score
from termcolor import colored
from sklearn.metrics import f1_score, confusion_matrix

if __name__ == "__main__":
    _, test_df = prep.split_train_test(test_data.load(), train_percent=0)
    X_test, y_test = prep.get_X_y(test_df)
    
    model = MLModel()
    
    y_pred = model.test_predict(X_test)
    test_score = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(colored("[EVAL]", "blue"), " f1 = " + str(f1) + "\t\ttest_score = " + str(test_score))
    
    print(colored("[EVAL]", "blue"), " Generating confusion matrix ...")

    cm_df = pd.DataFrame(confusion_matrix(y_test, y_pred))
    print(cm_df)