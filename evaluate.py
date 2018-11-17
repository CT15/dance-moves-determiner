import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from termcolor import colored
from sklearn.metrics import f1_score, confusion_matrix

# Model id should either be 'RF' or 'SVM'
def evaluate(model, X_train, y_train, X_test, y_test, model_id, index=1):
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(colored("[EVAL]", "blue"), " f1 = " + str(f1) + "\t\ttrain_score =  " + str(train_score) + "\t\ttest_score = " + str(test_score))
    
    print(colored("[EVAL]", "blue"), " Generating confusion matrix ...")

    cm_df = pd.DataFrame(confusion_matrix(y_test, y_pred))
    print(cm_df)

    cm_df = cm_df[cm_df.columns].astype(int)
    hm = sn.heatmap(cm_df, annot=True)
    figure = hm.get_figure()

    figure_path = './eval_results/svm_conf' + str(index) + '.png' if model_id == 'SVM' else './eval_results/random_forest_conf' + str(index) + '.png'
    file_path = './eval_results/svm_eval' + str(index) +'.txt' if model_id == 'SVM' else './eval_results/random_forest_eval' + str(index) + '.txt'

    with open(figure_path, 'wb') as f:
        figure.savefig(f, dpi=600)
   
    file = open(file_path, 'a+')
    file.write("f1:\t" + str(f1) + "\ntrain_score:\t" + str(train_score) + "\ntest_score:\t" + str(test_score) + "\n")
    png_name = 'svm_conf' + str(index) + '.png' if model_id == 'SVM' else 'random_forest_conf' + str(index) + '.png'
    file.write("Confusion Matrix: [refer to " + png_name + "]\n")
    file.write("\n------------------------------ END\n")
    file.close()

    return test_score
