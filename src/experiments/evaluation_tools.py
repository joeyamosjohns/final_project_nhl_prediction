from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, confusion_matrix
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns



def evaluate_binary_classification(model_name, y_test, y_pred, y_proba=None):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    #try:
    if y_proba != None:
        rocauc_score = roc_auc_score(y_test, y_proba)
    else:
        rocauc_score = "no roc"
    #except: 
    #    pass     
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True)
    plt.tight_layout()
    plt.title(f'{model_name}', y=1.1)
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.show()
    print("accuracy: ", accuracy)
    print("precision: ", precision)
    print("recall: ", recall)
    print("f1 score: ", f1)
    print("rocauc: ", rocauc_score)
    print(cm)
    #return accuracy, precision, recall, f1, rocauc_score

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, f1_score

def evaluate_regression(y_test, y_pred):
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("mae", mae)
    print("mse", mse)
    print('r2', r2)

